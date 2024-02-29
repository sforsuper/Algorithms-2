import math

def arg_min(T, S):
    minn = -1
    m = math.inf  #максимальное значение
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            minn = i

    return minn

D = ((0, 3, 1, 3, math.inf, math.inf),
     (3, 0, 4, math.inf, math.inf, math.inf),
     (1, 4, 0, math.inf, 7, 5),
     (3, math.inf, math.inf, 0, math.inf, 2),
     (math.inf, math.inf, 7, math.inf, 0, 4),
     (math.inf, math.inf, 5, 2, 4, 0))

N = len(D) #число вершин графа
T = [math.inf]*N #последняя строка таблицы

v = 0 #вершина, с которой начинаем
S = {v} #пройденные вершины
T[v] = 0 #начальный вес для стартовой вершины
M = [0]*N #минимальные связи между вершинами

while v != -1:
    for j, dw in enumerate(D[v]): #перебор всех связанных с v вершин, dw - вес ребра между ними
        if j not in S:
            w = T[v] + dw #новая длина пути от начальной вершины до вершины j
            if w< T[j]:
                T[j] = w
                M[j] = v #связываем j с вершиной v
    v = arg_min(T,S) #выбор следующего узла с минимальным весом
    if v>=0: #выбираем вершину
        S.add(v) #вершина добавлена в рассмотрение

 #формируем оптимальный маршрут
 start = 0
 end = 4
 P = [end]
 while end != start:
     end = M[P[-1]]
     P.append(end)

print(P)
