from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,indices,vertex):
        self.graph[indices].append(vertex)

    def BFS(self, start):

        visited = [False] * len(self.graph)

        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            start = queue.pop(0)
            print(start , end=" ")

            for i in self.graph[start]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True





if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.BFS(2)

