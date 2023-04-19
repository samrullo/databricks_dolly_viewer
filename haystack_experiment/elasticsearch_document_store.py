import sys
import pathlib
sys.path.append(pathlib.Path.cwd())

from haystack.document_stores.elasticsearch import ElasticsearchDocumentStore
from load_subjqa_dataset import get_subjqa_dfs

document_store=ElasticsearchDocumentStore(return_embedding=True)
dfs=get_subjqa_dfs()

for split,df in dfs.items():
    docs=[{"text":row['context'],"meta":{"item_id":row['title'],"question_id":row['id'],"split":split}} for _,row in df.drop_duplicates(subset="context").iterrows()]
    document_store.write_documents(docs,index="document")

print(f"Loaded {document_store.get_document_count()} documents")
