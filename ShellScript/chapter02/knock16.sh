num=`wc -l $1 | cut -d' ' -f7` 
one=`expr $num / $2`

split -a 1 -l $one $1 data/split_
