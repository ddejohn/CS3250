# import dictionary_print
from pprint import pprint


class A:
    def __init__(self):
        super().__init__()
        print("a init")
        self.a = "a"
        self.a_num = 1

    def get_vars(self):
        return {
            "a dict": vars(self)
        }


class B:
    def __init__(self):
        super().__init__()
        print("b init")
        self.b = "b"
        self.b_num = 2

    def get_vars(self):
        return {
            "b dict": vars(self)
        }


class C:
    def __init__(self):
        super().__init__()
        print("c init")
        self.c = "c"
        self.c_num = 3

    def get_vars(self):
        return {
            "c dict": vars(self)
        }


class D(C, B, A):
    def __init__(self):
        super().__init__()
        print("d init")
        self.d = "d"
        self.d_num = 4

    def get_all_vars(self):
        return self.get_vars()


d = D()
pprint(d.get_all_vars())
# print(dictionary_print._verbose_print(d.get_all_vars()))


# {
#     "c_dict": {
#         "c": "c",
#         "c_num": 3
#     },
#     "b_dict": {
#         "b": "b",
#         "b_num": 2
#     },
#     "a_dict": {
#         "a": "a",
#         "a_num": 1
#     },
#     "d_dict": {
#         "d": "d",
#         "d_num": 4
#     },
# }