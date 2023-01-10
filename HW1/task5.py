"""
    Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число, предел (limit), после чего попробуйте сгенерировать по порядку все числа. Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.
"""
import functools as ft
import operator as op
import itertools as it

def count_find_num(primesL, limit):
    nums = set()
    if (mult := ft.reduce(op.mul, primesL)) < limit:
        nums.add(mult)
    while any(newOnes := set(filter(
        lambda x: x <= limit and not (x in nums),
            map(
                lambda x: ft.reduce(op.mul, x), it.product(list(nums), primesL)
            )
        ))):
        nums = nums.union(newOnes)
    if any(nums):
        return [len(nums), sorted(nums).pop()]
    return []

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []

