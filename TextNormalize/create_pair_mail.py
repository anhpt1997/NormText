file = "mail_sample.txt" 
with open(file , "r") as f:
    data = f.readlines() 
    data = [w.replace("\n","") for w in data]

result = [] 
for i in range(len(data)):
    _ = data[i].split(";")
    _ = [t.strip() for t in _]
    __ = _[1:]
    for j in range(len(__)):
        result.append(__[j] + ";" + _[0])
for i in range(len(result)):
    print(result[i])
with open("pair_mail.txt " , "w") as f:
    f.write("\n".join(result))