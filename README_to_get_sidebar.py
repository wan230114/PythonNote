#! C:\Python37\python.exe
with open('./README.md', 'rb') as fi, open('./_sidebar.md', 'wb') as fo:
    p = -1
    for line in fi:
        if line.startswith(b'<!-- menu -->'):
            p *= -1
        elif p > 0:
            fo.write(line)
