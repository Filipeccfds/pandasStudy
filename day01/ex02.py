# %%
import pandas as pd

dados = {
    "nome" :["teo","nah","napoleao"],
    "idade" :[31, 32 ,14]  
}

df = pd.DataFrame(dados)
df
# %%
df.columns
# %%
df['nome'].describe()
# %%

df["idade"].mean()
# %%
# ultimo nome na posição nome
df["nome"].iloc[-1]
