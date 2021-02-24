import os
from re import T
import re
import requests,random
from requests.api import get
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

cookies = requests.cookies.RequestsCookieJar()
cookies.set("language", "cn_CN", domain=".p06.rocks", path="/")

# 91 的临时站点
# URL = "http://91porn.com/"
# URL = "http://91.91p17.space/"
# URL = "https://p06.rocks"
# URL = "http://807.workgreat17.live/"

URL = "http://807.workgreat17.live/"
KEY = "91"
KEY_SRC = "91_src"
KEY_NONE = "91_none"
LOG = './log/spider.log'
TORRENT = "./sed/"
PARSE_LOG = "./log/parse.log"
DOWNLOAD = './download/'
path = '/'.join(LOG.split("/")[0:-1])

if not os.path.exists(TORRENT):
    os.makedirs(TORRENT)

if not os.path.exists(path):
    os.makedirs(path)

if not os.path.exists(DOWNLOAD):
    os.makedirs(DOWNLOAD)

# 参数设置

def getNumber():
    while True:
        num = input("请输入你想抓取的总页数:")
        try:
            page = int(num)
            return page
        except:
            print("抱歉，您输入的不是有效的数字, 请重新输入.")
            continue


def getTime():
    while True:
        num = input("请输入想获取的时长(分钟):")
        try:
            time = int(num)
            return time
        except:
            print("抱歉，您输入的不是有效的数字, 请重新输入.")
            continue



def visit(url):
    #   构造随机ip作为请求头访问目标站点
    randomIP = str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))
    retries = Retry(total=5,backoff_factor=10, status_forcelist=[500,502,503,504])
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'X-Forwarded-For': randomIP
    }

    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=retries))
    html = s.get(url, headers=headers, cookies=cookies, stream=True).content
    print("visit success!")
    return html