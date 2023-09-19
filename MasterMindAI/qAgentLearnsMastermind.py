# Code written by ChatGPT with Zach as the prompter
# This code trains a Q-learning agent to play Mastermind and allows the user to play against the agent.

import random
import numpy as np

N_COLORS = 6
CODE_LENGTH = 4
N_GAMES = 1000
EPSILON = 0.1
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9

def generate_code():
    return [random.randint(1, N_COLORS) for _ in range(CODE_LENGTH)]

def provide_feedback(guess, code):
    hits = sum(g == c for g, c in zip(guess, code))
    pseudo_hits = sum(min(guess.count(c), code.count(c)) for c in set(guess)) - hits
    # print(hits, pseudo_hits, '*')
    return hits, pseudo_hits

def state_index(state):
    guess, feedback = state
    guess_index = int(''.join(map(str, guess)), N_COLORS)
    feedback_index = feedback[0] * 5 + feedback[1]
    return guess_index * 25 + feedback_index

def action_to_guess(action):
    base_repr = np.base_repr(action, base=N_COLORS)
    padded_repr = base_repr.zfill(CODE_LENGTH) # Pad with zeros to the correct length
    return [int(digit) + 1 for digit in padded_repr]

def compute_reward(hits, pseudo_hits):
    reward = hits * 0.5 + pseudo_hits * 0.25
    if hits == CODE_LENGTH:
        reward += 5  # Bonus reward for guessing the code correctly
    else:
        reward -= 0.1  # Small penalty for incorrect guess
    return reward


def train_agent():
    q_table = np.zeros((5 * 5, N_COLORS**CODE_LENGTH))

    print_interval = N_GAMES // 100
    
    #track the total number of guesses from all games.
    totalGuesses = 0

    for game in range(N_GAMES):
        if game % print_interval == 0:
            progress_percent = (game / N_GAMES) * 100
            print(f"Training progress: {progress_percent:.1f}%")

        code = generate_code()
        state = (0, 0)  # Initial feedback
        done = False
        guesses = 0


        while not done:
            if random.random() < EPSILON:
                action = random.randint(0, N_COLORS**CODE_LENGTH - 1)
            else:
                action = np.argmax(q_table[state[0] * 5 + state[1]])

            guess = action_to_guess(action)  
            # print(code, guess)
            
            hits, pseudo_hits = provide_feedback(guess, code)
            reward = compute_reward(hits, pseudo_hits)
            reward -= guesses * 0.15  # Decrease reward based on the number of guesses
            new_state = (hits, pseudo_hits)

            if hits == CODE_LENGTH:
                done = True

            best_next_action = np.argmax(q_table[new_state[0] * 5 + new_state[1]])
            q_table[state[0] * 5 + state[1], action] = (1 - LEARNING_RATE) * q_table[state[0] * 5 + state[1], action] + \
                                                       LEARNING_RATE * (reward + DISCOUNT_FACTOR * q_table[new_state[0] * 5 + new_state[1], best_next_action])

            state = new_state
            
            guesses += 1
        # print("took ", guesses, " guesses.")
        totalGuesses = totalGuesses + guesses

    print("Training complete!")
    print("Average guesses per game: ", totalGuesses / N_GAMES)
    return q_table


def play_game(q_table):
    code = generate_code()
    state = ([0] * CODE_LENGTH, (0, 0))
    attempts = 0

    while True:
        guess, feedback = state
        action = np.argmax(q_table[state_index(state)])
        new_guess = action_to_guess(action)
        hits, pseudo_hits = provide_feedback(new_guess, code)
        print(f"Agent's guess: {new_guess}, Hits: {hits}, Pseudo-hits: {pseudo_hits}")

        if hits == CODE_LENGTH:
            print(f"Agent guessed the code {code} in {attempts} attempts.")
            break

        feedback_input = input("Enter your feedback (Hits Pseudo-hits): ").strip().split()
        feedback = tuple(map(int, feedback_input))
        state = (new_guess, feedback)
        attempts += 1

def main():
    print("Training the agent. Please wait...")
    q_table = train_agent()
    print("Training complete. Let's play!")
    play_game(q_table)

if __name__ == "__main__":
    main()
