#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-01-25, 19:53:12
# @ Modified By: Chen Jun
# @ Last Modified: 2021-01-26, 19:45:28
#############################################


# %%
import json
import re
import os
import sys
from copy import deepcopy


finame = sys.argv[1]
# finame = "./test.md"
# finame = "docs/01.Datascience/Datascience_3pandas.md"
foname1 = "ipynb_" + os.path.splitext(os.path.basename(finame))[0] + ".ipynb"
foname2 = "ipynb_" + \
    os.path.splitext(os.path.basename(finame))[0] + ".code.ipynb"


def get_file_iter():
    # res = []
    code_stat = 0
    changed_stat = 0
    with open(finame) as fi:
        content = []
        for line in fi:
            if re.findall(r"\s*```python", line):
                code_stat = 1
                changed_stat = 1
            elif code_stat and re.findall(r"\s*```(:?\r\n|\n)", line):
                code_stat = 0
                changed_stat = 1
            else:
                content.append(line)
                changed_stat = 0
            # print(content)
            if changed_stat:
                kw = "code" if not code_stat else "markdown"
                # res.append([kw, content])
                yield [kw, content]
                content = []


ipynb1 = {
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.7.9"
        }
    },
    "nbformat": 4,
    # "nbformat_minor": 4,
    "cells": [
        # {
        #     "cell_type": "code",
        #     "execution_count": null,
        #     "metadata": {},
        #     "outputs": [],
        #     "source": [
        #         "print(\"hello\")"
        #     ]
        # }
    ],
}
ipynb2 = deepcopy(ipynb1)


for kw, content in get_file_iter():
    # print(kw, content)
    data = {
        "cell_type": kw,
        "source": content,
        "metadata": {},
    } if kw == "markdown" else {
        "cell_type": kw,
        "source": content,
        "metadata": {"trusted": True},
        "outputs": [],
    }
    ipynb1["cells"].append(data)
    if kw == "code":
        ipynb2["cells"].append(data)


print(json.dumps(ipynb1, indent=2, ensure_ascii=False), file=open(foname1, "w"))
print(json.dumps(ipynb2, indent=2, ensure_ascii=False), file=open(foname2, "w"))

# %%
