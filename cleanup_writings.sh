#!/bin/bash

for i in writings/*; do
    cat $i | sed -e $'s/||||/\\\n/g' | sed -e $'s/\\\\\t//g' > /tmp/out
    links -dump /tmp/out | tail -n+2 > /tmp/out2
    head -2 /tmp/out > content/$i
    echo "Date: `date`" >> content/$i
    cat /tmp/out2 >> content/$i
done
    
