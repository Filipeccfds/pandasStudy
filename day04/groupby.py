# %%
import pandas as pd

df = pd.read_excel("../database/transactions.xlsx")
df

# %%

condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user["Points"].sum()

# %% modo raiz
pontos = {}

for i in df["IdCustomer"].unique():
    condicao = df["IdCustomer"] == i
    pontos[i] = df[condicao]["Points"].sum()

pontos
# %% no goupby e separado o idcustomers 1 por 1 e excecuto aquilo que desejo
df_sum = df.groupby(["IdCustomer"])["Points"].sum()
# reset index transformou a serie em um dataframe
df_sum.reset_index()

# %%
import datetime

def resolucao_datas (x):
    diff = datetime.datetime.now() - x.max()
    return diff.days


# %%
# argg lhe permite usar lista e dicionario atribuindo algumas funçoes
(df.groupby(["IdCustomer"]).agg({
                        "Points": "sum",
                        "UUID": "count",
                        "DtTransaction": resolucao_datas,
                        }).rename(columns={
                        "DtTransaction": "Ultima Transacao",
                        "Points":"Valor",
                        "UUID":"Frequencia"
                        }).reset_index()
                        )