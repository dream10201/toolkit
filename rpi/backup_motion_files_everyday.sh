#!/bin/bash

# 每天23：55分开始备份 motion 的文件.
# crontab -e
# 55 23 * * * sh /root/backup_motion_files_everyday.sh
#

d=`date "+%Y%m%d"` ; echo $d ; mkdir /root/motion_backup/$d ; mv /root/motion/*  /root/motion_backup/$d/

