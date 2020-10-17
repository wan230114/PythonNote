var = 0


def print_var():
    global var
    print('[model var]:', var)


def set_var(n):
    global var
    print('修改var:', var, '-->', n)
    var = n


if __name__ == "__main__":
    print('test model var: ', var)
    set_var(100)
    print('test model var: ', var)
