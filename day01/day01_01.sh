#!/bin/bash

count=0
calorie_count=0
calories=()
while read line
do
  calorie_count=$((calorie_count+line))
  if [ "$line" = "" ]
  then
    calories+=($calorie_count)
    count=$((count+1))
    calorie_count=0
  fi
done < input.txt

max=0
for i in ${calories[@]}
do
  if [ $i -gt $max ]
  then
    max=$i
  fi
done

echo "answer is"
echo $max
