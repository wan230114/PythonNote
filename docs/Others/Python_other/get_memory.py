import psutil


def get_memory_info():
    virtual_memory = psutil.virtual_memory()
    used_memory = virtual_memory.used/1024/1024/1024
    free_memory = virtual_memory.free/1024/1024/1024
    memory_percent = virtual_memory.percent
    memory_info = "Usage Memory：{:.2f} G，Percentage: {:.1f}%，Free Memory：{:.2f} G".format(
        used_memory, memory_percent, free_memory)
    return memory_info


print(get_memory_info())
