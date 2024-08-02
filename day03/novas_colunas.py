# %%
import pandas as pd
import numpy as np

df = pd.read_csv("../database/customers.csv", sep=";")
df 
# %%
df["Points_Double"] = df["Points"] * 2
df
# %%
df["Points_Ratio"] = df["Points_Double"] / df["Points"]
df
# %%

df["Constante"] = None
df
# %%
df["Points_Log"] = np.log(df["Points"])
df
# %% jeito para colocar em caixa alto
nome_altas = []
for i in df["Name"]:
    nome_altas.append(i.upper())

df["Nome Alta"] = nome_altas
df
# %%
df["Name"].str.upper()

# %%

def get_first(nome:str):
    return nome.split("_")[0]
# %%
get_first("Antonio")
# %%
df["First_Name"] = df["Name"].apply(get_first)
df
# %%
#uma funcao com lambda e uma funcao que e para ser uma função simples executada para aquele momento especifico
df["Name"].apply( lambda x: x.upper().split("_")[0])

# %%
def intevalo(pontos): 
    if pontos < 2500:
        return "baixo"
    elif  pontos > 3580:
        return "medio"
    else:
        "alto"

df["Media_Pontuacao"] = df["Points"].apply(intevalo)

# %%
df["UIID"].apply(lambda x: x[-3])

# %%

data = {
    "nome":["Teo","Nah","Maria","Lara"],
    "recencia":[1,30,10,45],
    "valor":[100,2000,15,500],
    "frequencia":[2,5,1,15]
}

df_crm = pd.DataFrame(data)

def rfv(row):
   
    nota = 0

    if row["recencia"] <= 10:
        nota += 10
    elif 10 < row["recencia"] <= 30:
        nota += 5
    elif row["recencia"] > 30:
        nota += 0

    if row["valor"] > 1000:
        nota += 10
    elif 100 <= row["valor"] < 1000:
        nota += 5
    elif row["valor"] < 100:   
        nota += 0 

    if row["frequencia"] > 10:
        nota += 10
    elif 5 <= row["frequencia"] < 10:
        nota += 5
    elif row["frequencia"] < 5:
        nota += 0

    return nota



# %%
#axis pega o eixo na horizontal e na vertical

df_crm["RFV"]=df_crm.apply(rfv, axis=1)
df_crm

# %%
