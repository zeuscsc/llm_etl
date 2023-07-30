from sentence_transformers import SentenceTransformer
from .llm import LLM_Base
model:SentenceTransformer=None
class Bert(LLM_Base):
    def __init__(self):
        if model is None:
            model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    def get_embedding(self,sentences:str):
        return model.encode(sentences)