from haystack.nodes.reader.farm import FARMReader

question="How much music can this hold?"
context="An MP3 is about 1MB/minute so about 6000 hours depending on file size"


model_ckpt="deepset/minilm-uncased-squad2"
max_seq_length,doc_stride=384,128
reader=FARMReader(model_name_or_path=model_ckpt,progress_bar=False,max_seq_len=max_seq_length,doc_stride=doc_stride,return_no_answer=True)

print(reader.predict_on_texts(question=question,texts=[context],top_k=1))