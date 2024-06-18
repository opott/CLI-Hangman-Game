word = []
word = input("Enter a word: ")
word = word.upper()

progress = []
chances = 5
needed = len(word)

for i in word:
     progress.append("_")

def main():
    global chances
    global needed

    guess = input("Enter a letter: ")
    guess = guess.upper()
    if guess in word:
        print("Correct!")
        progress[word.index(guess)] = guess
        needed = needed - 1
    else:
        print("Incorrect!")
        chances = chances - 1

    print(progress)

    if chances != 0:
        if needed == 0:
             print("You win!")
             print(word)
        else: 
            return main()
    else:
        print("You lose!")
        print(word)

main()