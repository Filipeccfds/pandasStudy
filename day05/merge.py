# %%

import pandas as pd

df_customers = pd.read_csv("../database/customers.csv", sep=";")
df_customers
# %%

df_transactions = pd.read_excel("../database/transactions.xlsx")
df_transactions

# %%
df_cart = pd.read_parquet("../database/transactions_cart.parquet")
df_cart

# %%

df_join = (df_transactions.merge(df_customers,
                                how="inner",
                                left_on="IdCustomer",
                                right_on="UUID",
                                suffixes=["_Transaction","_Customer"]
                                ).merge(df_cart,
                                        how="inner",
                                        left_on="UUID_Transaction",
                                        right_on="IdTransaction",
                                        
                                ))

df_join