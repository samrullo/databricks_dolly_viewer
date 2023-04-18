import sys
import pathlib

sys.path.append(pathlib.Path.cwd())

from config import DBricksConfig
from datasets import load_dataset
from nltk_utils import extract_nouns,get_eng_stop_words,get_pos_tags

folder=DBricksConfig.folder
filename=DBricksConfig.filename

data=load_dataset("json",data_files=str(folder/filename))
print(data)

def extract_nouns_as_tags(example,col_name):
    """
    Leverage nltk pos_tagger to extract nouns
    """
    example[f'{col_name}_noun_tags']=extract_nouns(example[col_name])
    return example

stop_words=get_eng_stop_words()
def extract_pos_tags(example,col_name):
    """
    extract pos(part of speech) tags
    """
    example[f'{col_name}_pos_tags']=get_pos_tags(example[col_name],stop_words)
    return example

def get_tag_count(example,col_name):
    """
    Assuming col_name contains list data, get its count
    """
    example[f"{col_name}_count"]=len(example[col_name])
    return example

train_ds=data['train']
# let's use map function of DatasetDict to extract nouns
for col_name in ['instruction','response']:
    train_ds=train_ds.map(lambda example : extract_pos_tags(example,col_name))
    train_ds=train_ds.map(lambda example : extract_nouns_as_tags(example,col_name))
    train_ds=train_ds.map(lambda example : get_tag_count(example,f"{col_name}_noun_tags"))

print("completed extracting tags")
new_filename="databricks-dolly-15k-with-tags.jsonl"
train_ds.to_json(folder/new_filename)