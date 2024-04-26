def dfs(matrix, v, visited):
    visited[v] = 1
    for to in [count for count, value in enumerate(matrix[v]) if value == 1]:
        if visited[to] == 0:
            dfs(matrix, to, visited)


with open('lab2source.txt') as f:
    matrix = [list(map(int, x.split())) for x in f]
    visited = [0] * len(matrix)
    for i in range(len(visited)):
        if visited[i] == 0:
            dfs(matrix, i, visited)
            print(visited)
