from queue import Queue
from task2 import bfs

with open('lab2source.txt') as f:
    matrix = [list(map(int, x.split())) for x in f]
    visited = [0] * len(matrix)
    for i in range(len(matrix)):
        if visited[i] == 0:
            res = bfs(matrix, i)
            output = []
            for i in range(len(res)):
                if res[i] != -1:
                    output.append(i)
                    visited[i] = 1
            print(output)