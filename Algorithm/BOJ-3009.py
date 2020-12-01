a = [list(map(int, input().split())) for _ in range(3)]
print(a[2][0] if a[0][0] == a[1][0] else a[0][0] if a[1][0] == a[2][0] else a[1][0], a[2][1] if a[0][1] == a[1][1] else a[0][1] if a[1][1] == a[2][1] else a[1][1])
