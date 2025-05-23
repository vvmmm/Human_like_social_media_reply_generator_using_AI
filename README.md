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

## 📦 Installation dependencies
```bash
pip install -r requirements.txt

## Setup Environment Variables

```bash
GEMINI_API_KEY=your_gemini_api_key
MONGO_URI=your_mongodb_connection_string

##🚀 Running the App Locally

###Backend (FastAPI)
```bash
uvicorn app.main:app --reload

###Frontend (Streamlit)
```bash
streamlit run streamlit_app.py

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
