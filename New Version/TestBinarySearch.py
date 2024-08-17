import csv


d = open("feat.csv","r")
csv_d = csv.reader(d)
allchar =[]
feat = []
line_count = 0
for row in csv_d:
    if line_count>0:
        feat.append(row)
        allchar.append(row)
    line_count = line_count + 1
s = open("suppChar.csv","r")
csv_s = csv.reader(s)
supp = []
line_count = 0
for row in csv_s:
    if line_count>0:
        supp.append(row)
        allchar.append(row)
    line_count = line_count + 1
o = open("otherChar.csv","r")
csv_o = csv.reader(o)
other = []
line_count = 0
for row in csv_o:
    if line_count>0:
        other.append(row)
        allchar.append(row)
    line_count = line_count + 1
a = open("antagChar.csv","r")
csv_a = csv.reader(a)
antag = []
line_count = 0
for row in csv_a:
    if line_count>0:
        antag.append(row)
        allchar.append(row)
    line_count = line_count + 1

b = open("comicList.txt","w")

onlychar = []
for i in range(len(allchar)):
    onlychar.append(allchar[i][1])
    
noDup = list(dict.fromkeys(onlychar))

noDup.sort()
noDupClean = []
for i in noDup:
    if "Vol" in i or "#" in i or "http" in i:
        pass
    else:
        noDupClean.append(i)
 
def binary_search(v,L):
    i = 0
    low = 0
    high = len(L)-1
    while (low <= high):
        print(i,low,high)
        mid = (low+high)//2
        if v in L[mid] == v:
            return mid
        elif L[mid] < v:
            low = mid + 1
        else:
            high = mid -1
        i+=1
print(binary_search(noDupClean[33051],noDupClean))

