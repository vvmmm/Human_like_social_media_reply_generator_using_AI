# Human_like_social_media_reply_generator_using_AI
Human-like Social Media Reply Generator  A FastAPI backend and Streamlit frontend application that generates context-aware, human-like replies to social media posts using Google Gemini AI. It supports multiple platforms (Twitter, LinkedIn, Instagram), stores conversation history in MongoDB, and enables seamless, real-time interaction .

# 🤖 Human-like Social Media Reply Generator

A full-stack AI-powered application that automatically generates human-like, context-aware replies to social media posts using Google's Gemini model and MongoDB as a knowledge base. Ideal for marketers, content creators, and community managers looking to streamline engagement.

---

## 🌐 Live Demo

- 🔗 **Streamlit App:** https://humanlikesocialmediareplygeneratorusingai-bypugbpqrqvhkpvp2rgb.streamlit.app/
- 🔗 **FastAPI Endpoint:** https://human-like-social-media-reply-generator-6fmj.onrender.com/reply

---

## 🚀 Features

- 💬 Generate human-like replies for platforms like Twitter, LinkedIn, and Instagram.
- 📚 Leverages similar posts from a MongoDB-powered knowledge base.
- 🧠 Powered by Google's Gemini 2.0 Flash model for fast, natural-sounding replies.
- 🖥️ Built with FastAPI (backend) and Streamlit (frontend).
- 🔍 Retrieval-Augmented Generation (RAG) for context-aware response generation.

---

## 🧱 Tech Stack

| Layer       | Technology               |
|-------------|--------------------------|
| Frontend    | Streamlit                |
| Backend     | FastAPI                  |
| AI Model    | Google Gemini (via API)  |
| Database    | MongoDB Atlas + ChromaDB |
| Deployment  | Render (FastAPI), Streamlit Cloud |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vvmmm/Human_like_social_media_reply_generator_using_AI.git
cd social-media-reply-generator
```

## 📦 Installation dependencies
```bash
pip install -r requirements.txt
```
## Setup Environment Variables

```bash
GEMINI_API_KEY=your_gemini_api_key
MONGO_URI=your_mongodb_connection_string
```

##🚀 Running the App Locally

###Backend (FastAPI)
```bash
uvicorn app.main:app --reload
```

###Frontend (Streamlit)
```bash
streamlit run streamlit_app.py
```
##🌍 Deployment Guide

###Backend (Render)
Push your repo to GitHub

Go to Render.com

Create a New Web Service

Connect your GitHub repo

Use the following start command:

bash
Copy
Edit
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 🤖 Explanation of Human-like Reply Generation Approach

To ensure the AI-generated replies feel **authentic, context-aware, and human-like**, we adopted the following strategy:

- **1. Contextual Understanding via RAG (Retrieval-Augmented Generation):**  
  The input post is matched against a knowledge base of past social media content using ChromaDB embeddings. Similar posts are retrieved to provide the AI with examples of how humans typically respond in related contexts.

- **2. Gemini Language Model:**  
  We use Google's Gemini Flash model, optimized for both speed and natural language understanding. The model is prompted not just with the current post, but also with semantically similar examples, enhancing the realism of its responses.

- **3. Platform-Aware Styling:**  
  The system considers the selected platform (Twitter, LinkedIn, Instagram) to tailor tone and brevity. For instance, replies on LinkedIn are more formal, while Twitter replies are concise and informal.

- **4. Instruction-Tuned Prompts:**  
  Prompts provided to the language model are carefully crafted to steer the AI toward:
  - Emotional nuance (e.g., empathetic, excited, congratulatory)
  - Use of emojis when appropriate
  - Avoiding robotic or generic responses

- **5. Future-Ready Design:**  
  The architecture supports expanding into **tone/style customization** (e.g., professional vs. humorous), enabling replies to be further personalized.

This combination of **retrieval-based grounding** and **prompt engineering with a powerful language model** ensures that replies are not just relevant—but feel like something a real person would write.
