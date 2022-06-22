# myvue

实际部署时请先修改/src/pages/store.ts中path_nginx_staitc

## TODO
1. 尽量缩小到1mb以内

## 请求表
```
vue_store.frew + 'jsPost/auth/login' 
vue_store.frew + 'jsGet/potato/clientip'
vue_store.frew + 'jsGet/share/filetree'
vue_store.frew + 'jsStream/upload/{parm_status}'
```

## 魔改配置
1. 修改html输出目录：vue.config.js > chainWebpack()  
2. 修改build后src、href根目录：vue.config.js > publicPath  
3. 修改浏览器标签页名称：package.json > "name"
4. 修改Eslint语法：.eslintrc.js

***
### Project setup>>>  ```npm install```
### Compiles and hot-reloads for development>>>```npm run serve```
### Compiles and minifies for production>>>```npm run build```
### Lints and fixes files>>>```npm run lint```
### Customize configuration  See [Configuration Reference](https://cli.vuejs.org/config/).
