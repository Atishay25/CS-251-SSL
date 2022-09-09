#!/bin/bash

textfile=$1
sed 's/.$/\:)/g' <$textfile > temp.txt
sed 's/\./\$/g' <temp.txt
rm temp.txt
