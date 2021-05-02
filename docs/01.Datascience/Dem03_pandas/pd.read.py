# %%

# 数据生成
print("""c1	c2	c3	c4
5	6	7	8
9	NA	11	NA
13	14	15	16
17	18	19	20
""", file=open("./mat.tsv", "w"))

# %%
import pandas as pd


def pd_read_table_str(infile):
    # ! 二次读取的解决方案：先读第一行，将所有列指定为str，根据需求手动改类型，二次读取。
    colnames = pd.read_table(infile, nrows=1).columns
    dtype = {x: "str" for x in colnames}
    # dtype.update({"c1": "int"})  # 根据需要更改
    df = pd.read_table(infile, dtype=dtype, keep_default_na=False)
    # 如需将NA也识别为字符串，需指定参数，keep_default_na=False
    return df


pd_read_table_str("./mat.tsv")
#%%