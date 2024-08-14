# %% 

import pandas as pd
import os

def import_etl(path:str):
    name = path.split("/")[-1].split(".")[0]
#aqui eu pego o path que vai ser uma string no caso url
# divido ela pelo "/", uso [-1] para pegar o ultimo elemento
#neste ultimo elemento divio o "." e pego o elemento antes do ponto usando ´[0]
    df = (pd.read_csv(path, sep=";")
          .rename(columns={"valor":name})
          .set_index(["cod","nome","período"]))
    return df

# %%

path = "../database/ipea/"
files = os.listdir(path)

# %%
dfs=[]
for i in files:
    dfs.append(import_etl(path+i))

# %%
dfs[2]

# %%
df_todos = pd.concat(dfs, axis=1).reset_index()
df_todos.to_csv("../database/df_allipea.csv", sep=";",index=False)
df_todos