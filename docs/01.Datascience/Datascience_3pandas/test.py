# %%
import pandas as pd


left = pd.DataFrame({'key1': ['K0', 'K0', 'K0', 'K0'],
                     'key2': ['K0', 'K0', 'K1', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K1'],
                      'key2': ['K1', 'K1', 'K2', 'K2'],
                      'A': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})


# result = pd.merge(left, right, on=['key1', 'key2'])
result = pd.merge(left, right,
                  #   on=['key1', 'key2'],
                  on=['key1'],
                  indicator=True,
                  suffixes=(False, False)
                  #   how="inner"
                  )
result


# %%
