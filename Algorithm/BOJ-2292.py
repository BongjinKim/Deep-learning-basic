import math

N = int(input())
if N == 1:
    print(1)
else:
    q = (N - 1) / 6
    #q = (n^2 + n) / 2 에서의 n의 값을 구하면 해결가능
    n = math.sqrt(2 * q + 0.25) - 0.5
    
    if n > int(n):
        print(int(n)+2)
    else:
        print(int(n)+1)
