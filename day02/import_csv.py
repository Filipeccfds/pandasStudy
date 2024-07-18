# %%
import pandas as pd

df_customers = pd.read_csv("../database/customers.csv", sep=";")
df_customers

# %%

df_customers.shape

# %%
df_customers.info(memory_usage="deep")

# %%

df_customers["Points"].astype(int)

# %%
df_customers["Points"].describe()

# %%

df_customers["Points"] + 1000

# %%

condicao = df_customers["Points"] > 1000
df_customers[condicao]

# %%

condicao = df_customers["Points"] == df_customers["Points"].max()
df_customers[condicao]

# %%
condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]


# %%

df_customers[["UUID", "Name"]]
# %%

df_colums = df_customers.columns.to_list()
df_colums.sort()
# cria um novo post nao atribuido ao prinicipal
#este atribui a dataframe principal
df_customers = df_customers[df_colums]

# %%
df_customers.rename(columns={"Name":"Nome",
                             "Points":"Pontos"
                })
# %%

df_customers.rename(columns={"UUID":"ID" }, inplace=True)
df_customers



# %%
condicao = (df_customers["Points"] >= 1000) & (df_customers["Points" >= 2000])
df_1000_2000 = df_customers[condicao]




notas = [ 34,43 ,23 ,1 ,5 ,7 ]
for i in notas:
    if i >=7:
        print(i)
    
# %%
notas_novas = []
for i in notas:
    notas_novas.append(i+1)

notas_novas