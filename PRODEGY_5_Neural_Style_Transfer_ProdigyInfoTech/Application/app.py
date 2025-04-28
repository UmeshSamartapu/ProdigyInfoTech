from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from style_transfer import run_style_transfer

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
OUTPUT_PATH = "static/output.jpg"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/transfer")
async def transfer_style(request: Request, content_image: UploadFile = File(...), style_image: UploadFile = File(...)):
    content_path = os.path.join(UPLOAD_DIR, "content.jpg")
    style_path = os.path.join(UPLOAD_DIR, "style.jpg")

    # Save uploaded images properly
    content_data = await content_image.read()
    style_data = await style_image.read()

    if not content_data or not style_data:
        return templates.TemplateResponse("index.html", {"request": request, "error": "Please upload both images."})

    with open(content_path, "wb") as f:
        f.write(content_data)
    with open(style_path, "wb") as f:
        f.write(style_data)

    # Check if files are valid images
    from PIL import Image, UnidentifiedImageError
    try:
        Image.open(content_path).verify()
        Image.open(style_path).verify()
    except UnidentifiedImageError:
        return templates.TemplateResponse("index.html", {"request": request, "error": "Uploaded files are not valid images."})

    # Run the style transfer
    run_style_transfer(content_path, style_path, OUTPUT_PATH)

    return templates.TemplateResponse("index.html", {"request": request, "result_image": OUTPUT_PATH})
