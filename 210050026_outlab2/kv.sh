#! /bin/bash

now="$(date +'%d/%m/%Y')"
time=$(date +"%T")
name=$2
underScore="_"
Name="$name$underScore"
id=$3

function storeInfo(){
    echo ${name}_${now}-${time} ${id} >> store.txt
}

function displayInfo(){
    echo Name OrderID
    cat store.txt
}

function getOrderID(){
    echo "OrderID's found are:"
    number=$(tr ' ' '\n' < store.txt | grep $Name | wc -l)
    found=$(grep $Name store.txt)
    j=0
    for i in $found
    do
        k=2
        if [ $(expr $j % 2) != "0" ]; then
            echo $i
        fi 
        j=$(($j+1))
    done
    echo "$name" ordered "$number" times
}

"$@"