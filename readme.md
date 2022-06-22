# Django file sharer

## description

这是利用校园网/园区网/局域网 172.0.0.0/192.0.0.0来进行文件分享/传输的东西 支持视频在线播放，图片在线浏览等

## run
直接运行start.bat
或python manage.py runserver 0.0.0.0:8000 --insecure

## into dev
- dist 存放html/css/js模板
- file_recevie 存放接受到文件
- file_share 存放需要分享的文件
- index Django创建的app

1. 修改html文件
2. 在File_localShare/urls.py添加路径
3. 在views 编写py包
