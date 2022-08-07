# %%
from multiprocessing import Pool
import time
import os
from multiprocessing import Pool, Array

# _shm = Array('i', [0, 0])
_shm = [0, 0]
print(list(_shm))


def worker(name, _shm):
    _shm[1] += 1
    time.sleep(1)  # random.random() * 2)
    print(f'- childer process {os.getpid()}.')
    print(f'hello {name}, {list(_shm)}')
    return f"{name} {_shm}"


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    # print(
    #     list(p.map(
    #         worker,
    #         range(10), [_shm]*10
    #     ))
    # )
    for i in range(10):
        result = p.apply_async(worker, args=(i, _shm))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print(result.get())


# %%


# def f(x):
#     time.sleep(x)
#     print(f"test {x}")
#     return f"res: {x}"


# if __name__ == '__main__':
#     with Pool(2) as p:
#         print(p.map(f, [1]*10))
