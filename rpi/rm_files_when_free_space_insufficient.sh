#!/bin/bash


#
# 每小时检测磁盘空间，大于给定值时删除指定的文件夹.
# 
# crontab -e
# 0 * * * * sh /root/rm_files_when_free_space_insufficient.sh
#

watermark=80%  # 磁盘已用空间大于此阀值时，开始删除指定文件

folderWillRemove=`/bin/ls -l -ltr /root/motion_backup/ | grep -v 'total' | awk {'print $9'} | head -n 1`


used=`df -h | grep rootfs | awk {'print $5'}` && echo $used

if test `echo  ${used%%%}'>'${watermark%%%} |bc -l` -eq 1
  then
  echo "$used>$watermark"
  /bin/rm -rf /root/motion_backup/$folderWillRemove
else
  echo "$used<=$watermark"
fi


