#this is for allAlias,curAlias,nameChar
import csv
f = open("nameChar.csv","r")
l = open("allAlias.csv","r")
g = open("curAlias.csv","r")
sql = open("Test.txt",  "w")
#dataIn = f.read()
#char616 = dataIn.split("\n")

name=[]
csv_d = csv.reader(f)
line_count = 0
for row in csv_d:
    if line_count>0:
        name.append(row)
    line_count = line_count + 1

        
sql.write("DROP TABLE IF EXISTS charName; \n\n")
sql.write("CREATE TABLE IF NOT EXISTS charName \n \t (char_link TEXT, \n \t char_name TEXT); \n\n")
sql.write("INSERT INTO charName \n \t (char_link, \n \t char_name) \n VALUES \n")
for i in name:
    if i == name[-1]:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "); \n" )
        print(i)
    else:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "), \n" ) # comma
    if name.index(i)%1000 ==0:
        print(name.index(i))
 # semicolon
print("File created successfully")


curAlias=[]
csv_g = csv.reader(g)
line_count = 0
for row in csv_g:
    if line_count>0:
        curAlias.append(row)
    line_count = line_count + 1

        
sql.write("DROP TABLE IF EXISTS charCurAlias; \n\n")
sql.write("CREATE TABLE IF NOT EXISTS charcurAlias \n \t (char_link TEXT, \n \t char_cur_alias TEXT); \n\n")
sql.write("INSERT INTO charcurAlias \n \t (char_link, \n \t char_cur_alias) \n VALUES \n")
for i in curAlias:
    if i == curAlias[-1]:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "); \n" )
        print(i)
    else:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "), \n" ) # comma
    if curAlias.index(i)%1000 ==0:
        print(curAlias.index(i))
 # semicolon
print("File created successfully")


allAlias=[]
csv_l = csv.reader(l)
line_count = 0
for row in csv_l:
    if line_count>0:
        allAlias.append(row)
    line_count = line_count + 1

        
sql.write("DROP TABLE IF EXISTS charallAlias; \n\n")
sql.write("CREATE TABLE IF NOT EXISTS charallAlias \n \t (char_link TEXT, \n \t char_all_alias TEXT); \n\n")
sql.write("INSERT INTO charallAlias \n \t (char_link, \n \t char_all_alias) \n VALUES \n")
for i in allAlias:
    if i == allAlias[-1]:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "); \n" )
        print(i)
    else:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "), \n" ) # comma
    if allAlias.index(i)%1000 ==0:
        print(allAlias.index(i))
 # semicolon
print("File created successfully")

sql.close()
f.close()
g.close()
l.close()


                       


