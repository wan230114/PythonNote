
#%%
import pandas as pd

df_test = pd.DataFrame(
    [["a1", "aa1",  "A", 1, 10000000],
        ["a2", "aa2",  "B1", 1, 10000000],
        ["a2", "aa2",  "B2", 2, 10000000],
        ["a3", "aa3",  "C1", 1, 10000000],
        ["a3", "aa3",  "C2", 2, 10000000],
        ["a3", "aa3",  "C2", 3, 10000000],
     ], columns=["name1", "name2", "type", "value", "value2"]
)

print(df_test.to_markdown())

# %%
df_test.iloc[:, 3:] = df_test.iloc[:, 3:].applymap(lambda x: "{:,}".format(x))
df_test
# %%

s = pd.Series(["elk", "pig", "dog", "quetzal"], name="animal")
print(s.to_markdown())
