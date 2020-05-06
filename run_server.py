"""
cd /d %~dp0
explorer http://localhost:3000
powershell -ExecutionPolicy ByPass -Command "docsify serve"
"""

from multiprocessing import Process
import time
import os
print('Global_print', os.getpid())


def run_proc(name):
    time.sleep(2)
    os.system('explorer http://localhost:3000')
    print('Run child process %s (%s)…' % (name, os.getpid()))


if __name__ == '__main__':
    p = Process(target=run_proc, args=('test',))
    print('__main__ pid:', os.getpid())
    p.start()
    os.system('powershell -ExecutionPolicy ByPass -Command "docsify serve"')
