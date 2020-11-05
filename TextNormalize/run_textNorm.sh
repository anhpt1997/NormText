

for index in 1 2 3 4 5 6 7 
do
python create_data.py --fileRead $index.csv --fileWriteRawText $index_raw.txt --fileWriteProcessText $index_process.txt --segmentLength 300 --pathDataRaw raw_text --pathDataProcess process_text
done