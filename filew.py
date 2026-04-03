with open('demo.txt','w') as file:
    data = input("Please Enter the data ")
    file.write(data)

with open('demo.txt','a') as file:
    file.write("Ashish")

with open('demo.txt','r') as file:
    print(file.read())