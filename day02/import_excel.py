# %%
#tem que instalar o openxls
import pandas as pd

df = pd.read_excel("../database/transactions.xlsx")

df
# %%
df.head()

# %%
df.shape

# %%

df.tail()

# %%

colunas = ["UUID",
        "Points",
        "IdCustomer",
        "DtTransaction"]

df = df[colunas]
df

# %%
df.info(memory_usage="deep")