import pandas as pd
import requests

df = pd.read_excel("posts.xlsx")

for _, row in df.iterrows():
    payload = {
        "platform": row["platform"],
        "post_text": row["post_text"]
    }
    response = requests.post("http://localhost:8000/reply", json=payload)
    print(response.json())
