
from calculation_sub.calculation_class import add_class
from .calculation_sub.calculation_class import minus_class


if __name__ == '__main__':
    # weight = 4
    inst = add_class(5)
    res = inst.add(3, 5)
    print(res)
    inst.other_print()

    inst02 = minus_class()
    result = inst02.minus(4,5)
    print(result)
    pass

