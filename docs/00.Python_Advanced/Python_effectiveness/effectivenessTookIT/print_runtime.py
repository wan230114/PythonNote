from datetime import datetime as dt
import sys
print(sys.version)


def print_runtime(func):
    def do(*args, **kwargs):
        t0 = dt.now()
        # print('[开始运行]%s' % t0)
        result = func(*args, **kwargs)
        t1 = dt.now()
        # print('[运行结束]%s' % t1)
        print('used time: %s, function: %s' % (t1-t0, func.__name__))
        return result
    return do
