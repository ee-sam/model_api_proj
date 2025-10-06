from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from contextlib import asynccontextmanager

import os
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        # pyinstaller bundle (exe)
        return os.path.dirname(sys.executable)
    else:
        # normal .py env
        return os.path.dirname(os.path.abspath(__file__))

base_path = get_base_path()
model_dir = os.path.join(base_path, '..', 't5_model', 't5_small')
model_dir = os.path.abspath(model_dir)

# [DEBUG]
# print(f"model path: {model_dir}")

# init global variables
tokenizer = None
model = None

# lifespan manager replaces deprecated @app.on_event('startup')
@asynccontextmanager
async def lifespan(app: FastAPI):
    global tokenizer, model
    print(f"Load model from: {model_dir}")
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
    print(f"Model loaded successfully")
    yield
    print(f"Teardown")

app = FastAPI(title="Summarization API", version="1.0", lifespan=lifespan)

# input schema
class SummarizeRequest(BaseModel):
    input_text: str
    min_length: int = 80
    max_length: int = 150
    length_penalty: float = 0.5
    temperature: float = 1.0
    top_p: float = 1.0

# output schema
class SummaryResponse(BaseModel):
    original_length: int
    summary_length: int
    summary: str

# summarization endpoint
@app.post("/summarize", response_model=SummaryResponse)
def summarize_text(request: SummarizeRequest):
    global tokenizer, model
    if tokenizer is None or model is None:
        return {"error":"Model not loaded"} ## [TO_FIX] Shud changed to follow response_model? Wat abt progress update?
    inputs = tokenizer(request.input_text, return_tensors="pt", truncation=True)
    print(f"Generating summary")
    outputs = model.generate(
        **inputs,
        max_length = request.max_length,
        min_length = request.min_length,
        length_penalty = request.length_penalty,
        temperature = request.temperature,
        top_p = request.top_p
    )
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    pass
    return SummaryResponse(
        original_length=len(request.input_text),
        summary_length=len(summary),
        summary=summary
    )


# health-check
@app.get("/")
def health_check():
    return {"status": "ok", "message": "T5 summarization service is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("summarizer:app", host="127.0.0.1", port=8080, reload=True)
    # uvicorn.run("summarizer:app", host="0.0.0.0", port=8080)