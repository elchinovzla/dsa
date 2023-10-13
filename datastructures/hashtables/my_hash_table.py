class MyHashTable:
    def __init__(self, size) -> None:
        self.data = [None] * size

    def hash(self, key):
        res = 0
        for i in range(len(key)):
            res = (res + ord(key[i])) % len(self.data)
        return res

    def set(self, key, value):
        self.data[self.hash(key)] = value

    def get(self, key):
        return self.data[self.hash(key)]


myHashTable = MyHashTable(3)
myHashTable.set("sonny0", 0)
myHashTable.set("sonny2", 2)
myHashTable.set("sonny1", 1)
print(myHashTable.get("sonny0"))
print(myHashTable.get("sonny1"))
print(myHashTable.get("sonny2"))
