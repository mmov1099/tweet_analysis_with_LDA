import gensim
import argparse
from analyze_models import load_data

def create_and_save_model(corpus, dictionary, num_topics=100, save_dir='model'):
    # LDAモデルの構築
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                        num_topics=num_topics,
                                        id2word=dictionary,
                                        random_state=1)
    lda.save(save_dir+'/test.model')

    return lda

def show_results(lda):
    print('Important 10 words of all topics')
    # 全topic(100個)に対して、上位10個の重要なwordをshow
    lda.show_topics(num_topics=-1, num_words=10)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--num_topics', default=100)
    args = parser.parse_args()

    tokenized_texts, dictionary, corpus = load_data()
    lda = create_and_save_model(corpus, dictionary, args.num_topics)

    show_results(lda)

if __name__ == '__main__':
    main()
