T = int(input())
for _ in range(T):
    x, y = map(int, input().split()); n = int((y - x + 0.25)**0.5 + 0.5 - 0.00001)
    print(2*n-1 if y - x <= n**2 else 2*n)
