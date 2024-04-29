import tkinter as tk
from tkinter import font as tkFont
import os

def launch_game(game):
    if game == "Typing Game":
        os.system(f"python typing_game.py")
    elif game == "Snake Game":
        os.system(f"python snakegame.py")
    elif game == "Flappy Bird Game":
        os.system(f"python flappybird.py")
    else:
        os.system(f"python {game}.py")

def launch_selected_game():
    selected_game = games_listbox.get(tk.ACTIVE)
    launch_game(selected_game)

root = tk.Tk()
root.title("Game Launcher")

# Add label for the prompt
prompt_label = tk.Label(root, text="Which game do you want to play?", font=("Helvetica", 12))
prompt_label.pack(pady=5)

games = ["Snake Game", "Pacman", "Typing Game", "Flappy Bird Game"]

custom_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

games_listbox = tk.Listbox(root, font=custom_font)
for game in games:
    games_listbox.insert(tk.END, game)
games_listbox.pack(pady=10)

launch_button = tk.Button(root, text="Play Game", padx=5, pady=5, command=launch_selected_game)
launch_button.pack()

root.mainloop()
