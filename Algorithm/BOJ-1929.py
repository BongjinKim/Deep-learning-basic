M, N = map(int, input().split())
arr = [0, 0] + [1 for _ in range(999999)]
#에라토스테네스의 채, O(N**0.5)
for i in range(2, int(1000001**0.5)):
    for j in range(i * 2, 1000001, i):
        if arr[j] == 0: continue
        arr[j] = 0
for r in range(M, N+1):
    if arr[r]: print(r)
