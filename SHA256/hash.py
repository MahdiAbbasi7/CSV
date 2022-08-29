import hashlib
import csv
with open ("user&pass.csv", encoding = 'utf-8') as file:
    reader = csv.reader(file)
    dict={}
    for row in reader:
        dict[row[1]] = row[0]
    dict_2={}
    for i in range(0000,9999):
        create_hash = hashlib.sha256(str(i).encode('utf-8')).hexdigest() #This line hashing namber in range (0000 ,9999)
        dict_2[create_hash]=i
    for key in dict:
        password=dict_2[key] # moghayese hash csv & hash create_hash
        name=dict[key]
        print([name,password])


#Rainbow_hack
