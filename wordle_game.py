import random

# Lista simple de palabras de 5 letras
word_list = ['apple', 'brave', 'crane', 'grape', 'plumb', 'shine', 'smart', 'plant']
secret_word = random.choice(word_list)

def give_feedback(guess, secret):
    feedback = ""
    for i in range(5):
        letter = guess[i].upper()
        if guess[i] == secret[i]:
            feedback += f"[✓] {letter}   "
        elif guess[i] in secret:
            feedback += f"[!] {letter}   "
        else:
            feedback += f"[X] {letter}   "
    return feedback.strip()

print("🎮 Bienvenido a Wordle versión consola (sin colores)!")
print("Adivina la palabra de 5 letras. Tienes 6 intentos.\n")

for attempt in range(1, 7):
    guess = input(f"Intento {attempt}/6: ").lower()

    if len(guess) != 5 or not guess.isalpha():
        print("❗ Por favor, escribe una palabra válida de 5 letras.\n")
        continue

    if guess not in word_list:
        print("❗ Esa palabra no está en la lista.\n")
        continue

    feedback = give_feedback(guess, secret_word)
    print("Resultado:")
    print(feedback + "\n")

    if guess == secret_word:
        print("🎉 ¡Adivinaste la palabra! ¡Felicidades!")
        break
else:
    print(f"❌ Se acabaron los intentos. La palabra era: {secret_word.upper()}")
