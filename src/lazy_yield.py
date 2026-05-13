def pr(tag, v):
    print(tag, v)
    return v

def fun():
    for i in range(3):
        yield pr('create:', i)

for i in fun():
    pr('use:', i)
