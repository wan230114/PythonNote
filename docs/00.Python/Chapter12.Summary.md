
# 12. Python的一些特点总结

Python的几大特性
- 面向对象
  - 可变对象
      - 穿透命名空间
      - 穿透函数
- 灵活
- 易于拓展


Demo1: 
> 它既能保证了命名空间的独立性，又保证了数据处理的灵活性。

```python
L = []  # 直接定义同级命名空间
def f1():
    L.append(1)
f2 = lambda x: L.append(x)
print(L)
f1()
print(L)
f2(2)
print(L)
```

Demo2: 
```python
def add_m(L1):
    L1.append(1)
def m1():
    L1 = []
    add_m(L1)  # 传入函数的值，让函数内改变同步到外部空间
    print(L1)
m1()
```