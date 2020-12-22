"""此脚本用于示例，Python所有基本语法"""
from datetime import datetime  # 该句话在做什么？


class Work():  # class 是什么？
    """一个自动化蔬菜工厂的控制程序"""

    def __init__(self, workarea, ):  # 该 def 是什么？
        # 类属性
        self.WORK_AREA = workarea  # 该句话在做什么？
        self.ALL_AREA = {"A", "B", "C"}  # 该句话在做什么？

    def main(self):  # 类方法
        """调控"""
        self.check()  # 该句话在做什么？
        self.do()

    def check(self):
        if self.WORK_AREA in self.ALL_AREA:  # if 是什么？ 此处的 in 是什么？
            print("输入区域检测通过")  # print() 是什么？
            print("正在检测植物各类需求量")
        else:
            raise Exception("检测有问题")  # raise 是什么？

    def do(self):
        for x in ["浇水", "施肥", "光照", "收割"]:  # for ... in ... 是什么？
            print("--> 正在" + x)  # 该句话在做什么？
        else:
            print("工作完成")
            fo = open("log.txt", "a")
            fo.write("Work done at %s.\n" % datetime.now())
            fo.close()


def main():  # 该 def 是什么?
    a = Work("A")  # 该句话在做什么？
    a.main()  # 该句话在做什么？


if __name__ == "__main__":
    main()  # 该句话在做什么？
