# %%
import pandas as pd

data = {
    "Nome":["Filipe","Lara","Teo","Cruz","Lara"],
    "Idade":[12,14,15,18,14],
    "Update_at": [1,3,2,4,3]
}

data

# %%
df = pd.DataFrame(data)
df
# %%
df.drop_duplicates()
# %%
df.drop_duplicates(subset=["Nome","Idade"], keep="last")
 # %%
df = (df.sort_values(by="Update_at", ascending=False )
       .drop_duplicates(subset=["Nome", "Idade"], keep="first"))
df