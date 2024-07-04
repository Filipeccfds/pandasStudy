# %%
import pandas as pd

idades = [30, 42, 90, 34]

# %%
series_idades = pd.Series(idades)
series_idades

# %%
series_idades.mean()
# %%
series_idades.median()
# %%
series_idades.var()
# %%
series_idades.std()
# %%
series_idades.shape
# %%
series_idades.describe()
# %%
series_idades.index= ['a','b','c','d']
# %%
#iloc usado para pegar o elemento por posição
series_idades.iloc[0]
# %%
series_idades = pd.Series(idades, name='marola') 
series_idades
