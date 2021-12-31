
# global weight
# weight =999
 

class add_class02():
    def __init__(self, weight) -> None:
        self.weight = weight
        self.result = 0
    def add(self,f, s):
        # global weight
        self.result = f + s + self.weight
        # weight =100
        return self.result
    def result_print(self):
        print(self.result)

class minus_class02():
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

