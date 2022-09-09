#!/bin/bash

# Please provide 'images' directory as command line arguement
# Rum the script as : ./q2b.sh images
# I implemented in this way because this was told in piazza
# however in outlab doc, nothing was mentioned about it

directory="images"
if [ $# == 1 ];
then
    directory=$1
else
    directory="images"
fi

cd "$directory" 
folder=*

for file in $folder;
do
    new_name=$(echo "$file" | sed -e 's/^img_\([0-9]*\)-\([0-9]*\)-\([0-9]*\)/\2-\3-20\1/p')
    mv "$file" "$new_name"
done
