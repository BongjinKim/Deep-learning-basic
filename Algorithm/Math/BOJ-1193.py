import math

X = int(input())
if X == 1:
    print('1/1')
else:
    # X는 항상 N+1번째 그룹에 속해있음
    N = int(math.sqrt(2 * X + 0.25) - 0.5000001)
    S = int(X - ((N*N + N) / 2))
    if (N+1) % 2: #N+1이 홀수이면 (N+1) - S + 1 / S 가성립함. 분자의 최소값은 1이므로 +1 해줌
        print(str(N-S+2) + '/' + str(S))
    else: #N+1이 짝수이면 반대임
        print(str(S) + '/' + str(N-S+2))
