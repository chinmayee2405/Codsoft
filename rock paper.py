import tkinter as tk
import random

# Game logic
def play(user_choice):
    global user_score, computer_score
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    result_label.config(text=f"🧑 You: {user_choice} | 💻 Computer: {computer_choice}\n{result}")
    score_label.config(text=f"Score -> You: {user_score} | Computer: {computer_score}")

# Initialize scores
user_score = 0
computer_score = 0

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("350x300")

tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 12)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Rock", width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Paper", width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Scissors", width=10, command=lambda: play("scissors")).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12), pady=10)
result_label.pack()

score_label = tk.Label(root, text="Score -> You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack()

tk.Button(root, text="Quit", command=root.destroy, width=10).pack(pady=15)

root.mainloop()



