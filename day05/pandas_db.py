# %%
import pandas as pd
import sqlalchemy

# %%
engine = sqlalchemy.create_engine("sqlite:///../database/database.db")
# %%
df = pd.read_sql_table("transactions_cart", engine)
df

# %%

query = 'SELECT * FROM customers LIMIT 10'
df_customers = pd.read_sql_query(query, engine)
df_customers

# %%

query = """
SELECT *
FROM customers AS t1
LEFT JOIN transactions AS t2
ON t1.UIDD = t2.IdCustomer
LIMIT 10
"""

df_join = pd.read_sql_query(query, engine)
df_join

# %%

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

#  %%
# pra eu enxergar no banco entro  no bash e passo o caminho sqlite3 database/database.db

df_01.to_sql("tb_nova",engine, index=False)

# %%
df_02.to_sql("tb_nova",engine, index=False, if_exists="append")


