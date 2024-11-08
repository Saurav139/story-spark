from openai import OpenAI

import numpy as np
#from config import OPEN_AI_KEY
import chromadb
from chromadb.config import Settings

# Set your OpenAI API key
client = OpenAI(api_key = OPEN_API_KEY)


# In-memory storage for embeddings
chroma_client = chromadb.PersistentClient(path="./chromastore")

# Create a collection to store the story segments
story_collection = chroma_client.get_or_create_collection(name="Story1")

def generate_embeddings(text_segments):
    """Generate embeddings for a list of text segments using OpenAI."""
    embeddings = []
    for text in text_segments:
        response = client.embeddings.create(input = [text], model='text-embedding-3-small').data[0].embedding
        embeddings.append(response)
    return embeddings

def add_to_chromadb(text_segments, embeddings):
    """Add text segments and their embeddings to the ChromaDB collection."""
    # Flatten list of lists and wrap each segment
    #print(text_segments)
    flattened_segments=[segment for segment in text_segments]

    #print(flattened_segments)
    # Generate unique IDs for each document
    ids = [f"doc_{i}" for i in range(len(flattened_segments))]
    #print(ids)
    # Upsert documents with unique IDs
    
    story_collection.upsert(
        documents=flattened_segments,  # Flattened list of text segments with triple quotes
        ids=ids                         # Unique IDs for each document
    )
    return story_collection



def retrieve_similar_segments(query, top_k=3):
    """Retrieve similar segments based on the query using ChromaDB."""
    # Generate embedding for the query
    # query_embedding =  client.embeddings.create(input = [query], model='text-embedding-3-small').data[0].embedding
    # Search ChromaDB for similar embeddings

    results = story_collection.query(query_texts=["Vasona Lake is an amazing place"], n_results=top_k)
    

    #print(results["documents"],results["distances"])
    # Return the text of the top-k results
    return {doc:dist for doc,dist in zip(results["documents"][0],results["distances"][0])}