import json
file = open("C:\\Users\\leasc\\github\\data_management_collection-\\Kayak_project\\booking_project\\booking_project\\spiders\\booking_project\\booking_test.json")
results = json.load(file) #charge le fichier dans une variable

import pandas as pd 
df = pd.DataFrame(results)

url_list = []
for url in df["url"]:
    url_list.append(url)
print(url_list)

textfile = open("url_list", "w") #ouvoere un fichier en mode écriture, le fichier est crée s'il n'existe pas
for element in url_list: #parcours chaque url
    textfile.write(element + "\n") #écrit chaque url
textfile.close() #ferme le fichier