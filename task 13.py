t = "hooligans"
#формирование таблицы смещений

s = set() #unique symbols
m = len(t) #image length
d = {} #collection of movements

for i in range(m-2, -1, -1):
    if t[i] not in s:
        d[t[i]] = m - i - 1
        s.add(t[i])

if t[m-1] not in s:
    d[t[m-1]] = m

d['*'] = m

print(d)

a = "hoola-hoola girls like hooligans"
n = len(a)

if m >= m:
    i = m-1

    while(i < n):
        k = 0
        for j in range(m-1, -1, -1):
            if a[i-k] != t[j]:
                if j == m-1:
                    if j == m-1:
                        off = d[a[i]] if d.get(a[i], False) else d['*']
                else:
                    off = d[t[j]]

                i += off
                break

            k +=1
        if j == 0:
            print(f'image is found by index {i-k+1}')
            break

    else:
        print("image is not found")
else:
    print("image is not found")