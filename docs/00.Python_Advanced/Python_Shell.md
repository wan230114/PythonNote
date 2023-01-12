
# 与Linux客户端的交互

```python
import multiprocessing
import subprocess
import time
from datetime import datetime as dt


for i in range(10):
    cmd = f"set -eo pipefail; echo 1 | grep 123 | awk '/SA:Z:/' "
    cmdrun = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if cmdrun.returncode == 0:
        break
    else:
        time.sleep(0.5)
        logtext = (f"Error: Exit code {cmdrun.returncode}\nCMD:\n{cmd}" +
                    "\nlog-stdout:\n" + cmdrun.stdout.decode("utf-8", "ignore") +
                    "\nlog-stderr:\n" + cmdrun.stderr.decode("utf-8", "ignore"))
        print(f"Error, (xxxx) Retrying {i} ...")
else:
    raise AssertionError(logtext)
```

