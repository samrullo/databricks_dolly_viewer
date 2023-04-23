from haystack.document_stores.elasticsearch import ElasticsearchDocumentStore
from haystack.nodes import BM25Retriever
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline
import pathlib

document_store=ElasticsearchDocumentStore(return_embedding=True)

retriever=BM25Retriever(document_store=document_store)

model_ckpt = "deepset/minilm-uncased-squad2"
max_seq_length, doc_stride = 384, 128
reader = FARMReader(model_name_or_path=model_ckpt, progress_bar=False,
                    max_seq_len=max_seq_length, doc_stride=doc_stride, return_no_answer=True)

pipe=ExtractiveQAPipeline(reader,retriever)

query="What is the most cited town?"

n_answers = 3
preds = pipe.run(query=query,
                 params={
                     "Retriever": {"top_k": 3}, 
                     "Reader": {"top_k": n_answers}})

print(f"Question : {preds['query']}")
for idx in range(n_answers):
    answer = preds['answers'][idx].to_dict()
    print(f"Answer {idx+1} : {answer['answer']}")
    print(f"Review snippet: ...{answer['context']}...")
    print("\n\n")
