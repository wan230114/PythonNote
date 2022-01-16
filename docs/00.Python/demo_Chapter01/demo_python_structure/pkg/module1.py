"""这是该模块1的说明文档"""

print("""这是模块1，它包含:
    三个变量: a -- 数值对象, ClassName -- 类对象, func -- 函数对象
    一个类: ClassName; 类方法有: __init__, main; 类属性有: self.arg
    一个函数: func
    五个语句块: 1 * class, 3 * def, 1 * for
    七个语句: 5 * print, a = 520, self.arg = arg
    """)

a = 520

class ClassName(object):
    """这是类的说明文档"""
    def __init__(self, arg):
        """这是类默认方法的说明文档"""
        self.arg = arg

    def main(self):
        """这是类方法的说明文档"""
        print("用于执行类方法的具体语句，打印该行字符串")


def func():
    """这是函数的说明文档"""
    print("用于打印函数")
    print("用于执行函数的具体语句，打印该行字符串")


for i in "123456":
    print(i)
