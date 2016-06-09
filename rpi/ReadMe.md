
喜欢的给个 star ， 谢谢。

rpi_auto_send_motion_files.py 是检测motion软件保存的图片是否达到一定的规则，达到之后就自动发送某些图片到指定邮箱。 可用于树莓派监控报警。
功能还没有测试，需要进一步测试后方可使用。


rpi_auto_send_ip_to_github.py 自动更新树莓派的内网、外网IP地址到 自己的github上。使用方法如下，
1) 创建一个自己的repos，用于上传IP地址。并 clone 到树莓派上。
2） 在树莓派上的自己的 repos 目录下执行 nohup python /path/rpi_auto_send_ip_to_github.py number &
其中， path是rpi_auto_send_ip_to_github.py脚本所在目录，number是用于在自己外网IP地址每个数字上加一个值，这个值只有你自己知道，防止别人看到你的GITHUB后用你的IP做一些破坏。
3) 到你的github页面，看到ip.txt的内容即是你的树莓派内外网IP，注意要减去你输入的number.


