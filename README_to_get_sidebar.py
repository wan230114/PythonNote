import re
import datetime

# with open('./docs/README.md', 'rb') as fi, open('./docs/_sidebar.md', 'wb') as fo:
#     p = -1
#     for line in fi:
#         if line.startswith(b'<!-- menu -->'):
#             p *= -1
#         elif p > 0:
#             fo.write(line)

with open('./docs/README.md', 'rb') as fi:
    doc = fi.read()
    L_job1 = re.compile(rb'<!-- menu -->.*?<!-- menu -->',
                        re.DOTALL).findall(doc)
    if L_job1:
        # print(L_job1)
        with open('./docs/_sidebar.md', 'wb') as fo:
            fo.write(L_job1[0])
    L_job2 = re.compile(rb'<!-- introduction -->.*?<!-- introduction -->',
                        re.DOTALL).findall(doc)
    if L_job2:
        # print(L_job2[0].decode())
        with open('./docs/00.Python/Introduction.md', 'wb') as fo:
            fo.write(L_job2[0])

print(datetime.datetime.now(), '写入完毕')
