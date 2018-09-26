#!/bin/bash
declare -a letters=("a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z")

for char in "${letters[@]}"
do
   zgrep -i -h ^$char /gpfs/gpfsfpo/preprocess_1/* | cut -f1,2,3 -d$' '| awk '
    {
        a[$1" "$2] +=$3
    }
    END{
        for(i in a) print i" "a[i]
       }' > /gpfs/gpfsfpo/preprocess_2/words_$char.csv.zip
done
