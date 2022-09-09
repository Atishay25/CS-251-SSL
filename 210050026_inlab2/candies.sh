#! /bin/bash  

teacher=0

first=1

persons=$1

for((i=0; i<persons; i++))
do
        echo -n "$teacher "

        nextstudent=$(($teacher + $first))

        teacher=$first

        first=$nextstudent
done

echo

