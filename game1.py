import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    guess = int(guess_entry.get())
    attempts.append(guess)
    
    if guess < number:
        result_label.config(text="Загаданное число больше", fg="red")
    elif guess > number:
        result_label.config(text="Загаданное число меньше", fg="red")
    else:
        messagebox.showinfo("Победа!", f"Поздравляю! Вы угадали число за {len(attempts)} попыток!")
        reset_game()

def reset_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = []
    result_label.config(text="")
    guess_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Угадай число")

number = random.randint(1, 100)
attempts = []

instructions_label = tk.Label(window, text="Я загадал число от 1 до 100. Попробуйте отгадать его.", font=("Helvetica", 16))
instructions_label.pack(pady=10)

guess_entry = tk.Entry(window, font=("Helvetica", 14))
guess_entry.pack(pady=10)

submit_button = tk.Button(window, text="Проверить", font=("Helvetica", 14), command=check_guess)
submit_button.pack(pady=10)

result_label = tk.Label(window, font=("Helvetica", 16))
result_label.pack(pady=10)

reset_button = tk.Button(window, text="Начать заново", font=("Helvetica", 14), command=reset_game)
reset_button.pack(pady=10)

window.mainloop()