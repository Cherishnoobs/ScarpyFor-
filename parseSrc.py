import time
import threading
import js2py
import common
from redisUtil import redisUtil
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
def parse(url, r, ts):
    d = pq(common.visit(url))
    src = d("#player_one script").text()
    src = src[20:-8]
    context = js2py.EvalJs()
    jscode = open("./js/strencode2.js",'r',encoding= 'utf8').read()
    context.execute(jscode)
    src = context.eval(src)

    if src is not None:
        src = pq(src)
        src = src("source").attr("src")
        html = common.visit(url)
        soup = BeautifulSoup(html,"lxml")
        con = soup.find(name="div", attrs={"class": "boxPart"}).text
        con = "".join(con.split())
        t = con.split(":")
        times = int(t[1])
        stand = int(ts)
        if times >= stand:
            print( threading.current_thread().name,  " 满足条件插入redis： ", src)
            with open("./sed/urlwithtitle.txt","a") as f:
                f.write(src)
                f.write("\n")
            redisUtil.add(src, common.KEY_SRC)
            r.lrem(common.KEY, 1, url)
        else:
            print(threading.current_thread().name,  src, "时长不够,时长：", times, "分钟")
    else:
        print(threading.current_thread().name,  url, " url的src解析为None, 插入 redis_error")
        redisUtil.add(url, common.KEY_NONE)

def enter(**kwargs):
    start = kwargs["start"]
    end = kwargs["end"]
    ts = kwargs["ts"]

    lst = redisUtil.r.lrange(common.KEY, int(start), int(end))
    for a in lst:
         print(threading.current_thread().name,  " parsing url ", a)
         parse(a, redisUtil.r, ts)
         time.sleep(0.1)
    with open(common.PARSE_LOG, "a") as f:
        f.write("thread " + threading.current_thread().name + " was finished. "+str(time.strftime('%Y-%m-%d %H:%M:%S'))+'\n')

def start():

    thread_list = []
    total = redisUtil.total(common.KEY   )
    ts = common.getTime()
    page_size = 0
    thread_total = 5

    if total <= 5:
        page_size = 1
        thread_total = total
    else:
        page_size = total / 5

    for t in range(1, thread_total + 1):
        start = (t - 1) * page_size + 1
        end = t * page_size + 1
        name = "a" + str(t)
        t = threading.Thread(target=enter, name=name, kwargs={"start":start, "end":end,"ts":ts,})
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    print("all thread over")

start()