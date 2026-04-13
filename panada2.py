import csv 
with open('file.csv','w',newline='')as file:

    writer = csv.writer(file)

    writer.writerow(['name','Age','city'])
    writer.writerow(['ashish',21,'Delhi'])
    writer.writerow(['ashish1',22,'Delhi'])

with open('file.csv','r',newline='')as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)