
# global weight

def add(f, s):
    global weight
    res = f + s + weight
    return res

 

if __name__ == '__main__':
    weight = 4
    res = add(3, 5)
    print(res)
    pass

