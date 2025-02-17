def factorial(n):
    if not isinstance(n, int):
        return False
    if n < 0:
        return False
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
