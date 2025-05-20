# Create file: chatbot.py
# import openai
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/chat/{message}")
# async def chat(message: str):
#     response = openai.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": message}]
#     )
#     return {"reply": response.choices[0].message.content}
# import os
# import openai
# from fastapi import FastAPI
# from dotenv import load_dotenv

# load_dotenv()  # Load .env file

# openai.api_key = os.getenv("secret key")

# app = FastAPI()

# @app.get("/chat/{message}")
# async def chat(message: str):
#     response = openai.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": message}
#         ]
#     )
#     return {"reply": response.choices[0].message.content}


# # Run with: uvicorn chatbot:app --reload
# 
# No paid API needed - use FREE Hugging Face models
from transformers import pipeline

# Free AI model
# Create this file today: ai_project.py

from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Load free AI model
sentiment_analyzer = pipeline("sentiment-analysis")

@app.get("/")
def home():
    return {"message": "My first AI API!"}

@app.get("/analyze/{text}")
def analyze(text: str):
    result = sentiment_analyzer(text)
    return {"result": result}