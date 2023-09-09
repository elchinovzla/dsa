# allows to store data in key:value pairs
myDictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(myDictionary["year"])
print(myDictionary.get("model"))
print(myDictionary.keys())
print(myDictionary.values())

myDictionary["colour"] = "red"
myDictionary["colour"] = "blue"
print(myDictionary.items())

for key, value in myDictionary.items():
    print(key, value)
