
from calculation_sub02.calculation_class02 import add_class02
class add_class():
    def __init__(self, weight) -> None:
        self.weight = weight
    def add(self,f, s):         
        res = f + s + self.weight         
        return res

    def other_print(self):
        instance = add_class02(5)
        instance.result_print()

class minus_class():
    def __init__(self) -> None:
        pass
    def minus(self, first, second):
        result = first - second
        return result














# if __name__ == '__main__':
#     # weight = 4
#     inst = class_name(5)
#     res = inst.add(3, 5)
#     print(res)
#     # print('weight : ', weight)
    
#     pass

