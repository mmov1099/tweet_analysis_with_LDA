from search_recent_trends import get_place_trends
from search_recent_tweets import search_recent_tweets
import glob
import json

#トレンドを取得してトレンドのワードで検索する一連の流れ
def search_and_save_data(max_results:int=100):
    get_place_trends()

    json_path = sorted(glob.glob('../data/trend/*'))
    with open(json_path[-1]) as f:
        trends = json.load(f)

    for trend in trends['trends']:
        trend['name']
        search_recent_tweets(trend['name'], max_results=max_results)

def main():
    search_and_save_data()

if __name__ == '__main__':
    main()