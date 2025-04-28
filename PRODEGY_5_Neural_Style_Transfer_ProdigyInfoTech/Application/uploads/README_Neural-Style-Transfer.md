
# Prodigy Infotech - Task 05: Neural Style Transfer 🎨

This project is a submission for **Prodigy Infotech's Internship Program**. 
The task was to perform **Neural Style Transfer** — applying the artistic style of one image (like a famous painting) onto another image (the content image) using deep learning.

Both a Jupyter notebook for experimentation and a **Web Application** for user-friendly interaction are included.

---

## 📁 Project Structure

```
Neural_Style_Transfer/
│
├── Neural Style Transfer.ipynb       # Main notebook to run and experiment
│
├── content_image/                    # Directory for content images
│   └── content2.jpg
│
├── style_image/                      # Directory for style images
│   ├── style1.jpg
│   └── style2.jpg
│
├── output/                           # Output directory for generated images
│   └── (generated images saved here)
│
Web_Application/
│
├── app.py                            # Main FastAPI web app
├── nst_utils.py                      # Helper functions for NST
├── requirements.txt                  # List of required Python libraries
├── style_transfer.py                 # Neural style transfer logic
│
├── assets/                           # Extra assets
│   ├── dir.txt
│   └── run.txt
│
├── Results/                          # Screenshots and Results
│   └── App UI.png
│
├── static/                           # Static files (CSS, JS if needed)
├── templates/
│   └── index.html                    # Web app frontend
├── uploads/                          # User-uploaded content and style images
│   ├── content.jpg
│   └── style.jpg
```

---

## 🚀 Features

- Transfer the artistic style of one image onto another using **VGG19** pretrained model.
- Fine control over **content weight** and **style weight**.
- Intermediate outputs saved during optimization.
- Web Application to **upload your own images** and get a styled output easily.
- Saves output images and a GIF showing the progress.

---

## 🛠️ How to Run

### 1. Notebook Version (Google Colab or Local)

- Upload the directory structure to Google Drive.
- Open `Neural Style Transfer.ipynb` in Colab.
- Mount your Google Drive:
  ```python
  from google.colab import drive
  drive.mount('/content/drive')
  ```
- Install dependencies:
  ```bash
  !pip install torch torchvision pillow imageio
  ```
- Run the cells to start style transfer.

### 2. Web Application (Computer)

- Navigate to the web app folder.
- Install required packages:
  ```bash
  pip install -r requirements.txt
  ```
- Run the web server:
  ```bash
  python app.py
  ```
- Open your browser at `http://127.0.0.1:5000/`.
- Upload a **content image** and a **style image** to generate your styled image.

---

## 📦 Libraries and Frameworks Used

- **PyTorch** (Deep Learning Framework)
- **TorchVision** (Pretrained VGG19 Model)
- **PIL** (Image Processing)
- **ImageIO** (GIF generation)
- **Flask / FastAPI** (Web Application)
- **HTML/CSS** (Frontend)

---

## 📸 Screenshots

### Web App Interface
![App UI](Results/App%20UI.png)

---

## ✨ Output Samples

- Saved output images at different iterations (every 100 iterations).
- Final stylized image.
- A GIF showing the transformation progress.

---

## 🤝 Credits

- Inspired by the paper ["A Neural Algorithm of Artistic Style"](https://arxiv.org/abs/1508.06576) by Leon A. Gatys et al.
- Pretrained model: **VGG19** from torchvision.

---

## 🔥 Future Improvements

- Support multiple style blending.
- Faster style transfer with lightweight models like **Fast Neural Style Transfer**.
- Deploy the web app online using **Render** or **Heroku**.

---

## 🧑‍💻 Author

**Amit Prajapati**  
Student at Avanthi Institute of Engineering and Technology

---

> _"Turn your creativity into code."_ 🎨
