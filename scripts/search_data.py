from search_recent_trends import get_place_trends
from search_recent_tweets import search_recent_tweets
import glob
import json

#トレンドを取得してトレンドのワードで検索する一連の流れ
def search_and_save_data(max_results:int=100, data_dir='data'):
    get_place_trends(data_dir=data_dir)

    json_path = sorted(glob.glob(data_dir+'/trend/*'))
    with open(json_path[-1]) as f:
        trends = json.load(f)

    for trend in trends['trends']:
        search_recent_tweets(trend['name'], max_results=max_results, data_dir=data_dir)

def main():
    search_and_save_data()

if __name__ == '__main__':
    main()
