#!/bin/bash
COUNTER=0
FILE_PATH='./static/img/clothes/'
for file in ./static/img/clothes/*; do
	mv "$file" "$FILE_PATH$COUNTER.png"
	let COUNTER=COUNTER+1
done
