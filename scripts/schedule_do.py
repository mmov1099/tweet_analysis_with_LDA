import schedule
from time import sleep
from search_data import search_and_save_data
import datetime

def task():
    try:
        search_and_save_data()
    except:
        print('Error')
    print(datetime.datetime.now())

def schedule_do(time:int=10800):
    #02 スケジュール登録
    schedule.every(time).seconds.do(task)

    # search_and_save_data()
    print(datetime.datetime.now())

    #03 イベント実行
    while True:
        schedule.run_pending()
        sleep(1)

def main():
    schedule_do()

if __name__ == '__main__':
    main()