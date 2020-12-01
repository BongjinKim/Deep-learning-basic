import sys

n = int(input())
sequence = [0] + list(map(int, input().split()))
m = int(input())
p = [0 for _ in range(n+1)]
#prefix sum
p[1] = sequence[1] 
for i in range(2, n+1):
    p[i] = p[i-1] + sequence[i]
print(p)

for _ in range(m):
    s, e = map(int, input().split())
    stack = sequence[s]
    length = 1
    #e - s 가 홀수일때만 값이 0이 나올 수 있음
    for i in range(e-s, 2):
        for j in range(1, e-s-1):
            check = p[e+i] - p[s-1-j]
            print(check)
    print(e, s)
