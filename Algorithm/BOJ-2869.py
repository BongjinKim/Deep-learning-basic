import math

A, B, V = map(int, input().split())
little = 0.0000001
# (h-1) * (A-B) + A >= V 이므로
# h >= (V - B) / (A - B) 이다. int()를 사용하면 >로 바꾸어야 정확한 값을 가지므로 작은 값을 빼서 부등호 수정함 
print(int((V - B) / (A - B) - little) + 1)
