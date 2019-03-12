class A():
    def __enter__(self):
        print('enter')
        self.a = 1
        return self

    def f(self):
        print('f')

    def __exit__(self, a, b, c):
        print('exit')


def func():
    return A()

with A() as a:
    # 1 / 0

    b = func()
    b.a = 3
    print(b.a)
    print(a.a)
