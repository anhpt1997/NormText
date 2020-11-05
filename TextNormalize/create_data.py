import sys, os , argparse
import pandas as pd 
from process import *

parser=argparse.ArgumentParser(description='xxx')
parser.add_argument('--fileRead',     type=str, required= True)
parser.add_argument('--fileWriteRawText' , type=str, required=True)
parser.add_argument('--fileWriteProcessText', type=str , required=True)
parser.add_argument('--segmentLength' , type=int , required= True)
parser.add_argument('--pathDataRaw', type=str , required=True)
parser.add_argument('--pathDataProcess', type=str , required=True)
args=parser.parse_args()

file_read = args.fileRead
file_writeRaw = args.fileWriteRawText
segment_length = args.segmentLength
fileWriteProcessText = args.fileWriteProcessText
path_data_raw = args.pathDataRaw
path_data_process = args.pathDataProcess
import os 
if os.path.exists(path_data_raw) == False:
	os.mkdir(path_data_raw)
if os.path.exists(path_data_process) == False:
	os.mkdir(path_data_process)

data = pd.read_csv(file_read , delimiter = ";")

# print(data.)
column = data['content'].values.tolist()
if type(column) != list:
	column = [column]
column = [str(row ) for row in column]
result = []
for i , c  in enumerate(column):
	segments = splitDocToSentences(c , segment_length)
	segments = concateListBeginByPunc(segments)
	for segment in segments :
		result.append(segment)
	
# process_doc = []
# print("result")
# for i in range(len(result)):
# 	# process_doc.append(insertLinkToDoc(result[i]))
# 	print(result[i])

for i in result:
	print(i)

# with open(path_data_raw+"/"+file_writeRaw , "w" , encoding='utf-8') as f:
# 	result = "\n".join(result)
# 	f.write(result)

# with open(path_data_process+"/"+fileWriteProcessText , "w" , encoding='utf-8') as f:
# 	process_doc = "\n".join(process_doc)
# 	f.write(process_doc)
