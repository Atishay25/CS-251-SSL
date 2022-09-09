#!/bin/bash

# Run the script as : ./q2a.sh guests.csv final.csv

touch temp.txt

sed 's/Timestamp/Date,Time/' $1 > temp.txt

awk -F'[,/_:]' 'BEGIN{
	num_months = split("January,February,March,April,May,June,July,August,September,October,November,December",month);
}
{ if(NR == 1) print; }
NR > 1 {	
	monthNumber = int($4)
	$4 = month[monthNumber]
	year = $3
	$3 = $5
	$5 = year
	if($6 >= 12 && $6 < 24){
		$8 = "PM"
		if($6 != 12) $6 = $6 - 12;
	}
	else {
		$8 = "AM"
		if($6 == 24) $6 = 0
	}
	printf $1 "," $2 "," $3 " " $4 " " $5","
	printf("%02d", $6)
	print ":"$7$8
}
' < temp.txt > $2

rm temp.txt

