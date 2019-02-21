# Notes or anything need to be memorized

* * *

-   \_\_init\_\_: 用在class的定义中，表示在class在创建时，自动调用进行初始化的函数

```python
>>> class tester: # Class-based alternative (see Part VI)
  def __init__(self, start): # On object construction,
    self.state = start # save state explicitly in new object
  def nested(self, label):
    print(label, self.state) # Reference state explicitly
    self.state += 1 # Changes are always allowed

>>> F = tester(0) # Create instance, invoke __init__
>>> F.nested('spam') # F is passed to self
spam 0
>>> F.nested('ham')
ham 1
```

-   List(列表？)与Tuple(元组)的区别：
    1.  List成员用\[]修饰；Tuple用()
    2.  List容量及成员均可以改变；Tuple为只读属性，只可访问
-   Dictionary字典
    1.  有点类似C++中的map，即对应关系

```Python
>>> aDict = {'host': 'earth'} # create dict
>>> aDict['port'] = 80 # add to dict
```

-   print的格式化写法：

```python
>>> print("key=%s, value=%s" % (key, dict2[key]))
```

-   python2中的range()函数返回的是一个list\[]列表;python3中返回的是一个迭代器，节省内存，需要加list修饰才能输出列表。

```python
#python2
>> range(0, 3, 1)
[0, 1, 2]
#python3
>> list(range(0, 3, 1))
[0, 1, 2]
```

-   解释器：当我们编写Python代码时，我们得到的是一个包含Python代码的以.py为扩展名的文本文件。要运行代码，就需要Python解释器去执行.py文件。官方解释器为CPython，PyPy是另一个Python解释器，它的目标是执行速度。PyPy采用JIT技术，对Python代码进行动态编译（注意不是解释），所以可以显著提高Python代码的执行速度。
-   列表生成式：列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

```python
#一番簡単なの
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1x1, 2x2, 3x3, ..., 10x10]
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 条件を付きの場合
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
```

-   由此引申出的生成器：如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
    -   同时，生成器也可以以函数的形式存在，包含yield关键字

```python
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>
>>> next(g)
0
>>> for n in g:
...     print(n)
```

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b #关键字
        a, b = b, a + b
        n = n + 1
    return 'done'
```

-   函数式编程：函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
