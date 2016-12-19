
# initial_NOOBS_v1_4_0_rpi2b.sh

# NOOBS_v1_4_0 安装到 rpi 2代B 型上的初始化脚本

######################### 下面是需要用户手动执行的 #########################

# 0)
# su - root

# 1) Download 
#  https://github.com/dungeonsnd/toolkit/tree/master/rpi/initial_NOOBS_v1_4_0_rpi2b/etc__network__interfaces  To
#  /etc/network/interfaces

# 2) Download 
#  https://github.com/dungeonsnd/toolkit/tree/master/rpi/initial_NOOBS_v1_4_0_rpi2b/etc__wpa_supplicant__wpa_supplicant.conf  To
#  /etc/wpa_supplicant/wpa_supplicant.conf

# 3) 配置好网络后重启. 使用 22端口来 ssh尝试.
# reboot

# 4) 备份 sshd 的配置文件. 修改默认端口号 22 为 12222 .
cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bk
sed 's/^#Port 22/Port 12222/' /etc/ssh/sshd_config
sed 's/PermitRootLogin yes/PermitRootLogin no/'  # 禁止 root 远程登录. 允许如pi用户远程登录.
/etc/init.d/ssh restart

# 5) 在路由器上做端口映射
12222 -> 192.168.1.8:12222
8080 -> 192.168.1.8:80
443 -> 192.168.1.8:443
9090 -> 192.168.1.8:9090
12223 -> 192.168.1.9:12222
8000 -> 192.168.1.9:80


######################### 下面是需要本脚本自动执行的 #########################
# 6) 
echo 'ping sohu.com'
ping sohu.com

# 7)
cp /etc/profile /etc/profile.bk
mkdir /tmp/recycle && chmod -Rf 777 /tmp/recycle
curl -o /tmp/etc.profile https://raw.githubusercontent.com/dungeonsnd/toolkit/master/scripts_configs/config_files/linux_cfg/etc.profile  &&  cat /tmp/etc.profile >> /etc/profile

# 8)
apt-get update 

# 9)
apt-get install ufw
ufw enable
ufw status verbose
ufw status numbered
ufw default deny
ufw allow from 192.168.1.0/24
ufw allow from 58.240.26.203 proto tcp to any port 12222
ufw allow proto tcp from any to any port 80,443,9090

# 10)
apt-get install motion
cp /etc/motion/motion.conf  /etc/motion/motion.conf.bk
curl -o /etc/motion/motion.conf https://github.com/dungeonsnd/toolkit/tree/master/rpi/initial_NOOBS_v1_4_0_rpi2b/etc__motion__motion.conf
mkdir /var/run/motion/
mkdir /root/motion
motion

# 11)
apt-get install  nginx
nginx

# 12)
## 管理磁盘空间，管理连不上外网。

