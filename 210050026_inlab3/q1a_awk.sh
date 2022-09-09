#!/bin/bash

directory=$1
touch combinedFile.txt
for entry in "$directory"/*
do
    cat "$entry" >> combinedFile.txt
    echo " " >> combinedFile.txt 
done
awk 'BEGIN{ sum=0 }{for(i=1;i<=NF;i++){count[$i]++}} END {for (word in count){ if(count[word]>=1){sum++}} print sum }' combinedFile.txt
rm combinedFile.txt