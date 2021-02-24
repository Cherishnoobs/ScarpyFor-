# ScarpyFor?
A simple crawler to get download url

## 运行
* 安装并运行本地 Redis 用于 Url 与 DownloadUrl 更新与删除 （此处不做特别说明）
* pip install-r requests.txt 安装相应的环境包
* 某自拍网站拥有多个临时站点, 若介意翻墙, 请使用 http://807.workgreat17.live/ 等墙内站点
* python run.py 即可开始体验

## 目录结构

```
├── download
├── js          // encoding js //
├── ├── strencode.js	
├── ├── strencode2.js
├── log
├── M3U8	// M3U8 视频文件处理组件
├── ├── rename.py
├── ├── m3u8.py
├── sed
├── common
├── ├── common.py
├── ├── parseList.py
├── ├── parseSrc.py
├── ├── redisUtil.py
├── run.py
├── .gitignore
├── .flaskenv
```

## 说明
本程序会先抓取指定网站（某自拍网站）的前多少页的视频信息,再对用户所定需求进行筛选后提取响应的 DownloadUrl
若条件允许请开启 SSR/V2rayN 等工具, 以便程序的稳定读取
若有简单包报错, 但不影响程序进行, 请自行忽略

## 声明

- 本程序仅供学习参考，请在达成目的后停止使用

- 使用后任何不可知事件都与原作者无关，原作者不承担任何后果

- [MIT License](https://choosealicense.com/licenses/mit/)

使用愉快。  ：）
