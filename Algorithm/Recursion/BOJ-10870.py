def fibonacci(n):
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n-2) + fibonacci(n-1)
n = int(input())
print(fibonacci(n))
