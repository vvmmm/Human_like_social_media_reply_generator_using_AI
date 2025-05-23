###################### try 1 ################################################################################


# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from datetime import datetime
# from fastapi.middleware.cors import CORSMiddleware


# # Import your models and generator function
# from app.models import PostRequest, ReplyResponse
# from app.generator import generate_reply
# from app.database import collection  # <- Add this to save to MongoDB

# app = FastAPI()


# origins = [
#     "http://localhost",
#     "http://localhost:8501",  # Default Streamlit port
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/reply", response_model=ReplyResponse)
# async def generate_social_reply(request: PostRequest):
#     if not request.post_text:
#         raise HTTPException(status_code=400, detail="Post text is required")

#     try:
#         reply = generate_reply(request.platform, request.post_text)

#         # Await async insert
#         await collection.insert_one({
#             "platform": request.platform,
#             "post_text": request.post_text,
#             "generated_reply": reply,
#             "timestamp": datetime.utcnow()
#         })

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

#     return {
#         "generated_reply": reply,
#         "timestamp": datetime.utcnow()
#     }

# @app.get("/")
# def root():
#     return {"message": "FastAPI is working"}


###################### try 2 ################################################################################



### UPDATED main.py ###

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from app.models import PostRequest, ReplyResponse
from app.generator import generate_reply
from app.database import collection

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/reply", response_model=ReplyResponse)
async def generate_social_reply(request: PostRequest):
    if not request.post_text:
        raise HTTPException(status_code=400, detail="Post text is required")

    try:
        reply = generate_reply(request.platform, request.post_text, request.tone if hasattr(request, 'tone') else None)
        await collection.insert_one({
            "platform": request.platform,
            "post_text": request.post_text,
            "generated_reply": reply,
            "tone": request.tone if hasattr(request, 'tone') else None,
            "timestamp": datetime.utcnow()
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"generated_reply": reply, "timestamp": datetime.utcnow()}

@app.get("/history")
def get_history():
    try:
        docs = list(collection.find().sort("timestamp", -1).limit(20))
        for doc in docs:
            doc['_id'] = str(doc['_id'])
        return docs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "FastAPI is working"}
