import json

students = open("students.json", "r")

data = json.load(students)
result = []
for i in data:
    limited = {
        "name": i["name"],
        "surname": i["surname"],
        "id": i["studentID"]
    }
    result.append(limited)

with open("limited.json","w") as limited:
    json.dump(result, limited, indent=2)