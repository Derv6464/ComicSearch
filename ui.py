import csv
f = open("AllLinks.csv","r")
dataIn = f.read()
list1 = dataIn.split("\n")

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
from tkinter import *
root = Tk()
root.title("tetsteftet")
root.geometry("800x500")

def update(data):
    my_list.delete(0,END)

    for item in data:
        my_list.insert(END,item)

def fillout(e):
    my_entry.delete(0,END)
    my_entry.insert(0,my_list.get(ANCHOR))
    
def check(e):
    typed = my_entry.get()
    if typed == '':
        data = noDup
        #my_list.grid(row=2,column=0)
    else:
        data = []
        for item in noDup:
            if typed.lower() in item.lower():
                data.append(item)
    update(data)
    
def getInfo():
    global y,i
    charIn = my_entry.get()
    #my_list.grid_forget()
    print(charIn)
    allEnt.append(charIn)
    lab = Label(root, text=my_entry.get())
    lab.grid(row=y,column=0)
    selectOp = OptionMenu(root,allSel[i],*selectOption)
    selectOp.grid(row=y,column=1)
    allFeat.append(selectOp)
    y+=1
    i+=1
    
def addSel():
    selectOp = OptionMenu(root,clicked,*selectOption)
    selectOp.grid(row=y,column=x)
    allFeat.append(selectOp)
    x+=1

def getSelOp():
    for i in enumerate(allFeat):
        print(allSel[i].get())
    
allEnt = []
y = 5
x = 2
i=0
allFeat = []
allSupp = []
allOther = []
allAntag = []
clicked = StringVar()
clicked.set("how they appear")
allSel = [clicked1,clicked2,clicked3,clicked4,clicked5,clicked6,clicked7,clicked8,clicked9,clicked10,clicked11,clicked12,clicked13,clicked14,clicked15,clicked16,clicked17,clicked18,clicked19,clicked20]
selAdd = []

    
my_label = Label(root, text="search character")
my_label.grid(row=0,column=0)

my_label2 = Label(root, text="characters you added:")
my_label2.grid(row=4,column=0)

my_entry = Entry(root, width=50)
my_entry.grid(row=1,column=0,padx=10)

my_list = Listbox(root, width=50)
my_list.grid(row=2,column=0,padx=10)


selectOption = ["Featured","Supporting","Other","Antagonist","All"]
selectOp = OptionMenu(root,clicked,*selectOption)

selectOp.grid(row=5,column=1)
addCharButton = Button(root,text="add character",command=getInfo)
addCharButton.grid(row=1,column=1)

addSelectOp = Button(root,text="add selection",command=addSel)
addSelectOp.grid(row=5,column=2)

SearchButton  = Button(root,text="Search",command=getSelOp)
SearchButton.grid(row=y+1)

update(noDup)
my_list.bind("<<ListboxSelect>>", fillout)
my_entry.bind("<KeyRelease>",check)



root.mainloop()

