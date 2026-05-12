def fun2():
    try:
        d = [0] * 3
        for i in range(5):
            try:
                d[i] = i  # raises IndexError when i>=3
                print(d[i])
            except ZeroDivisionError as e:
                print(type(e), e)
    except AssertionError as e:
        print(type(e), e)
    print('fun2() returns')

def fun1():
    try:
        return fun2()
    except NameError as e:
        print(type(e), e)
    print('fun1() returns')

try:
    fun1()
except LookupError as e:
    print(type(e), e)
print('program ended cleanly')