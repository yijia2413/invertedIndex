#!/bin/bash
#awk -F' ' '{print $NF}' a.txt
#sed -i 's/#/#/g' a.txt
while read i;do
	num=`echo $i | awk -F' ' '{print $NF}' -`
	s=`expr "$i" : '\(.*\) .*'` 
	echo $s | sed -e "s/#/#$num\n/g"
done < Result.txt
