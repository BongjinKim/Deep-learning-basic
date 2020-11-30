N = int(input())
A = map(int,input().split())
answer = 0
arr = [1 for _ in range(1001)]

arr[0] = 0
arr[1] = 0
for i in range(2, int(1001**0.5)):
    if arr[i] == 0: continue
    for j in range(i * 2, 1001, i):
        arr[j] = 0

for i in A:
    answer += arr[i]
print(answer) 
