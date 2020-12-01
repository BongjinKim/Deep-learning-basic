while True:
    a, b, c = sorted(map(int, input().split()))
    if a == 0: break #세 변중 하나도 0이면 안되므로 0일 경우 break
    print('right' if a**2 + b**2 == c**2 else 'wrong')
