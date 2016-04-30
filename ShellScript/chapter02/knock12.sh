for i in 1 2
do
    cut -f$i $1 > ./data/col$i.txt
done

