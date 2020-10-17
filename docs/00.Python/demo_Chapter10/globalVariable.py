from globalVariable_pkg import var, set_var, print_var

print_var()  # ____ 打印什么？
print('[var_main]: ', var)  # ____ 打印什么？

# 能否修改导入模块环境？
var = 1
print_var()  # ____ 打印什么？
print('[var_main]: ', var)  # ____ 打印什么？

# 能否通过导入模块的global, 修改当前主程序环境？
set_var(300)
print_var()  # ____ 打印什么？
print('[var_main]: ', var)  # ____ 打印什么？
