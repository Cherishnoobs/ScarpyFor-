import common
import re, time, random, threading
from bs4 import BeautifulSoup
from redisUtil import redisUtil

def parseList(url):
    html = common.visit(url)
    soup = BeautifulSoup(html,'html.parser')
    urls = soup.find_all(name='a',attrs={"href":re.compile(r'^http(.*)view_video(.*)')})
    for url  in urls:
        lst = url.get('href')
        redisUtil.add(lst, common.KEY)
        print(threading.current_thread().name, " insert into redis ", lst)
        

# 线程
def enter(**kwargs):
    start = kwargs["start"]
    end = kwargs["end"]
    for page in range(start, end):
        url = common.URL + "/video.php?category=rf&page=" + str(page)
        try:
            print(threading.current_thread().name, " 解析 ", page, " 页 ", url)
            parseList(url)
            time.sleep(random.randint(1, 3))
        except RuntimeError:
            print(threading.current_thread().name, " visiting page ", page, " occurs some errors ", RuntimeError.__with_traceback__)
            redisUtil.add(url, "91_error")
            continue
    # current thread has finished, log it and we can easily know it
    with open(common.LOG, "a") as f:
    	f.write("thread " + str(threading.current_thread().name) + " was finished. "+str(time.strftime('%Y-%m-%d %H:%M:%S'))+'\n')

# 运行方法
def start():
    thread_list = []
    total = common.getNumber()
    thread_total = 5 # 线程总数，默认为5，如果抓取页面小于5，则线程总数就是抓取的页面总数

    if total <= 5:
        page_size = 1
        thread_total = total
    else:
        page_size = int(total / 5) # start 5 thread to visit

    for i in range(1, thread_total + 1):
        start = (i - 1) * page_size + 1
        end = i * page_size + 1
        name = "a" + str(i)
        t = threading.Thread(target=enter, name=name, kwargs={"start":start,"end":end})
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    print("all thread over")

