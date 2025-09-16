file1 = open("C:/Users/balas/Downloads/ict.txt")

file1 = open(r"C:/Users/balas/Downloads/ict.txt")

#THis will print every line one by one in the file
for i in file1:
    print (i)

file1 = open(r"C:/Users/balas/Downloads/ict.txt")
print (file1.read())

with open(r"C:/Users/balas/Downloads/ict.txt",'r') as f1:  
    data = f1.read() 
print(data)

f1 = open(r"C:/Users/balas/Downloads/ict.txt")
print (f1.read(5))

with open(r"C:/Users/balas/Downloads/ict.txt",'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

print (word)
 
file = open("3EK2A.txt",'w')
file.write("ICT ICT ICT \n")
file.write("ICT ICT ICT ICT ICT")
file.close()

with open("sathwik.txt","w") as f:
    f.write("Hello sathwik!!!") 
    f.close()

file = open("sathwik.txt",'a')
file.write("\n Department Department")
file.close()

with open(r'C:/Users/balas/Downloads/a.tif','rb') as file:
    binary_data = file.read()
    
with open('C:/Users/balas/Downloads/a.tif','wb') as f:
    f.write(binary_data)
    f.close()

import csv
# Reading from a CSV file
with open(r'C:/Users/balas/Downloads/data-1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    
# Writing to a CSV file
import csv
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Subject', 'Mark'])
    writer.writerow(['sathwik', 'PWP', 9])
    writer.writerow(['bala', 'PWP', 10])
    file.close()
    
try:
    with open(r'C:/Users/balas/Downloads/ict.txt', "r") as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    print("Lines:", line_count)
    print("Words:", word_count)
    print("Characters:", char_count)

except FileNotFoundError:
    print("Error: File not found. Check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

with open(r'C:/Users/balas/Downloads/ict.txt', "r") as file:
    lines = file.readlines()

print(lines)

import csv

with open(r'C:/Users/balas/Downloads/data-1.csv', "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open(r'C:/Users/balas/Downloads/ict.txt') as f1, open(r'C:/Users/balas/Downloads/data-1.csv', "r") as f2:
    content1 = f1.read()
    content2 = f2.read()

with open(r'C:/Users/balas/Downloads/ict.txt',r'C:/Users/balas/Downloads/data-1.csv "w") as merged:
    merged.write(content1)
    merged.write(content2)

