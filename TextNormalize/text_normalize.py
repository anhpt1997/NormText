num = ['một','hai','ba','bốn','năm','sáu','bảy','tám','chín','mười','lăm','linh','tư','mốt']
suffix = ['mươi', 'trăm','nghìn','triệu','tỷ']
value = [10 , 100 , 1000, 1000000,1000000000]
a = 'linh'

so = ['1', '2' ,'3' ,'4', '5' ,'6' ,'7','8', '9','10','5','0','4','1']
decade = dict(zip(suffix , value))
d = dict(zip(num , so))
b = ['năm','nghìn','một','trăm','hai','mươi','ba']
b = ['một','trăm','linh', 'sáu']
print("dsdsds" , b[0:])
def convert_subInput_toStack(b):
	result = []
	for i in range(len(b)):
		if b[i] in d.keys():
			result.append(d[b[i]])
		else:
			result.append(b[i])
	return result

queue = []
def compute_sum(input):
	result = 0 
	for i in range(len(input)):
		if input[i].isdigit() == True:
			result += int( input[i])
	return result

def compute_sum_sub_input(input):
	result = 0 
	decade = input[-1]
	for i in range(len(input)-1):
		if input[i].isdigit() == True:
			result += int( input[i])
	return result

def find_index_split(input):
	split_index = [0]
	for i in range(len(input)):
		if input[i] in suffix:
			split_index.append(i + 1)
	split_index.append(-1)
	return split_index

def convertToNumber(list_input):

	list_index_split = find_index_split(list_input)
	print('list index ', list_index_split)
	sub_input = []
	for  i in range(len(list_index_split) - 1 ):
		# if i < len(list_index_split) - 1 and i > 0:
		# 	sub_input.append(list_input[list_index_split[i]+1:list_index_split[i+1]+1])
		if list_index_split[-1] != -1 :
			sub_input.append(list_input[list_index_split[i]:list_index_split[i+1]])
		else:
			sub_input.append(list_input[list_index_split[i]:])

	# sub input : [['năm', 'nghìn'], ['một', 'trăm'], ['hai', 'mươi'], ['ba']]
	print('sub input ' , sub_input)
	sub_result = [compute_sum(convert_subInput_toStack(sub)) for sub in sub_input]
	return sum(sub_result)

print(b)
# print(compute_sum(convert_subInput_toStack(b)))
print(convertToNumber(b))

