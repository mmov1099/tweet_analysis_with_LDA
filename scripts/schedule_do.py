import schedule
from time import sleep
from search_data import search_and_save_data
import datetime
import argparse

def task(data_dir):
    try:
        search_and_save_data(data_dir=data_dir)
    except:
        print('Error')
    print(datetime.datetime.now())

def schedule_do(args):
    time = args.time
    data_dir = args.data_dir

    #02 スケジュール登録
    schedule.every(time).seconds.do(task, data_dir=data_dir)

    # search_and_save_data()
    print(datetime.datetime.now())

    #03 イベント実行
    while True:
        schedule.run_pending()
        sleep(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--time', default=10800, type=int)
    parser.add_argument('-d', '--data_dir', default='data')
    args = parser.parse_args()

    schedule_do(args)

if __name__ == '__main__':
    main()
