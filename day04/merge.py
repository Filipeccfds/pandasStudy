# %%
import pandas as pd

data_user = {
    "id":[1,2,3,4],
    "nome": ["Teo","Mat","Nah","Mah"],
    "idade": [31,31,32,32]
    }

df_user = pd.DataFrame(data_user)
df_user

# %%
data_transacoes = {
    "id_user":[1,1,1,2,3,3],
    "vl":[432,532,123,6,4,87],
    "qtProdutos":[2,1,3,6,10,2],
}

df_trasancao = pd.DataFrame(data_transacoes)
df_trasancao

# %%
# so o que tem nos dois dataframes

df_trasancao.merge(df_user,
                   how="left",
                   left_on="id_user",
                   right_on="id"
                    )

# %%
df_trasancao.to_clipboard()