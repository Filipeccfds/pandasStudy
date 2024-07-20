# %%
import pandas as pd

df = pd.read_csv("../database/customers.csv", sep=";")
df

# %%

df.sort_values(by="Points",ascending=False, inplace=True)
df.rename(columns={"Name":"Nome","Points":"Pontos"}, inplace=True)
df

# %%
df = (df.sort_values(by="Points", inplace=True)
        .rename(columns={"Name":"Nome","Points":"Pontos"}, inplace=True))
df

# %%

df.sort_values(by=["Points", "Name"],ascending=[False,True], inplace=True)
df
