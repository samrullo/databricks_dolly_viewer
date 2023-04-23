from haystack.document_stores.elasticsearch import ElasticsearchDocumentStore
from haystack.nodes.retriever.sparse import BM25Retriever
from haystack.nodes.reader.farm import FARMReader
from haystack.pipelines import ExtractiveQAPipeline


document_store = ElasticsearchDocumentStore(return_embedding=True)
retriever = BM25Retriever(document_store=document_store)

model_ckpt = "deepset/minilm-uncased-squad2"
max_seq_length, doc_stride = 384, 128
reader = FARMReader(model_name_or_path=model_ckpt, progress_bar=False,
                    max_seq_len=max_seq_length, doc_stride=doc_stride, return_no_answer=True)

item_id = "B0074BW614"
query = "Is it good for reading?"

pipe = ExtractiveQAPipeline(reader, retriever)

n_answers = 3
preds = pipe.run(query=query,
                 params={
                     "Retriever": {"top_k": 3}, 
                     "Reader": {"top_k": n_answers}})

print(f"Question : {preds['query']}")
for idx in range(n_answers):
    answer = preds['answers'][idx]
    print(f"Answer {idx+1} : {answer['answer']}")
    print(f"Review snippet: ...{answer['context']}...")
    print("\n\n")
