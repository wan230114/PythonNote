'''hello, this is help doc for load.'''
print("demo01的__doc__属性：", __doc__)
print("demo01的__file__属性：", __file__)
print("demo01的__name__属性：", __name__)

a = 'demo'

if __name__ == "__main__":
    print('主脚本将会打印该句话')
else:
    print('若调用该模块将会打印该句话')
