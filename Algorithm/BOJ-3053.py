import math
r = int(input())
print(round(math.pi * r ** 2, 6))
#오차가 0.0001까지 허용되므로 작은 값을 더해서 6자리로 맞춰줌
print(round(2 * r ** 2 + 0.000001, 6))
