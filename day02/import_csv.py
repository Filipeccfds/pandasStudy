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

notas = [ 34,43 ,23 ,1 ,5 ,7 ]
for i in notas:
    if i >=7:
        print(i)
    
# %%
notas_novas = []
for i in notas:
    notas_novas.append(i+1)

notas_novas