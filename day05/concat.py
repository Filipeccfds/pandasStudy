# %%
import pandas as pd

data_01 ={
    "id":[1,2,3,4],
    "nome": ["teo","Nah","mah","je"],
    "idade": [12,34,23,21]
}

df_01 = pd.DataFrame(data_01)
df_01
# %%
data_02 ={
    "id":[5,6,7,8],
    "nome": ["jose","route","red","titan"],
    "idade": [32,36,28,11]
}

df_02 = pd.DataFrame(data_02)
df_02

# %%
#drop true e para exluir a linha de index que a criada a mais
pd.concat([df_01,df_02]).reset_index(drop=True)

# %%

data_03 = {
    "sobrenome":["calvo","kuri","wizer","carlos","wiz"],
    "renda": [3100,3100,3200,3200,3200]
}

df_03 = pd.DataFrame(data_03).sort_values(["renda","sobrenome"], ascending=False)
df_03
# %%
# no concat quando se adiciona se orginiza pelo index
pd.concat([df_01,df_03],axis=1)