def pr(tag, v):
    print(tag, v)
    return v

def fun():
    result = []
    for i in range(3):
        result.append(pr('create:', i))
    return result

for i in fun():
    pr('use:', i)
