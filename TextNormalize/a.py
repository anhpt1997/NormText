def create_doc_content_gmail(tail_gmail , list_context, list_pair_gmail):
	result = []
	if tail_gmail == "@gmail.com":
		tail_doc = "a còng gờ mêu chấm com"
		for i in range(len(list_pair_gmail) // 2):
			pair = list_pair_gmail[i].split(";")
			doc , mail = pair[0] , pair[1] 
			for context in list_context:
				result.append(";".join([ " ".join([context , doc, tail_doc])  , " ".join([context , mail]) ]))

		for i in range(len(list_pair_gmail)// 2 , len(list_pair_gmail)):
			pair = list_pair_gmail[i].split(";")
			doc , mail = pair[0] , pair[1] 
			for context in list_context:
				result.append(";".join([ " ".join([doc, tail_doc])  , " ".join([mail]) ]))			
		
		with open('pair_gmail_com_context', "w") as f:
			f.write("\n".join(result))
	elif tail_gmail == "@viettel.com.vn":
		tail_doc = "a còng việt theo chấm com chấm vi en"
		for i in range(len(list_pair_gmail)):
			pair = list_pair_gmail[i].split(";")
			doc , mail = pair[0] , pair[1] 
			for context in list_context:
				result.append(";".join([ " ".join([context , doc, tail_doc])  , " ".join([context , mail]) ]))
		with open('pair_viettel_com_context', "w") as f:
			f.write("\n".join(result))
			  
context = ["vui lòng gửi thư đến hòm thư" , "vui lòng gửi thư đến địa chỉ" ,
 "mọi chi tiết xin liên hệ",  "hòm thư" , 
 "liên hệ đến địa chỉ " , "mọi ý kiến đóng góp, xin liên hệ " , " phản hồi về hòm thư" , "phản hồi theo đường dẫn", "gửi thư đến", " gửi thư tới"]

with open("final_pair_mail_2.txt", "r") as f:
	data = f.readlines()
	data = [w.replace("\n","") for w in data]

create_doc_content_gmail(tail_gmail = "@viettel.com.vn" , list_context = context , list_pair_gmail = data)
# # with open("all_pair_context_mail.txt" , "r") as f:
# # 	lines = f.readlines()
# # import random
# # choices = random.choices(lines , k = 5)
# # for c in choices:
# # 	print(c)

# with open("pair_mail_2.txt", "r") as f:
# 	lines = f.readlines()
# final_result = []
# for line in lines:
# 	temp = line.split(";")
# 	if " đê " in temp[0] or " đê" in temp[0] or "đê " in temp[0]:
# 		_ = temp[0].replace(" đê "," dê ")
# 		_ = _.replace(" đê"," dê")
# 		_ = _.replace("đê ","dê ")
# 		final_result.append(";".join([ _ ,temp[1]]))
# 		final_result.append(line)
# 	else:
# 		final_result.append(line)
# with open("final_pair_mail_2.txt" , "w") as f_w:
# 	f_w.write("".join(final_result))