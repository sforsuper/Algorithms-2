from queue import Queue

def bfs(matrix, v):
    visited = [0] * len(matrix)
    distance = [-1] * len(matrix)
    visited[v] = 1
    distance[v] = 0
    q = Queue(len(matrix))
    q.put(v)
    while not q.empty():
        vertex = q.get()
        for i in range(len(matrix)):
            if matrix[vertex][i] == 1:
                if visited[i] == 0:
                    visited[i] = 1
                    q.put(i)
                    distance[i] = distance[vertex] + 1
    return distance


f = open('lab2source.txt')
a = [list(map(int, x.split())) for x in f]
print(bfs(a,0))


