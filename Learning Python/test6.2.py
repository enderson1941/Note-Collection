from functools import reduce
a = "this is a string"
print(a[0])
b = list(a)
print(b)
print(type(b))
b[2:4] = ["a", "t"]
print(b)


class A(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print("a= ", self.__a, "b= ", self.__b)

    def __str__(self):
        return self.__a, self.__b

    def __call__(self, value):
        print("call params: ", value)


a1 = A(10, 20)
val = a1.__str__()
print(val)
print(type(val))
a1.myprint()
a1(25)

g = (x * x for x in range(10))
for p in g:
    print(p)

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
# def char2num(s):
#     return DIGITS[s]
#
# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#
# ret = str2int(5)
# print(ret)


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
