a = "this is a string"
print(a[0])
b = list(a)
print(b)
print(type(b))
b[2:4]=["a","t"]
print(b)
class A(object):
    def __init__(self,a,b):
        self.__a=a
        self.__b=b
    def myprint(self):
        print("a= ",self.__a,"b= ",self.__b)
    def __str__(self):
        return self.__a,self.__b
    def __call__(self,value):
        print("call params: ",value)
a1=A(10,20)
val=a1.__str__()
print(val)
print(type(val))
a1.myprint()
a1(25)
