from haystack.document_stores.elasticsearch import ElasticsearchDocumentStore
from haystack.nodes.retriever.sparse import BM25Retriever

document_store = ElasticsearchDocumentStore(return_embedding=True)
retriever=BM25Retriever(document_store=document_store)

item_id="B0074BW614"
query="Is it good for reading?"
retrieved_docs=retriever.retrieve(query=query,top_k=3,filters={"item_id":[item_id],"split":["train"]})

print(retrieved_docs[0])