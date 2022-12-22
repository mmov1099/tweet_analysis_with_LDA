import pickle

import gensim


def show_results(lda):
    import pprint
    print('Important 10 words of all topics')
    # 全topic(100個)に対して、上位10個の重要なwordをshow
    pprint.pprint(lda.show_topics(num_topics=-1, num_words=10))
    print('')

def create_and_save_model(corpus, dictionary, num_topics, save_dir='model'):
    print('Creating LDA model...')
    # LDAモデルの構築
    # lda = gensim.models.ldamulticore.LdaMulticore(corpus=corpus, id2word=dictionary,
    #                                            num_topics=num_topics, workers=3, minimum_probability=0.001,
    #                                            passes=20, chunksize=10000)
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                    num_topics=num_topics,
                                    id2word=dictionary,
                                    random_state=1)
    lda.save(save_dir+'/lda.model')

    return lda

def compress_tweets_and_save_features(corpus, lda, save_dir='model'):
    print('Compressing tweets...')
    # all data
    vs = lda[corpus]
    num_topics = len(lda.show_topics(num_topics=-1))

    data = []
    for v in vs:
        each = [0.] * num_topics
        for i, d in v:
            each[i] = d
        data.append(each)
    #     break
    with open(save_dir+'/features.dump', 'wb') as g:
        pickle.dump(data, g)
    print('Saved features in model directory\n')

    return data
