import csv
f = open("616Char.csv","r")
d = open("otherChar.csv","r")
c = open("otherClean616.csv","w")
#reading in 616 chars
csv_f = csv.reader(f)
char616 =[]
line_count = 0
for row in csv_f:
    if line_count>0:
        char616.append(row[0])
    line_count = line_count + 1
#reading in featured chars
csv_d = csv.reader(d)
allchar =[]
line_count = 0
for row in csv_d:
    if line_count>0:
        allchar.append(row)
    line_count = line_count + 1
    

for i in allchar:
    if i[1] in char616:
        c.write(i[0] +","+i[1]+ "\n")
        if int(i[0])%1000==0:
            print(i)
        
d.close()
f.close()
c.close()
        
