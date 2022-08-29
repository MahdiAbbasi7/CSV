import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
     with open ('user&pass.csv','r', encoding='utf-8') as f:
        reader=csv.reader(f)
        dict1={}
        for row in reader:
            dict1[row[1]]=row[0]
        dict2={}
        for i in range (1000,10000):
            hashed_password=hashlib.sha256(str(i).encode('utf-8')).hexdigest()
            dict2[hashed_password]=i
        for key in dict1:
            with open ('final.csv', 'w', newline='') as f1:
                writer=csv.writer(f1)
                password=dict2[key]
                name=dict1[key]
                writer.writerow([name,password])


