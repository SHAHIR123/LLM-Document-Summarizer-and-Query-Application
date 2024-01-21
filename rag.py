# import qdrant_client
# from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.llms import Ollama
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
    SimpleDirectoryReader, 
    StorageContext
)

#semantic search
def semantic_search(query):
    if query is not None:
        
        documents = SimpleDirectoryReader('data').load_data()  
        llm = Ollama(model= "mistral", request_timeout=60.0, ) 

        service_context = ServiceContext.from_defaults(llm=llm, embed_model="local")

        index = VectorStoreIndex.from_documents(documents, service_context=service_context)
        query_engine = index.as_query_engine(similarity_top_k=5)
        response = query_engine.query(query)
        return response.response
    else:
        return "i am sorry. i cannot answer you for this due to some error in data"
    

#summarization 
def summarize(file):
    
    documents = SimpleDirectoryReader('data').load_data()
    llm = Ollama(model= "mistral", request_timeout=60.0)

    service_context = ServiceContext.from_defaults(llm=llm, embed_model="local")
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    query_engine = index.as_query_engine()
    response = query_engine.query("Could you Write a concise solid summary of the document ? Return your response which covers the key points of the text and does not miss anything important, approximately 20 sentence .")
    return response.response

