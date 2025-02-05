from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.storage import StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
import chromadb
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_KEY')
os.environ['OPENAI_API_KEY'] = api_key

def create_index():
    Settings.llm = OpenAI(model='gpt-4')
    Settings.embed_model = OpenAIEmbedding()
    Settings.chunk_size = 1024
    
    chroma_client = chromadb.Client()
    chroma_collection = chroma_client.create_collection("my_docs")
    
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    parser = SimpleNodeParser.from_defaults(
        chunk_size=1024,
        chunk_overlap=20
    )
    
    documents = SimpleDirectoryReader('./docs').load_data()
    nodes = parser.get_nodes_from_documents(documents)
    
    return VectorStoreIndex(
        nodes,
        storage_context=storage_context
    )

def main():
    try:
        index = create_index()
        query_engine = index.as_query_engine(
            similarity_top_k=3,
            response_mode="compact"
        )

        response = query_engine.query(
            "What's the main topic of these documents?"
        )
        print(response)
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()