def callback_func(inputvalue):

    print("inputvalue : ", inputvalue)

    return
def call_func(one, two, callback_f):
    res = one + two
    callback_f(res)
    return

first = 10
second= 20
call_func(first, second, callback_func)