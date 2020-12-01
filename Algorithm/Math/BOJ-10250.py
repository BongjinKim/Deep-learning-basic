T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    X = int(N / H - 0.00000001) + 1
    Y = N % H if N % H else H
    if H == 1 and W == 1:
        print(101)
    else:
        print(Y * 100 + X)
