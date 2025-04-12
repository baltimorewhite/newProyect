import random

word_list = ["stare", "phone", "pizza","seven","happy","house","mouse","watch"]
answer = random.choice(word_list)

def get_clue(ans, guess):
    clue = ""
    for idx, letter in enumerate(guess):
        if letter == ans[idx]:
            clue += "G"
        elif letter in ans:
            clue += "Y"
        else:
            clue += "-"
        return clue

for x in range (1,7):
    guess = input("Word? ")[0:5]
    print(get_clue(answer, guess), x)
    if answer == guess:
        break