"""
Написать метод bananas, который принимает на вход строку и возвращает количество слов «banana» в строке.

(Используйте - для обозначения зачеркнутой буквы)
"""

import itertools as it

def bananas(s):
    result = set()
    # Created set of permutations which can possible can implmented to word "banana"
    # (1, 0, ...), (0, 1, ...), ...
    maskPermutations = { x for x in it.permutations([1]*len('banana') + [0]*(len(s)-len('banana'))) }
    for mask in maskPermutations:
        if ''.join([x for x in it.compress(s, mask)]) == 'banana':
            result.add(''.join(list(map(lambda w, m: w if m else '-', list(s), mask))))
    return result

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

