class Node:
    def __init__(self, value):
        self.node = {
            "value": value,
            "next": None
        }

    def getNode(self):
        return self.node


class LinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value).getNode()
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value).getNode()
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        previous_head = self.head
        self.head = Node(value).getNode()
        self.head["next"] = previous_head
        self.length += 1

    def insert(self, value, index):
        if index <= 0:
            self.prepend(value)
        else:
            previous_node = self.find_node(index-1)
            new_node = Node(value).getNode()
            new_node["next"] = previous_node["next"]
            previous_node["next"] = new_node
            self.length += 1

    def find_node(self, index):
        if index == self.length:
            return self.tail
        elif index > self.length:
            raise Exception("index out of bound")

        current_index = 0
        node = self.head
        while current_index < index:
            node = node["next"]
            current_index += 1

        return node

    def remove(self, index):
        if index == 0:
            self.head = self.head["next"]
            self.length -= 1
        else:
            previous_node = self.find_node(index-1)
            node_to_be_deleted = previous_node["next"]
            previous_node["next"] = node_to_be_deleted["next"]
            self.length -= 1

    def __str__(self) -> str:
        node = self.head
        returnstr = ""
        while node is not None:
            returnstr += node["value"] + "\n"
            node = node["next"]

        return returnstr


test = LinkedList("sonny")
test.append("ana")
test.prepend("leonardo")
test.insert("real madrid", 0)
test.insert("new york yankees", 5)
test.insert("sonya", 3)
test.remove(5)
test.remove(0)
test.remove(2)
print(test)
