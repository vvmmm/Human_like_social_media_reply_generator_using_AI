import google.generativeai as genai
from app.config import GEMINI_API_KEY
from app.utils import get_similar_post

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-exp")

def generate_reply(platform: str, post_text: str, tone: str = None) -> str:
    similar = get_similar_post(post_text) or "No similar posts found."
    
    tone_text = f"Tone: {tone}" if tone else "Tone: Neutral"
    
    prompt = f"""
Platform: {platform}
{tone_text}

Original Post:
{post_text}

Similar Post from Knowledge Base:
{similar}

Now write a human-like, context-aware reply that fits the tone and platform.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Sorry, I couldn't generate a reply due to an error: {str(e)}"
