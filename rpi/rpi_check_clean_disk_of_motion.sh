#!/bin/bash

while :

do

if [ `df -h | grep /dev | awk {'print $5'} | sed -n '1,1p' | cut -f 1 -d "%"` -gt 90 ];
then echo 'going rm' >> /tmp/crond.log && /bin/rm -rf /tmp/motion/* ;
else echo 'unrm' >> /tmp/crond.log ;
fi

sleep 1m
done
