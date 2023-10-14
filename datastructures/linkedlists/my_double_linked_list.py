class Node:
    def __init__(self, value):
        self.node = {
            "value": value,
            "next": None,
            "prev": None
        }

    def getNode(self):
        return self.node


class DoubleLinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value).getNode()
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value).getNode()
        new_node["prev"] = self.tail
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value).getNode()
        previous_head = self.head
        previous_head["prev"] = new_node
        new_node["next"] = previous_head
        self.head = new_node
        self.length += 1

    def insert(self, value, index):
        if index <= 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            node_at_index = self.find_node(index)
            new_node = Node(value).getNode()
            new_node["next"] = node_at_index
            new_node["prev"] = node_at_index["prev"]
            previous_node_index = node_at_index["prev"]
            node_at_index["prev"] = new_node
            previous_node_index["next"] = new_node
            self.length += 1

    def find_node(self, index):
        if index > self.length - 1:
            raise Exception("index out of bound")

        current_index = 0
        node = self.head
        while current_index < index:
            node = node["next"]
            current_index += 1

        return node

    def remove(self, index):
        if index == 0:
            second_node = self.head["next"]
            self.head = second_node
            second_node["prev"] = None
            self.length -= 1
        elif index == self.length - 1:
            second_last_node = self.tail["prev"]
            second_last_node["next"] = None
            self.tail = second_last_node
            self.length -= 1
        else:
            node_at_index = self.find_node(index)
            prev_node = node_at_index["prev"]
            next_node = node_at_index["next"]
            prev_node["next"] = next_node
            next_node["prev"] = prev_node
            self.length -= 1

    def __str__(self) -> str:
        node = self.head
        returnstr = ""
        while node is not None:
            returnstr += node["value"] + "\n"
            node = node["next"]

        return returnstr


test = DoubleLinkedList("sonny")
test.append("ana")
test.prepend("leonardo")
test.insert("real madrid", 0)
test.insert("new york yankees", 4)
test.insert("sonya", 3)
print(test)
test.remove(5)
test.remove(0)
test.remove(2)
print(test)
