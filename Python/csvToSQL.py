"""
We begin this tutorial using the cleaned data from an earlier
tutorial (ALT2 Revision Tutorial)  "annual_temp_cleaned.csv".

Using this data  we will produce a second file called
"setUpDatabase.txt".  This file can be used to create a
SQLlite3 database and populate the database with the data from
the .csv file.

The database, generated later, will become part of an interactive
website.
"""
#this is for antagClean616,featClean616,otherClean616,suppClean616
import csv
f = open("suppClean616.csv","r")
g = open("featClean616.csv","r")
h = open("antagClean616.csv","r")
m = open("otherClean616.csv","r")
sql = open("SetUpDatabase.txt",  "w")

#Supporting Characters
suppchar616=[]
csv_d = csv.reader(f)
line_count = 0
for row in csv_d:
    if line_count>0:
        suppchar616.append(row)
    line_count = line_count + 1


        
sql.write("DROP TABLE IF EXISTS suppChars; \n\n")
sql.write("CREATE TABLE IF NOT EXISTS suppChars \n \t (comic_num INTEGER, \n \t char_link TEXT); \n\n")
sql.write("INSERT INTO suppChars \n \t (comic_num, \n \t char_link) \n VALUES \n")
for i in suppchar616:
    if i == suppchar616[-1]:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "); \n" )
        print(i)
    else:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "), \n" ) # comma
    if int(i[0])%10000 ==0:
        print(i[0])
 # semicolon
print("File created successfully")


#Featured Characters
featchar616=[]
csv_d = csv.reader(g)
line_count = 0
for row in csv_d:
    if line_count>0:
        featchar616.append(row)
    line_count = line_count + 1


        
sql.write("DROP TABLE IF EXISTS featChars; \n\n")
sql.write("CREATE TABLE IF NOT EXISTS featChars \n \t (comic_num INTEGER, \n \t char_link TEXT); \n\n")
sql.write("INSERT INTO featChars \n \t (comic_num, \n \t char_link) \n VALUES \n")
for i in featchar616:
    if i == featchar616[-1]:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "); \n" )
        print(i)
    else:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "), \n" ) # comma
    if int(i[0])%10000 ==0:
        print(i[0])
 # semicolon
print("File created successfully")

#Other Characters
otherchar616=[]
csv_d = csv.reader(m)
line_count = 0
for row in csv_d:
    if line_count>0:
        otherchar616.append(row)
    line_count = line_count + 1


        
sql.write("DROP TABLE IF EXISTS otherChars; \n\n")
sql.write("CREATE TABLE IF NOT EXISTS otherChars \n \t (comic_num INTEGER, \n \t char_link TEXT); \n\n")
sql.write("INSERT INTO otherChars \n \t (comic_num, \n \t char_link) \n VALUES \n")
for i in otherchar616:
    if i == otherchar616[-1]:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "); \n" )
        print(i)
    else:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "), \n" ) # comma
    if int(i[0])%10000 ==0:
        print(i[0])
 # semicolon
print("File created successfully")

#Antagonists Characters
antagchar616=[]
csv_d = csv.reader(h)
line_count = 0
for row in csv_d:
    if line_count>0:
        antagchar616.append(row)
    line_count = line_count + 1


        
sql.write("DROP TABLE IF EXISTS antagChars; \n\n")
sql.write("CREATE TABLE IF NOT EXISTS antagChars \n \t (comic_num INTEGER, \n \t char_link TEXT); \n\n")
sql.write("INSERT INTO antagChars \n \t (comic_num, \n \t char_link) \n VALUES \n")
for i in antagchar616:
    if i == antagchar616[-1]:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "); \n" )
        print(i)
    else:
        sql.write( "\t (" + str(i[0]) + "," + str(i[1]) + "), \n" ) # comma
    if int(i[0])%10000 ==0:
        print(i[0])
 # semicolon
print("File created successfully")

sql.close()



                       

