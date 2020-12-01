M = int(input())
N = int(input())

arr = [0, 0] + [1 for _ in range(9999)]

ans_sum = 0
ans_min = 10001
for i in range(2, int(10001 ** 0.5)):
    for j in range(2 * i, 10001, i):
        if arr[i] == 0: continue
        arr[j] = 0

for i in range(M,N+1):
    if arr[i]:
        ans_min = i if ans_min > i else ans_min
        ans_sum += i
if ans_sum and ans_min:
    print(ans_sum)
    print(ans_min)
else:
    print(-1)
