# Notes or anything need to be memorized
---
- \__init__: 用在class的定义中，表示在class在创建时，自动调用进行初始化的函数

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
- List(列表？)与Tuple(元组)的区别：
  1. List成员用[]修饰；Tuple用()
  2. List容量及成员均可以改变；Tuple为只读属性，只可访问
- Dictionary字典
  1. 有点类似C++中的map，及对应关系

```Python
>>> aDict = {'host': 'earth'} # create dict
>>> aDict['port'] = 80 # add to dict
```
- print的格式化写法：
```python
>>> print("key=%s, value=%s" % (key, dict2[key]))
```
- python2中的range()函数返回的是一个list[]列表;python3中返回的是一个迭代器，节省内存，需要加list修饰才能输出列表。
```python
#python2
>> range(0, 3, 1)
[0, 1, 2]
#python3
>> list(range(0, 3, 1))
[0, 1, 2]
```
