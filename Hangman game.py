import random
words = ["apple", "banana", "grapes", "orange", "mango"]
word = random.choice(words)
guessed = []
display = ["_"] * len(word)
chances = 6
print("Welcome to Hangman Game")
while chances > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Guessed letters:", guessed)
    print("Chances left:", chances)
    letter = input("Enter a letter: ").lower()

    if letter in guessed:
        print("Already guessed!")
        continue

    guessed.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
        print("Correct guess!")
    else:
        chances -= 1
        print("Wrong guess!")

if "_" not in display:
    print("\nYou won! The word is:", word)
else:
    print("\n Game over! The word was:", word)
