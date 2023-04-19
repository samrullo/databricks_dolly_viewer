from datasets import get_dataset_config_names
domains=get_dataset_config_names('subjqa')
print(domains)
from datasets import load_dataset
subjqa=load_dataset("subjqa",name="electronics")
print(subjqa['train']['answers'][1])

import pandas as pd
dfs={split:dset.to_pandas() for split,dset in subjqa.flatten().items()}

for split,df in dfs.items():
    print(f"{split} has {df['id'].nunique()} questions")

from transformers import AutoTokenizer
model_ckpt="deepset/minilm-uncased-squad2"
tokenizer=AutoTokenizer.from_pretrained(model_ckpt)
question="How much music can this hold?"
context="An MP3 is about 1MB/minute so about 6000 hours depending on file size"
inputs=tokenizer(question,context,return_tensors="pt")

print(tokenizer.decode(inputs['input_ids'][0]))

import torch
from transformers import AutoModelForQuestionAnswering

model=AutoModelForQuestionAnswering.from_pretrained(model_ckpt)
with torch.no_grad():
    outputs=model(**inputs)
print(outputs)
start_logits=outputs.start_logits
end_logits=outputs.end_logits

start_idx=torch.argmax(start_logits)
end_idx=torch.argmax(end_logits)+1
answer_span=inputs['input_ids'][0][start_idx:end_idx]
answer=tokenizer.decode(answer_span)
print(f"Q : {question}")
print(f"A : {answer}")

from transformers import pipeline
pipe=pipeline("question-answering",model=model,tokenizer=tokenizer)
pipe(question=question,context=context,top_k=3)