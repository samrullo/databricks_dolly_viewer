from datasets import load_dataset
import pandas

def get_subjqa_dfs():
    subjqa=load_dataset("subjqa",name="electronics")
    dfs={split:dset.to_pandas() for split,dset in subjqa.flatten().items()}
    return dfs