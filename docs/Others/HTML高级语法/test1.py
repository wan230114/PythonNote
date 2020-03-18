import os
import time

file = open('now_time' + '.txt', 'w')
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
file.close()
