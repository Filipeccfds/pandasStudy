# %%

import pandas as pd
import numpy as np

data = {
    "nome":["Teo","Nah","Lah","Mah","Jo"],
    "idade":[31,32,34,12,np.nan],
    "renda":[np.nan,3245,357,12432,np.nan],
}

df = pd.DataFrame(data)
df

# %%
# isna e para indentificar o que e nan
df["idade"].isna()
# %%
df.isna().sum()
# %%
df.isna().mean()
# %%
# fillna preencher os nan
# ele cria outro dataset para colocar no original tem que reatribuir
df.fillna({
    "idade":df["idade"].mean(),
    "renda":df["renda"].mean(),
})

# %%
# dropna tirar o nan - any qualquer um que tenha
# all toda a coluna  que tenham somente nan

df.dropna(subset=["idade","renda"], how="all")
# %% o tresh ele exibi a coluna de acordo com a quantidade que vc coloca se vc coloca ex 4 nesta coluna ele tem que ter 4 valores nao nulos
df.dropna(axis=1, thresh=4)
