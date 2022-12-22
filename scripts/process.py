import argparse
import pickle

import gensim
import preprocess
from analyze_models import load_data
from kmeans import *
from lda import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-nt','--num_topics', default=50)
    parser.add_argument('-p', '--preprocess', help='run preprocess', action='store_true')
    parser.add_argument('-t', '--train', help='run training LDA model', action='store_true')
    parser.add_argument('-tf', '--tfidf', help='use tfidf corpus', action='store_true')
    parser.add_argument('-f', '--feature', help='compress tweets and save features', action='store_true')
    parser.add_argument('-e', '--elbow', help='run elbow', action='store_true')
    parser.add_argument('-nc','--num_cluster', default=100)
    parser.add_argument('-k', '--kmeans', help='run create_and_save_kmeans_model()', action='store_true')
    args = parser.parse_args()

    if args.preprocess:
        tokenized_texts, dictionary, corpus = preprocess.main(args)
    else:
        tokenized_texts, dictionary, corpus = load_data()

    if args.train:
        lda = create_and_save_model(corpus, dictionary, args.num_topics)
    else:
        lda = gensim.models.ldamulticore.LdaMulticore.load('model/lda.model')

    show_results(lda)

    if args.feature:
        data = compress_tweets_and_save_features(corpus, lda)
    else:
        with open('model/features.dump', mode='rb') as f:
            data = pickle.load(f)
    if args.elbow:
        elbow(data)

    if args.kmeans:
        km = create_and_save_kmeans_model(data, args)
        y_km = km.fit_predict(data)
        plot_topic_distribution_for_clusters(y_km, data, args)
    else:
        with open("model/kmeans.model", "rb") as f:
            km = pickle.load(f)


if __name__ == '__main__':
    main()
