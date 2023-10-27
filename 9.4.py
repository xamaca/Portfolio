fname = input("Enter name of the file: ")
if len(fname) < 1 : fname = 'mbox-short.txt'
fh = open(fname)
counts = dict()
for lines in fh :
    words = lines.rstrip()
    if not words.startswith("From"):
        continue
    words = lines.split()
    #print(words)
    for word in words:
        worda = words[1]
        #print(worda)
        counts[worda] = counts.get(worda, 0) + 1
#print('Counts', counts)
bigcount = None
bigword = None
for k,v in counts.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v
print(bigword, bigcount)
        