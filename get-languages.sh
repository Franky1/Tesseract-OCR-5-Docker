#!/bin/bash
readarray -t languages < languages.txt
for i in "${languages[@]}"
do
  echo "Downloading ${i}.traineddata"
  wget -qO ${i}.traineddata https://github.com/tesseract-ocr/tessdata_best/blob/main/${i}.traineddata?raw=true
done
echo "Done"
