a = [1, 2, 3, 4, 5, 6]
Index = 0
for item in a:
    print(Index, item, a, end=' --> ')
    a.remove(item)
    print(a)
    Index += 1
print('a最终结果：', a)

a = {1, 2, 3, 4, 5, 6}
it = iter(a)
Index = 0
while True:
    try:
        item = next(it)
        print(Index, item, a, end=' --> ')
        a.remove(item)
        print(a)
        Index += 1
    except StopIteration:
        break
print('a最终结果：', a)
