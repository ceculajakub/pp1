import json

file = open("euro.json", "r")
data = json.load(file)

print("Date       Buying Rate       Selling Rate")
print("-----------------------------------------") 
print("-----------------------------------------") 
for i in data["rates"]:
    print(i["effectiveDate"]+"       "+ str(i["bid"])+"       "+ str(i["ask"]))
