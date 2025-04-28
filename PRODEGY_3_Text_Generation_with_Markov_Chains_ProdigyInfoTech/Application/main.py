# main.py

from markov import MarkovChain

def read_input_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    text = read_input_file("input.txt")

    print("Training Markov model...")
    markov = MarkovChain(order=2)  # You can change the order (1 = bigram, 2 = trigram)
    markov.train(text)

    print("\nGenerated Text:\n")
    generated = markov.generate(max_words=50)
    print(generated)

if __name__ == "__main__":
    main()
