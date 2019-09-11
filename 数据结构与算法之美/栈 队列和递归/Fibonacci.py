def fibonacci(n):
    nums = [0, 1]
    if n < 2:
        return nums[n]
    if n >= 2:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))