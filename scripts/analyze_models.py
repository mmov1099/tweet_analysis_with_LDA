import pickle

import gensim
import matplotlib.pyplot as plt
import numpy as np
from preprocess import json2texts, tokenize
from tqdm import tqdm


def load_data(dir='model'):
    # 基本となるデータをload
    print('Loading tokenized_texts')
    with open(dir+"/tokenized_texts.pkl", "rb") as f:
        tokenized_texts = pickle.load(f)

    # 辞書のテキストファイルをload
    print('Loading a dictionary')
    dictionary = gensim.corpora.Dictionary.load_from_text(dir+'/wordid.txt')

    # コーパスのファイルをload
    print('Loading a copus')
    with open(dir+'/corpus.pkl', mode='rb') as f:
        corpus = pickle.load(f)
    print('Completed loading\n')

    return tokenized_texts, dictionary, corpus


class AnalyzerModels():
    def __init__(self, start=2, limit=100, step=1) -> None:
        #Metrics for Topic Models
        self.start = start
        self.limit = limit
        self.step = step

        self.coherence_vals = []
        self.perplexity_vals = []

    def analyze(self, texts_words, dictionary, corpus):
        for n_topic in range(self.start, self.limit, self.step):
            print(f'Building model of {n_topic} topics')
            lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=n_topic, random_state=0)
            print('Calculating perplexity value')
            self.perplexity_vals.append(np.exp2(-lda_model.log_perplexity(corpus)))
            print('Building coherence model')
            coherence_model_lda = gensim.models.CoherenceModel(model=lda_model, texts=texts_words.values(), dictionary=dictionary, coherence='c_v')
            print('Calculating coherence')
            self.coherence_vals.append(coherence_model_lda.get_coherence())

    def visualize(self, save_dir='model'):
        print('Visualizing results')
        # evaluation
        x = range(self.start, self.limit, self.step)

        fig, ax1 = plt.subplots(figsize=(12,5))

        # coherence
        c1 = 'darkturquoise'
        ax1.plot(x, self.coherence_vals, 'o-', color=c1)
        ax1.set_xlabel('Num Topics')
        ax1.set_ylabel('Coherence', color=c1); ax1.tick_params('y', colors=c1)

        # perplexity
        c2 = 'slategray'
        ax2 = ax1.twinx()
        ax2.plot(x, self.perplexity_vals, 'o-', color=c2)
        ax2.set_ylabel('Perplexity', color=c2); ax2.tick_params('y', colors=c2)

        # Vis
        ax1.set_xticks(x)
        fig.tight_layout()

        # save as png
        print('Saving a figure')
        plt.savefig(save_dir+'/metrics.png')

def main():
    print('Loading data')
    texts_words, dictionary, corpus = load_data()

    analyzer = AnalyzerModels()
    print('Analysis starts')
    analyzer.analyze(texts_words, dictionary, corpus)
    analyzer.visualize()
    print('All done')

if __name__ == '__main__':
    main()
