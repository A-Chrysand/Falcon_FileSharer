# falcon_fileSharer

### 初始化服务器:

```bash
cd 到Falcon_FileSharer/
bash ./service/init/init.sh
```

### 开启服务器：

首先确认您是否需要使用Nginx、Apache等软件提供静态文件服务。  
如果需要，则

1. 将service_conf.py中nginx_static修改为你的服务器url，并且下载前端源代码重新编译
2. 将service_conf.py中standalone_mode改成False

如果不需要，则
1. 将service_conf.py中standalone_mode改成False  


   

