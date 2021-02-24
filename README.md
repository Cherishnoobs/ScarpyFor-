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
