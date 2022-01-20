import requests

url = input("Enter domain or IP :")
path = input("Enter Wordlist path :")

file = open(path, "r")

for i in range():
   dir_name = file.readline()
   r = requests.get(url+dir_name)
   stats = r.status_code

if status == 200:
   print("*"*40)
   print("Path : "+url+dir_name, (stats))
   print("*"*40)
    
file.close()
