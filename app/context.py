import os

from llama_index import ServiceContext
from llama_index.llms.clarifai import Clarifai


def create_base_context():
    MODEL_URL = os.getenv("MODEL_URL")
    return ServiceContext.from_defaults(llm_model=Clarifai(model_url=MODEL_URL))
