# coding=utf-8
import requests
import os
import re
import time
import random
import threading
import progressbar
import requests.packages.urllib3
import sys
import base64
from bs4 import BeautifulSoup
import js2py
import youtube_dl
import signal
from tqdm import tqdm
from urllib.parse import urlparse


def main():
    file_path = os.getcwd() + "\\" + 'Downloads'
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间
        dir_list = sorted(dir_list,key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        # print(dir_list)
        with open("../demo/urlwithtitle.txt", "r") as f:  # 打开文件
            index = 0
            for line in f.readlines():
                name = line.split("----")[1].replace('\n','') + ".mp4"
                os.rename(os.path.join(file_path,dir_list[index]),os.path.join(file_path,name))
                index += 1
        return dir_list


if __name__ == '__main__':
    main()