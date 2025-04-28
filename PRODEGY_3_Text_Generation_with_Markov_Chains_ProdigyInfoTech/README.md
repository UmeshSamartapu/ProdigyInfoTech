
# Text Generation with Markov Chains

This project implements a simple text generation algorithm using **Markov Chains**.  
It creates a statistical model that predicts the probability of the next word based on the previous word(s).

---

## 📂 Project Structure

```
├── main.py          # Main script to train the model and generate text
├── markov.py        # MarkovChain class for training and text generation
├── input.txt        # Input text file used for training
└── README.md        # Project documentation
```

---

## 🚀 How It Works

- **Training**:  
  The model reads `input.txt` and learns the word transitions using a Markov Chain of a given order (default is `2` for trigrams).

- **Text Generation**:  
  After training, the model generates a sequence of words based on the learned transitions.

---

## 🛠️ How to Run

1. Make sure you have Python installed (`3.6+` recommended).
2. Clone/download the project.
3. Place your input text in `input.txt`.
4. Run the program:

```bash
python main.py
```

You will see generated text printed in the terminal.

---

## 📄 Files Explained

- **main.py**  
  - Loads and reads the input text.
  - Trains the Markov model.
  - Generates and prints random text.

- **markov.py**  
  - Defines the `MarkovChain` class.
  - Handles model training and text generation.

- **input.txt**  
  - Sample input text to train the Markov model.  
  - You can replace this with your own text to generate different results.

---

## ⚙️ Customize

- **Change the order of the model**:  
  In `main.py`, modify:

  ```python
  markov = MarkovChain(order=2)  # Change 2 to 1 (bigram) or any other number
  ```

- **Change the number of generated words**:  
  Modify the `max_words` parameter:

  ```python
  generated = markov.generate(max_words=50)  # Generate 50 words
  ```

---

## 📚 Example Output

```
Training Markov model...

Generated Text:

Once upon a time there was a brave knight who fought dragons and saved kingdoms. The knight traveled across mountains and rivers. Every town he visited, people greeted him with joy.
```

*(Output will vary each time based on randomness.)*

---

## ✨ Future Improvements

- Character-level Markov chain.
- Add randomness control (e.g., using seeds).
- GUI for text generation.
- Save the trained model for reuse.

---

## 📜 License

This project is open-source and free to use under the MIT License.

## 👨‍💻 Author

**Umesh Samartapu**  

## 📫 Let's Connect

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umeshsamartapu/)
[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://x.com/umeshsamartapu)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:umeshsamartapu@gmail.com)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/umeshsamartapu/)
[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20Me%20a%20Coffee-FBAD19?style=flat-square&logo=buymeacoffee&logoColor=black)](https://www.buymeacoffee.com/umeshsamartapu)

---

🔥 Always exploring new technologies and solving real-world problems with code!
