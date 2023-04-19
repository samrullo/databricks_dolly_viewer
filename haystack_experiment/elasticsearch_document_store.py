from haystack.document_stores.elasticsearch import ElasticsearchDocumentStore
from load_subjqa_dataset import get_subjqa_dfs

from datasets import load_dataset
import pandas


def get_subjqa_dfs():
    subjqa = load_dataset("subjqa", name="electronics")
    dfs = {split: dset.to_pandas() for split, dset in subjqa.flatten().items()}
    return dfs


document_store = ElasticsearchDocumentStore(return_embedding=True)
dfs = get_subjqa_dfs()

for split, df in dfs.items():
    docs = [{"content": row['context'], "meta":{"item_id": row['title'], "question_id":row['id'],
                                             "split":split}} for _, row in df.drop_duplicates(subset="context").iterrows()]
    document_store.write_documents(docs, index="document")

print(f"Loaded {document_store.get_document_count()} documents")
