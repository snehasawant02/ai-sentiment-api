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
import os
import uvicorn
from fastapi import FastAPI, Request
from transformers import pipeline
from fastapi.staticfiles import StaticFiles
app = FastAPI(title="AI Application")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
# Load free AI models
sentiment_analyzer = pipeline("sentiment-analysis")
text_generator = pipeline("text-generation", model="gpt2")
@app.get("/")
async def root():
    # Redirect to our HTML page
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/static/index.html")

@app.get("/analyze/{text}")
def analyze(text: str):
    result = sentiment_analyzer(text)
    return {"result": result}

@app.get("/generate/{prompt}")
def generate(prompt: str, max_length: int = 50):
    result = text_generator(prompt, max_length=max_length)
    return {"generated_text": result[0]["generated_text"]}

if __name__ == "__main__":  
    uvicorn.run("chatbot:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
