word_list = ["aardvark", "baboon", "camel"]
import random
word = input("choose word: ").lower()
chosen_word = random.choice(word_list)
count_word = int(len(chosen_word)) 
for letter in chosen_word:
    if letter == word:
        print("right")
    else:
        print("wrong")