def factorial(n):
    if n == 1:return 1
    if n >= 2:return factorial(n-1) * n

print(factorial(3))