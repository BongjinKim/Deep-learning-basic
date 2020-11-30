arr = [0, 0] + [1 for _ in range(123456 * 2 + 1)]

for i in range(2, 123456 * 2 + 1):
    for j in range(i * 2, 123456 * 2 + 1, i):
        if arr[j] == 0: continue
        arr[j] = 0

while True:
    n = int(input())
    if n == 0: break
    count = 0
    for i in range(n+1, 2*n + 1):
        if arr[i]: count += 1
    print(count)
