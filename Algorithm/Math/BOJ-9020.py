T = int(input())
#배열의 곱연산 추가
arr = [0, 0] + [1] * 9999

for i in range(2, int(10001**0.5)):
    for j in range(i * 2, 10001, i):
        #쓸데없는 코드 삭제
        if arr[j]:
            arr[j] = 0
for _ in range(T):
    n = int(input())
    half_n = n // 2
    if n == 4:
        print(2, 2)
        continue
    
    if half_n % 2: #half_n이 홀수이면 half_n부터 루프
        for j in range(half_n, 1, -2):
            if arr[j] and arr[n-j]:
                print(j, n-j)
                break
    else: #half_n이 짝수면 half_n-1
        for j in range(half_n - 1, 1, -2):
            if arr[j] and arr[n-j]:
                print(j, n-j)
                break
