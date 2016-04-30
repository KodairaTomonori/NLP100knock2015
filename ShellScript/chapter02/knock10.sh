# tutorial: unix command `wc'
num=`wc -l $1 | cut -d' ' -f7` 
echo $num
