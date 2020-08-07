import re
import datetime


def info(name):
    print(datetime.datetime.now(), name, '写入完毕')


def macth(rule, doc):
    return re.compile(rule, re.DOTALL).findall(doc)


# 1) 目录的预处理
with open('./README.md', 'rb') as fi:
    doc = fi.read()
    L_job1 = macth(
        rb'<!-- menu_base -->(.*?)<!-- menu_base -->', doc)
    L_job2 = macth(
        rb'<!-- menu_write -->.*?<!-- menu_write -->', doc)

if L_job1 and L_job2:
    menu = b'<!-- menu_write -->' + L_job1[0] + b'<!-- menu_write -->'
    menu = b'\r\n'.join((x.strip() for x in menu.splitlines()))
    with open('./README.md', 'wb') as fo:
        fo.write(doc.replace(L_job2[0], menu))

# 2) sidebar和intro匹配
with open('./README.md', 'rb') as fi:
    doc = fi.read()  # .replace(b'/docs/', b'')
    L_job1 = macth(
        rb'<!-- menu -->.*?<!-- menu -->', doc)
    L_job2 = macth(
        rb'<!-- introduction -->.*?<!-- introduction -->', doc)
# with open('./docs/README.md', 'wb') as fo:
#     info('./docs/README.md')
#     fo.write(doc)
if L_job1:
    sidebar = './_sidebar.md'
    with open(sidebar, 'wb') as fo:
        info(sidebar)
        fo.write(L_job1[0])
if L_job2:
    intro = './docs/00.Python/Introduction.md'
    with open(intro, 'wb') as fo:
        info(intro)
        fo.write(L_job2[0])
