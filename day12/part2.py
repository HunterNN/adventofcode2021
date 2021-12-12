from pyvis.network import Network

class Node():
    def __init__(self, id) -> None:
        self.id = id
        self.neighbors = {}
        self.walked_paths = []

    def addNeighbor(self, neighbor):
        if not neighbor.id in self.neighbors:
            self.neighbors[neighbor.id] = neighbor

    def isSmallCave(self):
        return self.id.lower() == self.id and not self.id == 'end' and not self.id == 'start'

    def goThroughPath(self, walked_path):
        walked_path = walked_path.copy()
        walked_path.append(self.id)
        if self.id == "end":
            self.walked_paths.append(walked_path)
            return
        for neighbor_id in self.neighbors:
            neighbor = self.neighbors[neighbor_id]
            if neighbor_id == "start":
                continue
            if neighbor.isSmallCave() and neighbor_id in walked_path:
                if walked_path[0] > 0:
                    _walked_path = walked_path.copy()
                    _walked_path[0] -= 1
                    neighbor.goThroughPath(_walked_path)
                continue
            neighbor.goThroughPath(walked_path)



def showGraph(nodes):
    net = Network()
    for node in nodes:
        if node == "start":
            net.add_node(node, color='#00ff1e', value=3)
        if node == "end":
            net.add_node(node, color='#dd4b39', value=3)
        else:
            if(nodes[node].isSmallCave()):
                net.add_node(node, value=1)
            else:
                net.add_node(node, value=2)
    for node in nodes:    
        for neighbor in nodes[node].neighbors:
            net.add_edge(node, neighbor)
    net.show('/tmp/mygraph.html')

with open("input.txt", "r") as f:
    nodes = {}
    lines = f.readlines()
    for line in lines:
        for part in line.replace("\n", "").split("-"):
            if not part in nodes:
                nodes[part] = Node(part)

    for line in lines:
        p1, p2 = line.replace("\n", "").split("-")
        nodes[p1].addNeighbor(nodes[p2])
        nodes[p2].addNeighbor(nodes[p1])

    nodes['start'].goThroughPath([1])
    print(len(nodes['end'].walked_paths))
    # for i in nodes['end'].walked_paths:
    #     print(i)