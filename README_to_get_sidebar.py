# with open('./README.md', 'rb') as fi, open('./_sidebar.md', 'wb') as fo:
#     p = -1
#     for line in fi:
#         if line.startswith(b'<!-- menu -->'):
#             p *= -1
#         elif p > 0:
#             fo.write(line)
import re
with open('./README.md', 'rb') as fi:
    doc = fi.read()
    L_job1 = re.compile(rb'<!-- menu -->.*?<!-- menu -->',
                        re.DOTALL).findall(doc)
    if L_job1:
        # print(L_job1)
        with open('./_sidebar.md', 'wb') as fo:
            fo.write(L_job1[0])
    L_job2 = re.compile(rb'<!-- introduction -->.*?<!-- introduction -->',
                        re.DOTALL).findall(doc)
    if L_job2:
        # print(L_job2[0].decode())
        with open('./00.Python/Introduction.md', 'wb') as fo:
            fo.write(L_job2[0])
