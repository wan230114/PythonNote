# %%
import time
import os
from multiprocessing import Pool, Array

_shm = Array('i', [0, 0])
# _shm = [0, 0]
print(list(_shm))


def worker(name, _shm):
    _shm[1] += 1
    time.sleep(1)  # random.random() * 2)
    print(f'hello {name}, {list(_shm)}')


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(10):
        p.apply_async(worker, args=(i, _shm))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
