
import traceback


def open_file(filename):
    try:
        f = open(filename, 'rt')
        print("\n打开的文件是：" + filename)
        s = f.read()
        print("读取文件成功! 文件中的内容是:")
        print(s)
    except Exception:
        print("读取文件" + filename + "失败! 错误信息是：")
        traceback.print_exc()


open_file("test_f_utf8.txt")
open_file("test_f_gbk.txt")

