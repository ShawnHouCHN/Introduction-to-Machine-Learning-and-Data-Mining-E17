import sqlite3
import pandas as pd


db_location = "../database.sqlite"

conn = sqlite3.connect(db_location)

df = pd.read_sql(sql="SELECT * FROM country", con=conn)


print(df)


conn.close()