from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .models import TextGenerator
import time
import os

app = FastAPI(title="GPT-2 Text Generator")

# Mount static files
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

# Setup templates
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

# Initialize model
generator = None

@app.on_event("startup")
async def startup_event():
    global generator
    try:
        # Ensure the model path is correct
        model_path = os.path.join(os.path.dirname(__file__), "..", "gpt2-finetuned")
        generator = TextGenerator(model_path)
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {str(e)}")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    if generator is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate_text(
    request: Request,
    prompt: str = Form(...),
    max_length: int = Form(100),
    temperature: float = Form(0.7),
    top_k: int = Form(50),
    top_p: float = Form(0.9)
):
    if generator is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    start_time = time.time()
    
    generated_text = generator.generate_text(
        prompt,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p
    )
    
    processing_time = round(time.time() - start_time, 2)
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "prompt": prompt,
        "generated_text": generated_text,
        "processing_time": processing_time,
        "max_length": max_length,
        "temperature": temperature,
        "top_k": top_k,
        "top_p": top_p
    })