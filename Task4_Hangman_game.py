import random

word_list = ["apple", "banana", "orange", "strawberry", "kiwi", "pineapple"]
chosen_word = random.choice(word_list)
guessed_letters = set()
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")

while incorrect_guesses < max_attempts:
    display_word = ''.join(letter if letter in guessed_letters else '_' for letter in chosen_word)
    print(display_word)
    
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.add(guess)
    
    if guess not in chosen_word:
        incorrect_guesses += 1
        print("Incorrect guess!")
    
    if set(chosen_word) == guessed_letters:
        print("Congratulations! You guessed the word:", chosen_word)
        break

else:
    print("Sorry, you've run out of attempts. The word was:",chosen_word)