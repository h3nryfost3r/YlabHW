def zeros(n):
    n2 = n5 = n10 = 0
    for num in range(1, n+1):
        while num % 10 == 0:
            n10 += 1
            num //= 10
        while num % 2 == 0:
            n2 += 1
            num //= 2
        while num % 5 == 0:
            n5 += 1
            num //= 5
    return n10 + min(n2, n5)

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
