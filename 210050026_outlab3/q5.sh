#!/bin/bash

# Run the script as : ./q5.sh key.txt replace.txt <num_keys>

num_keys=$3

awk -F'[- ]' -v num="$num_keys" ' NR==FNR {
    if(NR>1 && NR<(num+2)){
        replace[$1]=$2
    }
    next
}
{
    for(i=1;i<=NF;i++){
        replaced=0
        for( j in replace ){
            if(j == $i){
                replaced = 1
                printf replace[j] " ";
                break;
            }
        }
        if(replaced == 0) printf $i " ";
    }
}' $1 $2
