#!/bin/zsh

for i in $(seq 0 20);do
    python client-test03.py $i &
done
