import pandas as pd
df_csv=pd.read_csv('sample.csv')
print(f"Data frame csv : {df_csv}")
df_json=pd.read_json('sample.json')
print(f"DataFrame json : {df_json}")