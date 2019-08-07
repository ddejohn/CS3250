class A:
    def __init__(self):
        super().__init__()
        print(self.__class__.__bases__)
        # print("A")
        # for base in self.__class__.__bases__:
        #     print(d[base])


class B:
    def __init__(self):
        super().__init__()
        # print("B")


class C:
    def __init__(self):
        super().__init__()
        # print("C")


class D:
    def __init__(self):
        super().__init__()
        # print("D")


d = {
    A: "class A",
    B: "class B",
    C: "class C",
    D: "class D"
}


classes = [A, B, C, D]
Z = type('Z', (A, B, C, ), {})()
# print(vars(Z))
# print(type(Z))