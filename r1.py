import csv
headers=[]
rows=[]
with open('input.csv','r') as FI:
    csvreader=csv.reader(FI)
    headers=next(csvreader)
    for row in csvreader:
        rows.append(row)
print(headers)
print(rows)
count=0
for i in rows:
    if len(i):
        count+=1
for i in range(count):
    title=rows[i][2]
    h1=rows[i][2]
    h2=rows[i][3]
    explanation='explanation goes here'
    code='code goes here'
    filename=(rows[i][0])+'\\' + (rows[i][1])+'.html'
    indxFile='index1.html'
    

    
    with open(filename,'w') as FR:
    
        e = ['<!DOCTYPE html>', '<html>', '<head>', '<title>', title, '</title>', '</head>',
             '<body>',
             '<h1>', h1, '</h1>', '<div>', '<h2>', h2, '</h2>',
             '<div>', '<p>', explanation, '</p>', '</div>',
             '<div>', '<pre>', '<code class="language-python">', code, '</code>', '</pre>', '</div>',
             '</div>', '</body>', '</html>']
        e = [i+'\n' for i in e]

        FR.writelines(e)
