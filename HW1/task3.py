def zeros(n):
    n10 = n2 = n5 = 0
    for num in range(1, n+1):
        if num % 10 == 0:
            n10 += num // 10
            continue
        if num % 2 == 0:
            n2 += num // 2
        if num % 5 == 0:
            n5 += num // 5

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
