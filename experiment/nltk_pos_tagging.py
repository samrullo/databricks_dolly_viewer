import pathlib
from datasets import load_dataset

folder=pathlib.Path(r"C:\Users\samrullo\programming\projects\nlp_related\databricks_dolly_viewer\databrick\data")
filename="databricks-dolly-15k.jsonl"

data=load_dataset("json",data_files=str(folder/filename))
print(data)