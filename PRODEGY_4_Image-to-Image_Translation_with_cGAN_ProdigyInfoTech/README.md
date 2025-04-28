# Image-to-Image-Translation-with-cGAN

## Overview
The Image-to-Image Translation with cGAN project implements a deep learning model called pix2pix that learns to map an input image to a corresponding output image.
This is achieved using a Conditional Generative Adversarial Network (cGAN).

# Features
- Learns direct mappings between input and output images.

- Uses adversarial training to generate realistic outputs.

- Supports custom datasets for flexible applications.

- Checkpoint saving for models during training.

- Visualizes intermediate training results.

# Tools & Technologies
- **Deep Learning:** TensorFlow, Keras

- **GAN Framework:** Conditional GAN (cGAN)

- **Data Handling**: NumPy, OpenCV

- **Visualization:** Matplotlib

- **Version Control:** Git, GitHub

- **Training Progress:** tqdm

# Project Structure "Code"
  
```bash
Image-to-Image-Translation/
├── facades/             # Dataset folders
│   ├── train/
│   └── test/
├── models/
│   ├── generator.py     # U-Net Generator
│   ├── discriminator.py # PatchGAN Discriminator
├── utils/
│   └── data_load.py     # TF Dataset loading and preprocessing
├── training_checkpoints/
│   └── 
├── Image_to_Image_Translation_with_cGAN.ipynb              # Training logic
├── requirements.txt     # Dependencies
```
setup the structure in the colab and run the .ipynb file 

# Run code in colab

```bash
1.Open Google Drive, setup the above project directory as it is.
2.Open Google Colab.
3.Open Image_to_Image_Translation_with_cGAN.ipynb
4.It will open and you can run the cells one by one by clicking Shift + Enter
```
# Project Structure "Application"

```bash
📂 Image-to-Image-Translation
├── 📂 assets
│   ├── app UI.png
│   ├── create_model.py
│   ├── input.png
│   └── output.png
├── 📂 model
│   └── .gitignore
├── 📂 Results
│   ├── app UI.png
│   ├── input.png
│   └── output.png
├── 📂 templates
│   └── index.html
├── 📂 uploads
│   └── Screenshot 2025-04-28 235647.png
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

# Run Application:
```bash
python app.py
```
 
# Dataset 
download it from online
[pix2pix Facades Dataset](https://www.kaggle.com/datasets/sabahesaraki/pix2pix-facades-dataset)

## 📫 Let's Connect

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umeshsamartapu/)
[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://x.com/umeshsamartapu)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:umeshsamartapu@gmail.com)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/umeshsamartapu/)
[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20Me%20a%20Coffee-FBAD19?style=flat-square&logo=buymeacoffee&logoColor=black)](https://www.buymeacoffee.com/umeshsamartapu)

---

🔥 Always exploring new technologies and solving real-world problems with code!


