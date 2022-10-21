import requests
                                                       
url = input("Enter domain or IP with / at end:")
path = input("Enter Wordlist path :")

file = open(path, "r")

for i in range(len(file)):
   wls = file.readline()
   r = requests.get(url+wls)
   stats = r.status_code

if stats == 200:
   print("="*50)
   print("Path :"+url+wls, (stats))
   print("="*50)
elif stats == 404:
   print("="*50)
   print("Path :"+url+wls, (stats))
   print("="*50)
else:
   print("="*50)
   print("Path :"+url+wls, (stats))
   print("="*50)

file.close()
