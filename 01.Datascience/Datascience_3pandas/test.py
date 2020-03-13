# %%
import numpy as np
import pandas as pd

name = ["Tony", "Patty", "Alon", "Hellen", "Bella"]
score = np.random.randint(60, 100, 5)

df = pd.DataFrame(data=np.dstack((name, score)).reshape(-1, 2),
                  columns=['name', 'score'])

df2 = df.sort_values(by='score', ascending=False)
print(df2)