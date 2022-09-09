#!/bin/bash

awk 'BEGIN {
    for(p=97;p<123;p++){
        number[sprintf("%c",p)] = p - 87;
    }
    for(q=0;q<=9;q++){
        number[sprintf("%c",q+48)] = q;
    }
}
NR > 1 {   
    if(NR % 3 == 2){
        base1 = $1
        base2 = $2
        sum = 0
    }
    else {
        k = 1
        for(i=NF; i>0; i--){
            sum += k*number[$i];
            k = k*base1;
        }   
    }
    if(NR % 3 == 1){
            i = 0
            while(sum != 0){
                array[i] = sum % base2
                sum = int(sum/base2)
                i++
            }
            for(j=i-1;j>=0;j--){
                if(j==0) printf array[j];
                else printf array[j] " "
            }
            print '\n'
    }
} ' < $1 > $2


