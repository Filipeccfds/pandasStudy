# %%

import pandas as pd

df_products = pd.read_csv("../database/products.csv",
                          sep=";",
                          names=["ID","Name","Description"])
df_products

# %%
df_products.rename({"Name":"Nome","Description":"Descrição"}, inplace=True)
df_products