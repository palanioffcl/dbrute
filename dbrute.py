import requests

print("______________________________________________________________________________")
print("        _______           __                              __                  ")
print("       |       \         |  \                            |  \                 ")
print("       | $$$$$$$\        | $$____    ______   __    __  _| $$_     ______     ")
print("       | $$  | $$ ______ | $$    \  /      \ |  \  |  \|   $$ \   /      \    ")
print("       | $$  | $$|      \| $$$$$$$\|  $$$$$$\| $$  | $$ \$$$$$$  |  $$$$$$\   ")
print("       | $$  | $$ \$$$$$$| $$  | $$| $$|  \$$| $$  | $$| | $$ __ | $$|___|$$  ")
print("       | $$__/ $$|       | $$__/ $$| $$|     | $$__/ $$| | $$|  \| $$$$$$$$   ")
print("       | $$    $$|       | $$    $$| $$|      \$$    $$|  \$$  $$ \$$ \____   ")
print("        \$$$$$$$/         \$$$$$$$/ \$$|        \$$$$$$|   \$$$$   \$$$$$$$|  ")
print(" __________________________________________________Made by Palani_____________")                                                                    
                                                                    
                                                                    
url = input("Enter domain or IP :")
path = input("Enter Wordlist path :")

file = open(path, "r")

for i in range():
   wls = file.readline()
   r = requests.get(url+wls)
   stats = r.status_code

if stats == 200:
   print("_"*50)
   print("Path :"+url+wls, (stats))
   print("_"*50)
elif stats == 404:
   print("_"*50)
   print("Path :"+url+wls, (stats))
   print("_"*50)
else:
   print("_"*50)
   print("Path :"+url+wls, (stats))
   print("_"*50)

file.close()
