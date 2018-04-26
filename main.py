# https://vpic.nhtsa.dot.gov/api/

import requests
import json


url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetAllMakes?format=json'

r = requests.get(url)
#print(r.text)
car_dict_list = json.loads(r.text)
#print(car_dict_list['Results'])

make_list = []
for item in car_dict_list['Results']:
    make_list.append(item['Make_Name'])
#    print(item['Make_Name'])

make_model_dict = {}
i=0
for item in make_list:
    try:
        model_list = []
        model_url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/'+item+'?format=json'
        model_r = requests.get(model_url)
        model_dict = json.loads(model_r.text)
        for thing in model_dict['Results']:
            model_list.append(thing['Model_Name'])
        make_model_dict[item] = model_list
    except:
        print('Failure '+str(i))
    i+=1
    
print(make_model_dict)
with open('make_model.txt', 'w') as file:
     file.write(json.dumps(make_model_dict)) 
