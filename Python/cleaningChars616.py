import csv
f = open("616Char.csv","w")
d = open("AllChars.csv","r")
csv_d = csv.reader(d)
allchar =[]
line_count = 0
for row in csv_d:
    if line_count>0:
        allchar.append(row)
    line_count = line_count + 1
    
char616 = []
for i in allchar:
    if "616" in i[0]:
        char616.append(i[0])
        print(i)
        
for a in char616:
    f.write(a + "\n")
    
d.close()
f.close()