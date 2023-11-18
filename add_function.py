import numpy


class math_add:
    def add_two_items(a, b):
        if isinstance(a, numpy.number) and isinstance(b, numpy.number):
            return a + b
        else:
            print(Exception)
