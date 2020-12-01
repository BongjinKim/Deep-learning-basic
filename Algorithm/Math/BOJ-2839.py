N = int(input())
five_bag = int(N / 5)
flag = True 

for i in range(five_bag, -1, -1):
    j = int((N - (i * 5)) / 3)
    #print(i, j)
    if (N - (i * 5)) % 3 == 0:
        
        print(i + j)
        flag = False
        break
if flag:
    print(-1)
