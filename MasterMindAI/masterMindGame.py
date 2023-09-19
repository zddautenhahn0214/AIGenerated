# Code written by ChatGPT with Zach as the prompter
# This code simulates a game of Mastermind where the player tries to guess a secret code chosen by the computer.

import random

def generate_code():
    return [random.randint(1, 6) for _ in range(4)]

def provide_feedback(guess, code):
    hits = sum(g == c for g, c in zip(guess, code))
    pseudo_hits = sum(min(guess.count(c), code.count(c)) for c in set(guess)) - hits
    return hits, pseudo_hits

def main():
    code = generate_code()
    attempts = 0

    while True:
        guess = input("Enter your guess (4 numbers from 1 to 6, separated by spaces): ").strip().split()
        guess = [int(g) for g in guess]
        hits, pseudo_hits = provide_feedback(guess, code)
        print(f"Hits: {hits}, Pseudo-hits: {pseudo_hits}")
        attempts += 1

        if hits == 4:
            print(f"Congratulations! You've guessed the code {code} in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
