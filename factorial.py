def factorial(x):
    if x <= 1:
        return 1
    i = 1
    f = 1 
    while i <= x:
        f *= i
        i += 1
    return f