import random
import hangman_words
import hangman_art
print(hangman_art.logo)
chosen=random.choice(hangman_words.word_list)
WrongAns=0
Check=True
blank = ["_"] * len(chosen)
while Check:
    check=False
    gl = input("Guess a letter of the word:\n").lower()
    if gl in blank:
        print("You have already guessed this letter")
    index = 0
    for i in chosen:
        if i == gl:
            blank[index] = gl
            check=True
        index += 1

    if check == False:
        WrongAns+=1
        print(f"OOPS!! , Wrong guess \nYou have {7-WrongAns} tries remaining")

    print(f"CURRENT STATE OF GUESSES:\n{blank}")
    print(hangman_art.stages[7-WrongAns])

    if WrongAns==7:
        Check=False

    if"_" not in blank:
        print("CONGRATULATIONS!! , You have WON!")

print("\nYOU LOST THE GAME!!")
print(f"The word was:\n{chosen}")