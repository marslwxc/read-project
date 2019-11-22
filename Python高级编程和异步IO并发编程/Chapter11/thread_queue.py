# 线程间的通信
# 1.相乘通信方式——共享变量

import time
import threading
from Chapter11 import variables


def get_detail_html():
    #爬取文章详情页
    # global detail_url_list
    detail_url_list = variables.detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            # for url in detail_url_list:
            print("get detail html started")
            time.sleep(4)
            print('get detail html end')

def get_detail_url():
    # 爬取文章列表页
    # global detail_url_list
    detail_url_list = variables.detail_url_list
    while True:
        print("get detail url started") 
        time.sleep(2)
        for i in range(20):
            detail_url_list.append('http://projectsedu.com/{id}'.format(id=i))
        print('get detail url end')




if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_detail_url)
    for _ in range(10):
        html_thread = threading.Thread(target=get_detail_html)
        html_thread.start()
    start_time = time.time()
    thread_detail_url.start()
    print(time.time() - start_time)