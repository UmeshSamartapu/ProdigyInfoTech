
# Text Generation with GPT-2 (Colab & Web App)

This project demonstrates fine-tuning GPT-2 using a custom dataset and integrates both a Google Colab notebook for training and a FastAPI web app for serving the fine-tuned model to generate text from a given prompt.

# 📖 Project Overview

This project uses GPT-2, a transformer-based language model developed by OpenAI, and fine-tunes it on a custom dataset. The goal is to generate coherent and contextually relevant text based on any given prompt. The model is fine-tuned with LoRA (Low-Rank Adaptation) to use fewer parameters while retaining high performance.

# Key Features

- Fine-tune GPT-2 on a custom dataset.
- Use LoRA for lightweight fine-tuning.
- Supports dataset upload, preprocessing, and tokenization.
- Fine-tune with TensorBoard monitoring.
- Text Generation based on a user-provided prompt.
- Save the model in Hugging Face and PyTorch formats.
- Option to download the model as a ZIP file or upload to Google Drive.

# 🛠️ Tech Stack

- Python 3

- Hugging Face Transformers (transformers)

- PEFT (Parameter-Efficient Fine-Tuning) (peft)

- PyTorch (torch)

- TensorBoard (for training monitoring)
  
- Google Colab (for training)

- FastAPI (for the web app)

- Jinja2 Templates (for frontend)

- CSS (for styling the web app)

# 🚀 How to Run

## 1. Google Colab Notebook for Training GPT-2

You can train the GPT-2 model directly on Google Colab by following these steps:

### Install Dependencies
```bash
pip install -qU transformers==4.37.0 datasets==2.15.0 peft==0.6.0 accelerate==0.25.0
pip install -qU torch==2.1.0 tensorboard==2.15.0
```

### b. Upload and Preprocess Dataset
- Upload your data.txt file (where each line is a sample text).

- Convert it to Arrow format for optimized loading.
  
### c. Tokenize the Data
Use GPT-2's tokenizer to process your dataset with a max sequence length of 256 tokens.

### d. Train the Model
- Load the GPT-2 model and apply LoRA for fine-tuning.

- Monitor the training with TensorBoard.

### e. Save and Export the Model

- Save the fine-tuned model in Hugging Face format (gpt2-finetuned/) and PyTorch format (gpt2_weights.pt).

- Optionally, upload the model to Google Drive.

### f. Text Generation
```bash
print(generate_text("In a future where AI dominates"))
```
## 2. FastAPI Web App for Text Generation

After training the model, you can serve it through a FastAPI web app.

### a. Clone the repository:
```bash
git clone <repo-url>
cd gpt2-webapp
```
### b. Create a virtual environment:
```bash
python -m venv venv
```
### c. Activate the environment:
```bash
On Windows
venv\Scripts\activate
On mac
source venv/bin/activate
```
### d. Install Dependencies:
```bash
pip install -r requirements.txt
```
### e. Run the App:
```bash
uvicorn app.main:app --reload
```
### f. Visit the Web App:
```bash
Open your browser and go to: http://localhost:8000
```

---

## 📁 Application Structure

```
gpt2-webapp/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application routes
│   ├── models.py        # GPT-2 model loading and text generation logic
│   ├── static/          # Static files (e.g., CSS)
│   │   └── styles.css
│   └── templates/       # HTML templates (Jinja2)
│       └── index.html
├── assets/              # Additional resources (optional)
│   ├── dir.txt
│   ├── run.txt
│   └── sampleinput.txt
├── gpt2-finetuned/      # Fine-tuned GPT-2 model files
│   ├── adapter_config.json
│   ├── adapter_model.safetensors
│   ├── merges.txt
│   ├── special_tokens_map.json
│   ├── tokenizer_config.json
│   ├── training_args.bin
│   └── vocab.json
├── requirements.txt     # Python dependencies
└── README.md             # Project documentation
```

---

## 📋 Sample Input

> **Science Topic:**
> 
> Quantum computing is an area of computing focused on developing computer technology based on the principles of quantum theory, which explains the nature and behavior of energy and matter on the quantum level. Quantum computers use quantum bits or qubits which can exist in multiple states simultaneously, unlike classical binary bits. This allows quantum computers to process massive amounts of data and solve complex problems much faster than traditional computers. Major companies like IBM, Google, and Microsoft are investing heavily in quantum computing research.

---

## 📦 Key Files

- **app/main.py**: FastAPI app handling routes and request processing.
- **app/models.py**: Model class (`TextGenerator`) for loading GPT-2, PEFT adapter, and generating text.
- **gpt2-finetuned/**: Fine-tuned GPT-2 model and adapter weights.
- **requirements.txt**: All necessary Python libraries for the project.
- **templates/index.html**: Frontend page to enter prompts and view generated outputs.
- **static/styles.css**: Basic CSS for styling the frontend.

---

## ✨ Features

- Easy deployment-ready FastAPI structure.
- Fine-tuned GPT-2 text generation using **low-resource adapters** (PEFT).
- Supports adjusting model inference parameters (length, temperature, top_k, top_p).
- Displays inference time.
- Clean and simple UI for interaction.

---

## 📢 Notes

- Make sure the `gpt2-finetuned` folder is correctly placed in the project root.
- CUDA device is automatically selected if available for faster generation.
- The app is designed for educational and demonstration purposes; you can easily extend it to a production deployment (e.g., using Docker, Render, or Azure).

---

## 📫 Let's Connect

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umeshsamartapu/)
[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://x.com/umeshsamartapu)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:umeshsamartapu@gmail.com)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/umeshsamartapu/)
[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20Me%20a%20Coffee-FBAD19?style=flat-square&logo=buymeacoffee&logoColor=black)](https://www.buymeacoffee.com/umeshsamartapu)

---

🔥 Always exploring new technologies and solving real-world problems with code!
