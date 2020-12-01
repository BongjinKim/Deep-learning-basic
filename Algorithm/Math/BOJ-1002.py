T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    l = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(-1 if x1 == x2 and y1 == y2 and r1 == r2 else 0
             if r1 + r2 < l or abs(r1 - r2) > l else 1
             if r1 + r2 == l or abs(r1 - r2) == l else 2)
