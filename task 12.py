t = "greg"

p = [0]*len(t)
j = 0
i = 1

while i < len(t):
    if t[j] == t[i]:
        p[i] = j+1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

print(p)

a = "great greeting from greedy greg"
m = len(t)
n = len(a)

i = 0
j = 0
while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            print("Image is found")
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1

if i == n and j != m:
    print ('Image is not found')