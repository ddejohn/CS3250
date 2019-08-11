class A:
    def __init__(self):
        super().__init__()
        for base in self.__class__.__bases__:
            base()


class B:
    def __init__(self):
        super().__init__()


class C:
    def __init__(self):
        super().__init__()


class D:
    def __init__(self):
        super().__init__()


Z = type('Z', (A, B, C, ), {})()
