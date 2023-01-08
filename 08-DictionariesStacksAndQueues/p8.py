person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person)
print(person["name"])
print(person["hobby"])
person["surname"] = "Cecula"
person["married"] = False
gender = {"gender": "male"}
person.update(gender)
person["hobby"] += ["bicycle"]
person["phone"].update({"work phone":"313131444"})
print(person)