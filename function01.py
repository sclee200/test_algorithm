 
def addsubmuldiv(a, b):
    print(f'{a}+{b}={a+b}')
    print(f'{a}-{b}={a-b}')
    print(f'{a}*{b}={a*b}')
    try:
        print(f'{a}/{b}={a/b}')
    except Exception as e:
        print(e)

addsubmuldiv(10,20)
addsubmuldiv(10,0)