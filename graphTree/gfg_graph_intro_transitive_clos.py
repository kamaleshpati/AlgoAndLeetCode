from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.transitive_mat = [[0 for i in range(self.vertices)] for j in range(self.vertices)]

    def addEdge(self, indices, vertex):
        self.graph[indices].append(vertex)

    def findTransitive(self):
        for i in range(self.vertices):
            self.DFSRecurrsive(i, i)
        return self.transitive_mat

    def DFSRecurrsive(self, masterVertex, slaveVertex):
        self.transitive_mat[masterVertex][slaveVertex] = 1

        for i in self.graph[slaveVertex]:
            if self.transitive_mat[masterVertex][i] == 0:
                self.DFSRecurrsive(masterVertex, i)


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print(g.findTransitive())
