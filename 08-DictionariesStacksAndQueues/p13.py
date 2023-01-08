import json

student = {
    "firstname":"Jakub",
    "lastname": "Cecula",
    "age":20,
    "height": 6.2,
    "hobby":["football","music","coding"],
    "married": False,
    "gender": "male"
}
file = open("student.json", "a")
json.dump(student, file, indent=2)
