class MyGraph():
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def addVertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def addEdge(self, node1, node2):
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def showConnections(self):
        for node in self.adjacent_list.items():
            print(node)


test = MyGraph()
test.addVertex("0")
test.addVertex("1")
test.addVertex("2")
test.addVertex("3")
test.addVertex("4")
test.addVertex("5")
test.addVertex("6")
test.addEdge("3", "1")
test.addEdge("3", "4")
test.addEdge("4", "2")
test.addEdge("4", "5")
test.addEdge("1", "2")
test.addEdge("0", "2")
test.addEdge("6", "5")
test.showConnections()
