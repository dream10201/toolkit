#!/bin/bash


# chmod +x reboot_when_network_failure.sh
# nohup ./reboot_when_network_failure.sh &

function network_check()
{
    local network_failure_if_eq_0=`ping 192.168.1.1 -c 5 | grep "min/avg/max" -c`
    echo $network_failure_if_eq_0
}

while :
do
    # first-time checking.
    if [ $(network_check) -eq 0 ] ; then
        echo 'reset at '`date`  /tmp/reboot_when_network_failure.log && /etc/init.d/networking restart && ifdown wlan0 && ifup wlan0
        sleep 2m
        
        # second-time checking.
        if [ $(network_check) -eq 0 ] ; then
            echo 'reset --force at '`date`  /tmp/reboot_when_network_failure.log && /etc/init.d/networking restart && ifdown --force wlan0 && ifup --force wlan0
            sleep 5m
        
            # third-time checking.
            if [ $(network_check) -eq 0 ] ; then
                    echo 'reboot at '`date` >> /tmp/reboot_when_network_failure.log # && reboot    # Donot reboot temporarily, bcz my rpi may fail to restart for unkown reason.
            fi  
        fi
    else
         echo 'unset at '`date` >> /tmp/reboot_when_network_failure.log
    fi

    sleep 5m
    
done

