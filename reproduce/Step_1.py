import os
import json
import time

from PathCoRAG import PathCoRAG
from PathCoRAG.llm.openai import gpt_4o_mini_complete, openai_embed
from PathCoRAG.llm.ollama import ollama_model_complete, ollama_embed
from PathCoRAG.utils import EmbeddingFunc


def insert_text(rag, file_path):
    # with open(file_path, mode="r") as f:
    #     unique_contexts = json.load(f)

    retries = 0
    max_retries = 3
    while retries < max_retries:
        try:
            # rag.insert(unique_contexts)
            with open(file_path, "r", encoding="utf-8") as f:
                rag.insert(f.read())
            break
        except Exception as e:
            retries += 1
            print(f"Insertion failed, retrying ({retries}/{max_retries}), error: {e}")
            time.sleep(10)
    if retries == max_retries:
        print("Insertion failed after exceeding the maximum number of retries")


cls = "podcast"
WORKING_DIR = f"../{cls}"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = PathCoRAG(
    working_dir=WORKING_DIR,
    embedding_func=openai_embed,
    llm_model_func=gpt_4o_mini_complete,
    # llm_model_func=gpt_4o_complete
)

# insert_text(rag, f"../datasets/unique_contexts/{cls}_unique_contexts.json")
insert_text(rag, f"../datasets/{cls}_transcript.txt")