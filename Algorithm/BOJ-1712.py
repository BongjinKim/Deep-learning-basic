A, B, C = map(int, input().split())
if C > B:
    print(int(A / (C - B)) +1)
else:
    print(-1)
