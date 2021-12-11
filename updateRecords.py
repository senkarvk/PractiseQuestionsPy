"""
This script will update 
1)index.html file with new lines in each Section List or String.
2)create a new html file in each subdirectory and link it from index.html file

input is taken from input.csv
new lines to be updated should be placed before running this script

pending or enhancements:
1) problem:
if a line is already present, it is not checked in index ,so duplicate lines will be created 
so, before adding new lines in input.csv, we have to check manually 
solution:
add a method to check a given line or input is already present dont add that line again.

2) problem:
need cleanup
sol:
write clean methods and remove unnecessary lines

a sample input.csv is present in home folder
"""
import csv
#reading input from input.csv
a=[]
headers=[]
rows=[]
with open('input.csv','r') as FI:
    csvreader=csv.reader(FI)
    headers=next(csvreader)
    for row in csvreader:
        rows.append(row)
count=0
for i in rows:
    if len(i):
        count+=1
#reading index file to update
indxFile='index.html'
with open(indxFile,'r') as FI:
    a=FI.readlines()
n=len(a)
#for each row in input , iterating and updating index
for i in range(count):
    component=rows[i][0]
    newFileName=rows[i][1]
    title=rows[i][2]
    h1=rows[i][2]
    h2='write a program to '+rows[i][2]
    explanation='explanation goes here'
    code='code goes here'
    filename=component+'\\' + (rows[i][1])+'.html'
    insrtIndx=0
    secFound=False
    for k in range(n):
        srh='<h2>'+component+' Questions</h2>'
        secIndx=0
        if srh.lower() in a[k].lower():
            secIndx=k
            secFound=True
            print('found section-------------')
        if secFound:
            if '</ol>' in a[k]:
                insrtIndx=k
                print(f'insert index is {insrtIndx}')
                break
    #creating string which has to be inserted
    newFilePth=component+'/'+ newFileName+'.html'
    newFileStr='<a href="'+newFilePth+'"  target="_blank">link</a>\n'
    insrtStr='<li>'+h2+'\n'+newFileStr+'</li>\n'
    print(f'inserting newlines {insrtStr}')
    a.insert(insrtIndx,insrtStr)
    #writing new html file in each section such as string or list
    with open(newFilePth,'w') as FR:
    
        e = ['<!DOCTYPE html>', '<html>', '<head>', '<title>', title, '</title>', '</head>',
             '<body>',
             '<h1>', h1, '</h1>', '<div>', '<h2>', h2, '</h2>',
             '<div>', '<p>', explanation, '</p>', '</div>',
             '<div>', '<pre>', '<code class="language-python">', code, '</code>', '</pre>', '</div>',
             '</div>', '</body>', '</html>']
        e = [i+'\n' for i in e]

        FR.writelines(e)
    #writing index.html
    with open(indxFile,'w') as FO:
        FO.writelines(a)
    
    


    
