import string
import re
import unicodedata

# Storing the sets of punctuation in variable result
punc = set(string.punctuation)
list_punctuations_out = ['”', '”', "›", "“", '"' ,'...', '…']
for e_punc in list_punctuations_out:
    punc.add(e_punc)

def norm_text(text):
    text = unicodedata.normalize('NFC', text)
    text = re.sub(r"òa", "oà", text)
    text = re.sub(r"óa", "oá", text)
    text = re.sub(r"ỏa", "oả", text)
    text = re.sub(r"õa", "oã", text)
    text = re.sub(r"ọa", "oạ", text)
    text = re.sub(r"òe", "oè", text)
    text = re.sub(r"óe", "oé", text)
    text = re.sub(r"ỏe", "oẻ", text)
    text = re.sub(r"õe", "oẽ", text)
    text = re.sub(r"ọe", "oẹ", text)
    text = re.sub(r"ùy", "uỳ", text)
    text = re.sub(r"úy", "uý", text)
    text = re.sub(r"ủy", "uỷ", text)
    text = re.sub(r"ũy", "uỹ", text)
    text = re.sub(r"ụy", "uỵ", text)
    text = re.sub(r"Ủy", "Uỷ", text)
    return text


with open("all-vietnam.txt" , "r", encoding='utf-8')  as f:
	vocab = f.readlines()
	vocab = [word.replace("\n","") for word in vocab]
	vocab = [norm_text(word) for word in vocab]

vocabWToI = dict(zip(vocab , range(len(vocab))))
# print(vocabWToI)
def is_float(n):
	try:
		float_n = float(n)
	except ValueError:
		return False
	else:
		return True

def is_float(n):
	try:
		float_n = float(n)
	except ValueError:
		return False
	else:
		return True

def checkSpecialWord(word):
	characters = list(word)
	for c in characters:
		if c.isdigit() == True or c in punc:
			return True
	return False

def insert_link_charatertoWord(word):
	if len(word) > 1 :
		return word
	s = ""
	flag = 0
	for i in range(len(word)):
		if word[i].isdigit() == True and flag == 0 :
			s+= word[i]
			flag = 1
		elif word[i].isdigit() == True and flag == 1 :
			s+= " "+'_'+ word[i] + " "
		elif word[i] in punc:
			if i == len(word) - 1:
				s += " "+ '_'+ word[i] + " "
			elif i== 0:
				s += " "+ word[i] + "_" + " "
			else:
				s += " "+ "_" +  word[i]+ " "
		else:
			s += word[i]
	return s.strip()

def insert_link_charatertoDocument(doc):
	words = doc.split()
	words = [w.lower() for w in words]
	inserted_link_words = [insert_link_charatertoWord(w) for w in words]
	processed_doc = " ".join(inserted_link_words)
	split_process_doc = processed_doc.split()
	for i  in range(len(split_process_doc)):
		if split_process_doc[i].isalpha() == True:
			split_process_doc[i] = processOOV(split_process_doc[i])
	return " ".join(split_process_doc)

def isBrokenAlphaBet(word):


	#word is alpha bet 
	if len(word) == 1:
		return False
	if word.isalpha() == False:
		return True
	if word in vocabWToI:
		return False
	if word.isupper() == True:
		return True
	else:
		lower_word = word.lower()
		if lower_word in vocabWToI:
			return False
		else:
			return True

def splitwordByPunctuation(word):

	if isContainPunc(word) == False:
		return [word]
	else:
		characters = list(word)
		list_index = [] 
		result = []
		if characters[0] not in punc:
			list_index = [0]
		else:
			list_index =[]		
		for i in range(len(characters)-1):
			if characters[i] in punc :
				list_index.append(i)
		if characters[-1] in punc:
			list_index.append(-1)
		for i in range(len(list_index)-1):
			if i == 0:
				if characters[0] in punc:
					result.append(word[0])
					result.append(word[list_index[i]+1 : list_index[i+1]])
				else:
					result.append(word[list_index[i] : list_index[i+1]])
			else:
				result.append(word[list_index[i]])
				result.append(word[list_index[i]+1 : list_index[i+1]])
		if list_index[-1] == -1:
			result.append(word[list_index[-1]])
		else:
			result.append(word[list_index[-1]])
			result.append(word[list_index[-1]+1:])
		final_result = []
		for i in range(len(result)):
			for token in result[i].split():
				final_result.append(token)
		return final_result

def isContainPunc(word):
	for i in range(len(word)):
		if word[i] in punc:
			return True
	return False

# def isBreakSubword(list_subword):
# 	#check whether subword should be broken
# 	result = []
# 	print(list_subword)
# 	for i in range(len(list_subword)):

# 		if len(list_subword[i]) == 1:
# 			result.append(False)
# 		else:
# 			if list_subword[i] in punc or list_subword[i].isalpha() != True:
# 				result.append(True)
# 			else:
# 				#subword is alphabet
# 				result.append(isBroken(list_subword[i]))
# 	return result

# def processSplitedWord(word):
# 	tokenSplitByPunc = splitwordByPunctuation(word)
# 	result = [handleTokenAfterSplitByPunc(subword) for subword in tokenSplitByPunc]
# 	return result

def splitByAlphaBet(list_token):
	start = 0 
	result = []
	if len(list_token) == 1:
		return list_token
	while start < len(list_token):
		for i in range(start, len(list_token)):
			if list_token[i].isalpha() == True:
				end = i 
				break
			else:
				end = len(list_token)
		if end > start :
			sub_result = list_token[start:end]
			result.append("".join(sub_result))
		if end < len(list_token):
			result.append(list_token[end])
		start = end + 1
	return result

# def isPunc(character):
# 	if character.isalpha() == False and character.isdigit() == False:
# 		return True
# 	else:
# 		return False

def insertLinkToListToken(list_token):
	# print('list token ', list_token)
	if len(list_token) == 1:
		return list_token
	else:
		for i in range(len(list_token)):
			if i == 0:
				if list_token[i] in punc:
					list_token[i] = list_token[i] + '_'
			if 0 < i and i < len(list_token) - 1 :
				if list_token[i] in punc:
					list_token[i] = "_" + list_token[i] + "_"
			if i == len(list_token) - 1 and list_token[i] in punc :
				list_token[i] = "_" + list_token[i]
			# print(i , " ", list_token)
		return list_token

def insertLinkToOOVToken(token):
	s = ""
	if len(token) == 1:
		return token
	for i in range(len(token)):
		if i == 0:
			if token[i] == '_':
				s += '_'
			else:
				if token[i+1] != "_":
					s += token[i] + " "
				else:
					s += token[i]
		if i >0 and i < len(token) - 1:
			if token[i-1] == "_" and token[i+1] == "_":
				 s+= token[i]
			elif token[i+1] == "_" :
				s += "_" + token[i]
			elif token[i-1] == "_":
				s += token[i] + " "
			else:
				s += "_" + token[i] + " "
		if i == len(token)- 1:
			if token[i] != '_' and i > 1:
				s += "_" + token[i]
			elif token[i] != "_" and i ==1 and token[i-1] != '_':
				s += "_" + token[i]
			elif token[i] != "_" and i ==1 and token[i-1] == '_':
				s += token[i]
			else:
				s += "_"
	return s

def insertLinkToListTokenFinal(list_token):
	# if len(list_token) == 1:
	# 	return list_token
	# else:
	s = []
	for i in range(len(list_token)):
		if list_token[i].isalpha() == True:
			if isBrokenAlphaBet(list_token[i]) == True:
				s.append(insertLinkToOOVToken(list_token[i]))
			else:
				s.append(list_token[i])
		else:
			s.append(insertLinkToOOVToken(list_token[i]))
	return s

def process_word(word):
	l = splitwordByPunctuation(word)
	# print("l ", l)
	# l1 = splitByAlphaBet(l)
	# print( " l1" , l1)
	l3 = insertLinkToListToken(l)
	# print("l3" ,l3)
	l4 = insertLinkToListTokenFinal(l3)
	# print(l4)
	return " ".join(l4)

def insertLinkToDoc(doc):
	words = doc.split()
	# for i in range(len(words)):
	# 	print(i ,words[i] , process_word(words[i]))
	return " ".join([process_word(w) for w in doc.split()])

def deleteLinkDoc(doc):
	result  = doc.replace(" _", "")
	result = result.replace("_ ","")
	return result

def splitDocToSentences(doc, segment_length):
	doc = norm_text(doc)
	words = doc.split()
	num_segment = len(words) // segment_length
	if num_segment * segment_length < len(words) : 
		num_segment += 1
	result = []
	for i in range(num_segment):
		start = segment_length * i 
		end = min(segment_length * (i+1) , len(words) )
		segment = words[start : end]
		result.append(segment)
	handle_begin_punc = []
	for i in range(len(result)):
		_ = splitListBeginByPunc(result[i])
		for j in range(len(_)):
			handle_begin_punc.append(_[j])
	return handle_begin_punc

def splitListBeginByPunc(list_token):
	start = 0
	for i in range(len(list_token)):
		if list_token[i][0] in punc:
			start = i+1
		else:
			break
	if start == 0 or start == len(list_token) :
		return [list_token ]
	else:
		return list_token[:start] , list_token[start:]

def concateListBeginByPunc(listOflist_token):

	if len(listOflist_token) == 1:
		return [" ".join(listOflist_token[0])]
	else:
		result = []
		i = 0 
		while i < len(listOflist_token) :
			if listOflist_token[i][0][0] in punc : 
				if i == 0 :
					result.append(listOflist_token[0] + listOflist_token[1])
					i += 2
				else :
					result[-1] = result[-1] + listOflist_token[i]
					i+=1
			else:
				result.append(listOflist_token[i])
				i+=1
		# return  [" ".join(_) for _ in result]			

		if len(result) == 1:
			return [" ".join(result[0])]
		else:
			if len(result[-1]) < 5:
				result[-2] = result[-2 ] +result[-1]
				result = result[:-1]

			# if len(result) == 1:
			# 	return [" ".join(result[0])]
			# temp = []
			# flag = 0 
			# start = 0
			# print("result " , result)
			# while start < len(result) :
			# 	if result[start][-1][-1] == '-' and start < len(result) - 1:
			# 		if flag == 1:
			# 			temp.append(result[start][1:] + [result[start+1][0]])
			# 			flag = 0
			# 		else:
			# 			temp.append(result[start] + [result[start+1][0]])

			# 		if len(result[start+1]) == 1:
			# 			start += 2
			# 		else:
			# 			start += 1
			# 			flag = 1

			# 	else:
			# 		if flag == 1:
			# 			temp.append(result[start][1:])
			# 			flag = 0
			# 		else:
			# 			temp.append(result[start])
			# 		start += 1
			# result = temp
			return [" ".join(_) for _ in result]

def handlepuncbetweenAlphaBetWord(string):
	if len(string) == 1:
		return string
	result = ""
	for i in range(len(string)):
		if i == 0:
			if string[0] == '-':
				if string[1].isalpha() == True:
					result += string[0]+ " "
				else:
					result += string[0]
			else:
				result += string[0]
		elif i > 0 and i < len(string) - 1:
			if string[i] == '-' :
				if string[i-1].isalpha() == True or string[i+1].isalpha() == True:
					if string[i-1].isalpha()==True and string[i+1].isalpha()== True:
						result += " " + string[i] + " "
					elif string[i+1].isalpha() == True and string[i-1].isalpha() == False:
						result += " " + string[i] + " "
					elif string[i+1].isalpha() == False and string[i-1].isalpha() == True:
						result += " " + string[i] + " "
				else:
					result += string[i]
			else:
				result += string[i]
		else:
			if string[-1] == '-':
				if string[-2].isalpha() == True:
					result += " " + string[-1]
				else:
					result += string[-1]
			else:
				result += string[-1]
	return 	result		

def handlepuncbetweenAlphaBetSentence(sentence):
	return " ".join([handlepuncbetweenAlphaBetWord(w) for w in sentence.split()])

def removeHyperLinks(string):
	result = string
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
	for url in urls :
		result = result.replace(url , "")
	return result

def removeMails(string):
	result = string
	mails =  re.findall(r'[\w\.-]+@[\w\.-]+', string)
	for mail in mails :
		result = result.replace(mail , "")
	return result

def segment_doc(doc , segment_length):
	doc = doc.replace(" - ","-")
	doc = doc.replace(" -","-")
	doc = doc.replace("- ","-")
	print("doc split ", doc.split())
	doc = " ".join([handleErrorUpperWord(w) for w in doc.split()])	
	_ = splitDocToSentences(doc , segment_length)
	segments = concateListBeginByPunc(_)
	result = [handlepuncbetweenAlphaBetSentence(s) for s in segments]
	return result

def existUpperCharacter(word):
	for c in word :
		if c.isupper() == True:
			return True
	return False

def lowerTextError(word):
	if existUpperCharacter(word) == True and word[0].isupper() == False:
		return word.lower()
	else:
		return word

def handleErrorUpperWord(word):
	list_segmentByPunc = splitwordByPunctuation(word)
	return "".join([lowerTextError(token) for token in list_segmentByPunc])


# doc = """ Hôm nay, chính quy-ền Tru-mp chính thức rời Hiệp định Paris về Biến đổi Khí hậu. Và trong đúng 7-7-2020 ngày nữa, chính quyền Biden sẽ tái gia nhập hiệp định", ứng viên tổng thống đảng Dân chủ Joe Biden viết trên Twitter tối 4-11."""
# print(segment_doc(doc , segment_length = 10))

print(segment_doc(".Phan uTau uHaun a a a a a aA Ba a a a a a a " , segment_length = 2)) 