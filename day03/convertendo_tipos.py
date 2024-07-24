# %%
import pandas as pd

df = pd.read_csv("../database/customers.csv", sep=";")
df

#%%

df.dtypes

# %%

df["Points_Double"] = df["Points"] * 2
df

# %%

df[["Points","Points_Double"]].astype(float)

# %%

