import pandas as pd
import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

POSTS_XLSX = "posts.xlsx"
POSTS_CSV = "posts.csv"
INDEX_FILE = "post_index.faiss"

# Build and save the FAISS index
def build_index():
    if not os.path.exists(POSTS_XLSX):
        raise FileNotFoundError("posts.xlsx not found.")

    df = pd.read_excel(POSTS_XLSX)
    if df.empty or 'post_text' not in df.columns:
        raise ValueError("Invalid posts.xlsx: No 'post_text' column or it's empty.")

    embeddings = model.encode(df['post_text'].tolist())
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    df.to_csv(POSTS_CSV, index=False)
    faiss.write_index(index, INDEX_FILE)
    print("Index and CSV built successfully.")

# Retrieve similar post
def get_similar_post(text):
    if not os.path.exists(POSTS_CSV) or not os.path.exists(INDEX_FILE):
        build_index()

    df = pd.read_csv(POSTS_CSV)
    if df.empty:
        raise ValueError("posts.csv is empty.")

    index = faiss.read_index(INDEX_FILE)
    embedding = model.encode([text])
    D, I = index.search(np.array(embedding), 1)

    if len(I[0]) == 0 or I[0][0] >= len(df):
        return "No similar post found."
    
    return df.iloc[I[0][0]]['post_text']
