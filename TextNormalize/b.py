import random


with open('pair_viettel_com_context' , 'r') as f:
	lines = f.readlines() 

pairs = [line.replace("\n","") for line in lines]
random.shuffle(pairs)
file_input = "input_mail"
file_ouput = "output_mail"
result_input , result_output = [] , [] 
for pair in pairs:
	input_sentence , output_sentence = pair.split(";")
	result_input.append(input_sentence)
	result_output.append(output_sentence)

with open(file_input , "w") as f:
	f.write("\n".join(result_input))
with open(file_ouput , "w") as f:
	f.write("\n".join(result_output))