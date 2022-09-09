#!/bin/bash

pattern="#@$"       # pattern variable stores special patterns
word="word"         # word variable stores the recurring words

declare -a filetext

file=$1             # file is the text file
N=$2                # N is the number of occurences
grep -oE '[\*\&^%\#@\!\$]{3}' $file > file1         # taking all the special characters into a dummy file 'file1'
tag=$( tail -1 file1 )                              # tag is the last special character

j=0
while read line; do             # reading from the text file and storing all the words in an array 'filetext'
    for words in $line; do
            filetext[$j]+="$words"
            j=$(($j+1))
    done
done <q2-sample.txt

j=0
for (( i=0; i < ${#filetext[@]}; i++ )); do     # finding the index of first recurring word
    if [ ${filetext[i]} = '#@$' ]; then
        word=${filetext[i+1]}
        j=$(($i+1))
        break
    fi
done

count=0
for (( i=j; i < ${#filetext[@]}-2; i++ )); do       # looping throgh the array for finding last recurring word and pattern
    if [[ ${filetext[i]} =~ "$word" ]] && [[ "${filetext[i+1]}" =~ [\!@\#\$%\^\&\*]{3}$ ]] && [[ "${filetext[i+2]}" =~ [a-zA-Z]+$ ]]; then
        word=${filetext[i+2]}
        pattern=${filetext[i+1]}
        count=$(($count+1))
        if [[ $pattern =~ "$tag" ]] || [[ $count =~ $N ]]; then
            word=${filetext[i]}
            break
        fi
    fi
done

echo "Last Word found: $word"
echo "Last Pattern found: $pattern"

rm file1            # removing the temporary file created