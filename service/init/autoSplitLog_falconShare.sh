#!/bin/bash
# 设置日志文件存放目录，必须以/结尾
logs_dir_path="/var/local" #TODO edit this
access_filename="access"
error_filename="error"
mv ${logs_dir_path}${access_filename}.log ${logs_dir_path}${access_filename}_$(date -d "yesterday" +"%Y%m%d").log
touch ${logs_dir_path}${access_filename}.log
mv ${logs_dir_path}${error_filename}.log ${logs_dir_path}${error_filename}_$(date -d "yesterday" +"%Y%m%d").log
touch ${logs_dir_path}${error_filename}.log


