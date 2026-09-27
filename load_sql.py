import pandas as pd
import sqlite3

df = pd.read_excel("superstore_clean.xlsx")
conn = sqlite3.connect("superstore.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
conn.close()
print("Loaded", len(df), "rows into superstore.db")
