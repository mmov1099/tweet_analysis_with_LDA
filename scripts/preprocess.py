import glob
import json
import os
import pickle
import re
import urllib.request

import gensim
import MeCab

# jsonファイルからTweetを取り出して辞書で返す
def json2texts(path='data/tweet/*') -> dict:
    tweet_path_list = glob.glob(path)
    # key:tweet id, value:tweet text
    texts = dict()
    for path in tweet_path_list[:2816]:
        with open(path) as f:
            tweet = json.load(f)
        for t in tweet['tweets']:
            texts[t['id']] = t['text']
    return texts

#Neologdによるトーカナイザー(リストで返す関数・名詞のみ)
class MecabTokenizer():
    # pathはNEologdのパス
    def __init__(self, path="-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd") -> None:
        # ストップワードの一覧
        url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'

        # ストップワードの取得
        with urllib.request.urlopen(url) as response:
            self.stopwords = [w for w in response.read().decode().split('\r\n') if w != '']

        # ストップワードに除去したい文字列を追加
        self.stopwords += ['ReTweet', '*']

        # NEologdのパス
        self.mecab = MeCab.Tagger(path)

    def tockenize(self, text):
        replaced_text = text.lower()
        replaced_text = re.sub(r'[【】]', ' ', replaced_text)       # 【】の除去
        replaced_text = re.sub(r'[（）()]', ' ', replaced_text)     # （）の除去
        replaced_text = re.sub(r'[［］\[\]]', ' ', replaced_text)   # ［］の除去
        replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # メンションの除去
        replaced_text = re.sub(r'\d+\.*\d*', '', replaced_text) #数字を0にする
        replaced_text = re.sub(r'[#＃]', '', replaced_text)

        # ノイズとして取り除くパターン
        rt = re.compile(r'^RT\s*')
        mention = re.compile(r'\s*@\w+:\s*')
        url = re.compile(r'\s*https?://[\w/:%#\$&\?\(\)~\.=\+\-]+\s*')

        # ノイズ除去
        replaced_text = rt.sub('', replaced_text)
        replaced_text = mention.sub(' ', replaced_text)
        replaced_text = url.sub(' ', replaced_text)

        parsed_lines = self.mecab.parse(replaced_text).split("\n")[:-2]

        # #表層形を取得
        # surfaces = [l.split('\t')[0] for l in parsed_lines]
        #原形を取得
        token_list = [l.split("\t")[1].split(",")[6] for l in parsed_lines]
        #品詞を取得
        pos = [l.split('\t')[1].split(",")[0] for l in parsed_lines]
        # 名詞,動詞,形容詞のみに絞り込み
        target_pos = ["名詞", '形容詞', '副詞']
        token_list = [t for t, p in zip(token_list, pos) if p in target_pos]

        # stopwordsの除去
        token_list = [t for t in token_list if t  not in self.stopwords]

        # ひらがなのみの単語を除く
        kana_re = re.compile("^[ぁ-ゖ]+$")
        token_list = [t for t in token_list if not kana_re.match(t)]

        return token_list

def tokenize(texts, save_dir='model'):
    tokenizer = MecabTokenizer()
    tokenized_texts = {}
    for k, v in texts.items():
        tokenized_texts[k] = tokenizer.tockenize(v)
    with open(save_dir+"/tokenized_texts.pkl", "wb") as f:
        pickle.dump(tokenized_texts, f)
    return tokenized_texts

def make_dict(texts_words, no_below=5, no_above=0.5, save_dir='model'):
    # 辞書の作成
    dictionary = gensim.corpora.Dictionary(texts_words.values())
    dictionary.filter_extremes(no_below, no_above)
    dictionary.save_as_text(save_dir + '/wordid.txt')
    return dictionary

def make_corpus(texts_words, dictionary, save_dir='model'):
    corpus = [dictionary.doc2bow(words) for words in texts_words.values()]
    # コーパスをテキストファイルで保存する場合
    gensim.corpora.MmCorpus.serialize(save_dir+'/corpus.mm', corpus)
    # corpus = gensim.corpora.MmCorpus('blog_corpus.mm')
    # save corpus
    with open(save_dir+"/corpus.pkl",'wb') as f:
        pickle.dump(corpus,f)
    return corpus

def make_corpus_tfidf(texts_words, dictionary, save_dir='model'):
    corpus = make_corpus(texts_words, dictionary)
    tfidf = gensim.models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    with open(save_dir+'/tfidf.pkl', mode='wb') as f:
        pickle.dump(corpus_tfidf, f)
    return corpus_tfidf

def main(args):
    os.makedirs('model', exist_ok=True)

    # データからTweetを取り出す
    texts = json2texts()
    print(f'Data is {len(texts)} tweets')

    # トークナイズする
    print('Tokenizing...')
    tokenized_texts = tokenize(texts)
    print('Words count is {}'.format(sum([len(t) for t in tokenized_texts.values()])))

    # 辞書を作成
    dictionary = make_dict(tokenized_texts)
    print(f'Length of dictionary is {len(dictionary)}')
    # コーパスを作成
    if args.tfidf:
        corpus = make_corpus_tfidf(tokenized_texts, dictionary)
    else:
        corpus = make_corpus(tokenized_texts, dictionary)

    print('Preprocess is done\n')

    return tokenized_texts, dictionary, corpus

if __name__ == '__main__':
    main()
