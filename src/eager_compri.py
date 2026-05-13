def pr(tag, v):
    print(tag, v)
    return v

def fun():
    return [pr('create:', i) for i in range(3)]

for i in fun():
    pr('use:', i)
