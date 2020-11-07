import sys


class Edge:
    def __init__(self, src, destination, cost):
        self.src = src
        self.destination = destination
        self.cost = cost


class Graph:
    def __init__(self, v, e):
        self.vertices = v
        self.edges = e
        self.graph = []

    def addEdge(self, src: int, dest: int, cost: int) -> None:
        self.graph.append(Edge(src, dest, cost))

    def isNegativeCycle(self, start):
        dist = [sys.maxsize] * self.vertices
        dist[start] = 0
        for i in range(0,self.vertices - 1):
            for j in range(0,self.edges):
                srcVal = self.graph[j].src
                destVal = self.graph[j].destination
                costVal = self.graph[j].cost
                if dist[srcVal] != sys.maxsize and dist[srcVal] + costVal < dist[destVal]:
                    dist[destVal] = dist[srcVal] + costVal

        for value in range(0, self.edges):
            srcVal = self.graph[value].src
            destVal = self.graph[value].destination
            costVal = self.graph[value].cost
            if dist[srcVal] != sys.maxsize and dist[srcVal] + costVal < dist[destVal]:
                return True

        return False


if __name__ == '__main__':
    graph = Graph(5, 8)
    graph.addEdge(0, 1, -1)
    graph.addEdge(0, 2, 4)
    graph.addEdge(1, 2, 3)
    graph.addEdge(1, 3, 2)
    graph.addEdge(1, 4, 2)
    graph.addEdge(3, 2, 5)
    graph.addEdge(3, 1, 1)
    graph.addEdge(4, 3, -3)
    if graph.isNegativeCycle(0):
        print("negative")
    else:
        print("positive")

    graph = Graph(5, 8)
    graph.addEdge(0, 1, -1)
    graph.addEdge(2, 0, -4)
    graph.addEdge(1, 2, 3)
    graph.addEdge(1, 3, 2)
    graph.addEdge(1, 4, 2)
    graph.addEdge(3, 2, 5)
    graph.addEdge(3, 1, 1)
    graph.addEdge(4, 3, -3)
    if graph.isNegativeCycle(0):
        print("negative")
    else:
        print("positive")
