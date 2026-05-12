def fun2():
    try:
        d = [0] * 3
        for i in range(4):
            try:
                d[i] = i
            except TypeError as e:
                print(type(e), e)
    except AssertionError as e:
        print(type(e), e)
            
def fun1():
    try:
        return fun2()
    except NameError as e:
        print(type(e), e)
    
try:
    fun1()
except LookupError as e:
    print(type(e), e)
