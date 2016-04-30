## sed command: from  \t to ' '(one space)
#sed -e 's/	/ /g' $1

## tr command
#cat $1 | tr '\t' ' ' 

##expand command
expand -t 1 $1
