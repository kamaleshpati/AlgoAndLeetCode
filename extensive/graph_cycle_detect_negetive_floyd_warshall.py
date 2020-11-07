import sys

INF = sys.maxsize


def isNegative(graph: list, vertices: int) -> bool:
    dist = [[0 for i in range(vertices)] for j in range(vertices)]
    for i in range(vertices):
        for j in range(vertices):
            dist[i][j] = graph[i][j]
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(vertices):
        if dist[i][i] < 0:
            return True
    return False


if __name__ == '__main__':
    graph = [[0, 1, INF, INF],
             [INF, 0, -1, INF],
             [INF, INF, 0, -1],
             [-1, INF, INF, 0]]

    if isNegative(graph, 4):
        print("neg")
    else:
        print("pos")
