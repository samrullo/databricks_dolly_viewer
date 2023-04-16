import pathlib
import requests
import json

data_file=pathlib.Path("../data/databricks-dolly-15k.json")
with open(data_file) as fh:
    all_records=json.load(fh)

from sqlalchemy import create_engine,inspect
engine=create_engine('sqlite:///../../db.sqlite3')
inspector=inspect(engine)
print("table names",inspector.get_table_names())

import pandas as pd
df=pd.DataFrame(all_records)
print("dataframe length ",len(df))

df['id']=df.index+1

df.to_sql('databrick_databrickmodel',engine,index=False,if_exists='replace')