import csv 
with open('file1.csv','w',newline='')as file:

    writer = csv.writer(file)

    writer.writerow(['Name','Father Name','Registration Number','Contact Number','Email id'])
    writer.writerow(['Ashish','Anil Kumar Giri',21240674,9580685615,'ag2064931@gmail.com'])
    writer.writerow(['Ashish kumar','XYZ',21240675,9580685616,'xyz2064931@gmail.com'])

with open('file1.csv','r',newline='')as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)