"""
Надо написать класс CyclicIterator. Итератор должен итерироваться по итерируемому объекту (list, tuple, set, range, Range2, и т. д.), и когда достигнет последнего элемента, начинать сначала.
"""
class CyclicIterator:
    def __init__(self, values):
        self.values = values
        self.i_values = iter(values)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.i_values)
        except StopIteration:
            self.i_values = iter(self.values)
            return next(self.i_values)

cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
