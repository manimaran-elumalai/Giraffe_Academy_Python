#secret_word, guess_word, guess_count, guess_limit, out_of_guesses are all variables
secret_word = "Camel"
guess_word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess_word != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess_word = input("Can you guess:")            
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
        print("Hey, no more guess - YOU LOSE ")
else:
        print("Hurray... YOU WIN")

