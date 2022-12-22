import pickle

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


def elbow(data):
    print('Start elbow process...')
    ns = list(range(50, 401, 25))
    distortions = []
    for n in ns:
        print('fitting n of %d...' % n)
        km = KMeans(n_clusters=n, init='k-means++',
                    n_init=1, max_iter=300, random_state=0)
        km.fit(data)
        distortions.append(km.inertia_)

    plt.plot(ns, distortions, 'o-')
    plt.savefig('results/elbow.jpg')
    print('Saved elbow.jpg in results directory\n')

def create_and_save_kmeans_model(data, args, save_dir='model'):
    print('Creating kmeans model...')
    # n_cluster=100がいい感じのようにみえるので、100を採用
    ncluster = args.num_cluster
    km = KMeans(n_clusters=ncluster, init='k-means++',
                n_init=10, max_iter=300, random_state=0)
    y_km = km.fit_predict(data)

    with open(save_dir+'/kmeans.model', 'wb') as g:
        pickle.dump(km, g)
    print('Saved kmeans.model in model directory\n')
    return km

def plot_topic_distribution_for_clusters(y_km, data, args):
    print('Plotting topic distribution for clusters...')
    ncluster = args.num_cluster
    dic_cluster = {}
    for i in range(ncluster):
        dic_cluster[i] = np.where(y_km == i)[0]

    TH_IMPORTANCE = 0.1

    fig, axes = plt.subplots(20, 5, figsize=(24, 160))
    axes = axes.flatten()

    data_array = np.asarray(data)
    important_topics = []
    data_hist = []
    for i in range(ncluster):
        each = data_array[dic_cluster[i]].sum(axis=0)
        sorted_topics = each.argsort()[::-1]
        imp_topics = sorted_topics[each[sorted_topics]/sum(each) > TH_IMPORTANCE]
        data_hist.append(each)
        important_topics.append(imp_topics)
        axes[i].bar(np.arange(args.num_topics) + 0.5, each)
        axes[i].set_title('Cluster%d: n=%d' % (i, sum(each)))
    plt.savefig('results/topics_of_clusters.jpg')
    print('Saved topics_of_clusters.jpg in results directory\n')
