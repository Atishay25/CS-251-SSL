#!/bin/bash

directory=$1
touch combinedFile.txt
touch example.txt
touch final.txt
for entry in "$directory"/*
do
    cat "$entry" >> combinedFile.txt
    echo " " >> combinedFile.txt 
done
sed "s/ /\n/g" < combinedFile.txt > example.txt
sort example.txt > final.txt
awk 'BEGIN{ sum=0 }{for(i=1;i<=NF;i++){count[$i]++}} END {for (word in count) print word, count[word] > "example.txt" }' final.txt
sort example.txt
rm example.txt
rm combinedFile.txt
rm final.txt