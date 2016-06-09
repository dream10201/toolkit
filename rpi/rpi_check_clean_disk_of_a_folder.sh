
while :

do 

# test a directory 
used=`du -sh /tmp/motion/  | cut -f 1 -d "M"`
echo $used 


rst=`awk -v num1=$used -v num2=2048.0 'BEGIN{print(num1>num2)?"1":"0"}'`
echo $rst 

if [ "$rst" == "1" ]; 
then echo 'going rm' >> /tmp/crond.log && /bin/rm -rf /tmp/motion/* ; 
else echo 'unrm' >> /tmp/crond.log ; 
fi

sleep 1m
done

