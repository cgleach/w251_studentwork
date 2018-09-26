#!/bin/bash

for i in {0..33}
do
   zgrep "^[a-zA-Z]*\s[a-zA-Z]" /gpfs/gpfsfpo/originals/2gram-$i.csv.zip | cut -f1,3 -d$'\t' | awk '
 {
   A[$1" "$2]++
   D[$1" "$2]+=$3
 }
 END{
   for(i in A) print i,D[i]
 }' > /gpfs/gpfsfpo/preprocess_1/bigram_$i.csv.zip

done
