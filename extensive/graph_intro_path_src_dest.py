from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)

    def printAllPaths(self, src, dest):
        visited = [False] * self.V
        paths = []

        self.printAllPathsRecursive(src, dest, visited, paths)

    def printAllPathsRecursive(self, src, dest, visited, paths):
        visited[src] = True
        paths.append(src)

        if src == dest:
            print(paths)
        else:
            for i in self.graph[src]:
                if not visited[i]:
                    self.printAllPathsRecursive(i, dest, visited, paths)

        paths.pop()
        visited[src] = False


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)

    s = 2
    d = 3
    g.printAllPaths(s, d)
