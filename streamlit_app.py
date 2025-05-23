###################### try 1 ################################################################################

# import streamlit as st
# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()
# API_URL = "http://localhost:8000/reply"  # Or deployed URL

# st.set_page_config(page_title="Social Media Reply Generator", layout="centered")
# st.title("💬 Human-like Social Media Reply Generator")

# platform = st.selectbox("Select Platform", ["Twitter", "LinkedIn", "Instagram"])
# post_text = st.text_area("Paste the Social Media Post")

# if st.button("Generate Reply"):
#     if post_text.strip():
#         with st.spinner("Generating..."):
#             response = requests.post(API_URL, json={"platform": platform, "post_text": post_text})
#             if response.status_code == 200:
#                 st.success("Reply Generated")
#                 st.write(response.json()['generated_reply'])
#             else:
#                 st.error("Error: " + response.text)
#     else:
#         st.warning("Please enter a post.")



###################### try 2 ################################################################################


import streamlit as st
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = "http://localhost:8000/reply"  # Update if deployed

st.set_page_config(page_title="Social Media Reply Generator", layout="centered")
st.title("💬 Human-like Social Media Reply Generator")

# Input Section
platform = st.selectbox("🌐 Select Platform", ["Twitter", "LinkedIn", "Instagram"])
post_text = st.text_area("📝 Paste the Social Media Post", height=150)

# Submit Button
if st.button("✨ Generate AI Reply"):
    if post_text.strip():
        with st.spinner("🤖 Thinking..."):
            try:
                response = requests.post(API_URL, json={"platform": platform, "post_text": post_text})
                if response.status_code == 200:
                    data = response.json()
                    reply = data["generated_reply"]
                    timestamp = data.get("timestamp", str(datetime.utcnow()))

                    # Display Original Post
                    st.markdown("### 🧑‍💬 Original Post")
                    st.info(post_text)

                    # Display AI Reply
                    st.markdown("### 🤖 AI-Generated Reply")
                    st.success(reply)

                    # Optional timestamp
                    st.caption(f"🕒 Generated at: {timestamp}")

                else:
                    st.error("🚫 Error from FastAPI: " + response.text)
            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ Request failed: {e}")
    else:
        st.warning("⚠️ Please enter a post before generating a reply.")

