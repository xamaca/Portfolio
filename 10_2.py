fname = input("Enter file name here: ")
if len(fname) < 1 : fname = 'mbox-short.txt'
fh = open(fname)
dic = dict()
for lines in fh:
    words = lines.rstrip()
    if not words.startswith('From'):
        continue
   # print(words)
    result = words.split()
    try :
        new = result[5]
    except :
        continue
    new = new.split(':')
    new = new[0]
    #for w in new :
    dic[new] = dic.get(new,0) + 1
#print(dic)

temp =list()
for k,v in dic.items() :
    #print(k,v)
    newt = (k,v)
    temp.append(newt)
    
temp = sorted(temp)
print('sorted', temp)

for k,v in temp:
    print(k,v)
    

    













