from pprint import pprint


class A:
    def __init__(self):
        super().__init__()
        self.a = "a"
        self.a_num = 1

    def get_vars(self):
        return {
            "a dict": {
                "a": self.a,
                "a_num": self.a_num,
            }
        }


class B:
    def __init__(self):
        super().__init__()
        self.b = "b"
        self.b_num = 2

    def get_vars(self):
        return {
            "b dict": {
                "b": self.b,
                "b_num": self.b_num,
            }
        }


class C:
    def __init__(self):
        super().__init__()
        self.c = "c"
        self.c_num = 3

    def get_vars(self):
        return {
            "c dict": {
                "c": self.c,
                "c_num": self.c_num,
            }
        }


class D(C, B, A):
    def __init__(self):
        super().__init__()
        self.d = "d"
        self.d_num = 4

    def get_vars(self):
        data = {
            "d dict": {
                "d": self.d,
                "d_num": self.d_num,
            }
        }
        for sup in D.mro()[:-2]:
            this = super(sup, self).get_vars()
            for key, val in this.items():
                data[key] = val 
        return data


d = D()
print(verbose(d.get_vars()))
# print(f"\nwhat I get:\n\n" + verbose(d.get_all_vars()))
# print(f"\n\nwhat I want:\n\n" + verbose({
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
# }))