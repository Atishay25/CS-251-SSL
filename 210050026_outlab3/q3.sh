#!/bin/bash

flag=$2
arguements=$#

if [[ $arguements == 1 ]];
then
sed -e 's/ //g' -e '/^$/d' $1 | awk '
    BEGIN{ char = 0;}
    {   
        char += length($1)  
    }
    END{ printf char " characters,"  }'

awk 'BEGIN{ words = 0;}
    {
        words += NF;
    }
    END{ printf " " words " words," }' $1

awk 'END { printf " " NR " lines,"; }' $1

sed '/^$/N;/^\n$/D' $1 | awk '!NF {para += 1} END {
    if(NF == 0) print " " para " paragraphs"
    else print " " para+1 " paragraphs"
    }'

fi


if [[ $flag == "-chars" ]];
then
sed -e 's/ //g' -e '/^$/d' $1 | awk '
    BEGIN{ char = 0; }
    {   
        char += length($1)
    }
    END{ print char " characters"; }'    
fi

if [[ $flag == "-words" ]];
then
awk 'BEGIN{ words = 0; }
    {
        words += NF;
    }
    END{ print words " words"; }' $1
fi

if [[ $flag == "-lines" ]];
then
awk 'END { print NR " lines"}' $1
fi

if [[ $flag == "-paras" ]];
then
sed '/^$/N;/^\n$/D' $1 | awk '!NF {para += 1} END {
    if(NF == 0) print para " paragraphs"
    else print para+1 " paragraphs"
    }'
fi