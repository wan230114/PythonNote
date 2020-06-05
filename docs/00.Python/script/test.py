import subprocess


def runcmd(command):
    res = subprocess.run(command, shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    if res.returncode == 0:
        print("success:", res)
    else:
        print("error:", res)
    return res.returncode, res.stdout, res.stderr


# runcmd(["dir", "/b"])  # 序列参数
# runcmd("exit 1")  # 字符串参数
code, stdout, stderr = runcmd("echo 1231")  # 字符串参数
print(code, stdout, stderr)
code, stdout, stderr = runcmd("cat 1231")  # 字符串参数
print(code, stdout, stderr)
