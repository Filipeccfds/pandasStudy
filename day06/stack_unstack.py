 # %%
import pandas as pd

df_all = pd.read_csv('../database/df_allipea.csv', sep=";")
df_all

# %%

df_all = df_all.set_index(['cod','nome','período'])

# %%

df_all.stack()
# %%
#reatribui pra as linhas as colunas que nao foram setada no set_index
df_stack = df_all.stack().reset_index().rename(columns = {'level_3': 'Tipo_Homicidio',
                                                0 :'Qtde'
                                                })
df_stack

# %%

df_unstack =df_stack.set_index(['cod','nome','período','Tipo_Homicidio']).unstack().reset_index()
df_unstack
# %%
df_unstack.columns
homicidio = df_unstack['Qtde'].columns.to_list()
homicidio
# %%
df_unstack.columns = ['cod','nome','período'] + homicidio
df_unstack
# %%
