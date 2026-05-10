import memory_graph as mg

class MyClass:
    def __init__(self):
        self.children = {i: [i]*10 for i in range(5)}

a = 1
b = (1, 2, 3)
c = MyClass()
d = (4, 5, 6, 7)

mg.render(locals(), "collapse_type1.png")
