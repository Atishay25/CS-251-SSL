#!/bin/bash

inputfile=$1

awk '{ function changeBase(arr,n,line){
    prevbase = 8 + 2*(line%3)
    for(i=n-1;i>=0,i++){
        
    }
}}' $inputfile
