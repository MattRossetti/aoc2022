#!/bin/bash

calorie_count=0
calories=()
while read line
do
  calorie_count=$((calorie_count+line))
  if [ "$line" = "" ]
  then
    calories+=($calorie_count)
    calorie_count=0
  fi
done < input.txt

printf "%s\n" ${calories[@]} > sorted.txt
sort -nr sorted.txt > ordered.txt

top_three_sum=0
count=0
while read line
do
    top_three_sum=$((top_three_sum+line))
    count=$((count+1))
    if [ $count = 3 ]
    then
        break
    fi
done < ordered.txt
echo "answer"
echo $top_three_sum
/bin/rm sorted.txt
/bin/rm ordered.txt
