import torch
from transformers import pipeline

generate_text = pipeline(model="databricks/dolly-v2-12b",
                         torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")

generate_text(
    """What do you call something that has four wheels and that can move?""")
