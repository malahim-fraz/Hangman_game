import tkinter as tk
from tkinter import ttk, messagebox
import random

# --------------------- Theme Colors ---------------------
themes = {
    "Lavender": "#e6e6fa",
    "Pink": "#ffe4e1",
    "Yellow": "#fffacd",
    "Green": "#d0f0c0",
    "Blue": "#add8e6"
}
current_theme = "Lavender"

# --------------------- Word List by Category ---------------------
words_by_category = {
    "Food": ["apple", "banana", "grapes", "kiwi", "mango", "orange", "peach", "lemon"],
    "Things": ["table", "bottle", "pencil", "phone", "laptop", "chair"],
    "Places": ["paris", "london", "karachi", "tokyo", "lahore", "cairo"],
    "People": ["john", "emma", "alice", "mark", "lisa", "sara"],
    "Mix": ["robot", "magic", "jungle", "dream", "river", "chess"]
}

# --------------------- Hangman Styles ---------------------
hangman_styles = {
    "Classic": [
        "",
        "O",
        "O\n |",
        "O\n/|",
        "O\n/|\\",
        "O\n/|\\\n/",
        "O\n/|\\\n/ \\"
    ],
    "Wizard": [
        "",
        "🔮",
        "🔮 🧙‍️",
        "🔮 🧙‍️\n /|",
        "🔮 🧙‍️\n /|\\",
        "🔮 🧙‍️\n /|\\\n /",
        "🔮 🧙‍️\n /|\\\n / \\"
    ],
    "Party-Man": [
        "",
        "🥳",
        "🥳\n 🧥",
        "🥳\n🧥\n /|",
        "🥳\n🧥\n /|\\",
        "🥳\n🧥\n /|\\\n /",
        "🥳\n🧥\n /|\\\n / \\"
    ],
}
current_style = "Classic"


# --------------------- App Setup ---------------------
root = tk.Tk()
root.title("MiniGame World 🎮")
root.geometry("500x500")

# --------------------- Frame Functions ---------------------
def show_frame(frame):
    frame.tkraise()
    root.configure(bg=themes[current_theme])

def apply_theme():
    global current_theme
    selected = theme_var.get()
    if selected in themes:
        current_theme = selected
        for frame in (welcome_frame, menu_frame, settings_frame, play_frame, category_frame):
            frame.configure(bg=themes[selected])
        root.configure(bg=themes[selected])
        update_theme_on_widgets()

def update_theme_on_widgets():
    hangman_title.config(bg=themes[current_theme])
    word_display.config(bg=themes[current_theme])
    guesses_label.config(bg=themes[current_theme])
    hangman_visual.config(bg=themes[current_theme])
    for btn in letter_buttons:
        btn.config(bg="white")

# --------------------- Welcome Frame ---------------------
welcome_frame = tk.Frame(root, bg=themes[current_theme])
welcome_frame.place(relwidth=1, relheight=1)

welcome_label = tk.Label(welcome_frame, text="🎉 Welcome to MiniGame World 🎉", font=("Arial", 20), bg=themes[current_theme])
welcome_label.pack(expand=True)

root.after(5000, lambda: show_frame(menu_frame))

# --------------------- Menu Frame ---------------------
menu_frame = tk.Frame(root, bg=themes[current_theme])
menu_frame.place(relwidth=1, relheight=1)

menu_title = tk.Label(menu_frame, text="Main Menu", font=("Arial", 24), bg=themes[current_theme])
menu_title.pack(pady=30)

play_btn = tk.Button(menu_frame, text="▶️ Play", font=("Arial", 14), width=20, command=lambda: show_frame(category_frame))
play_btn.pack(pady=10)

custom_btn = tk.Button(menu_frame, text="🎨 Customize", font=("Arial", 14), width=20, command=lambda: show_frame(customize_frame))
custom_btn.pack(pady=10)

settings_btn = tk.Button(menu_frame, text="⚙️ Settings", font=("Arial", 14), width=20, command=lambda: show_frame(settings_frame))
settings_btn.pack(pady=10)

exit_btn = tk.Button(menu_frame, text="🚪 Exit", font=("Arial", 14), width=20, command=root.destroy)
exit_btn.pack(pady=10)

# --------------------- Settings Frame ---------------------
settings_frame = tk.Frame(root, bg=themes[current_theme])
settings_frame.place(relwidth=1, relheight=1)

settings_title = tk.Label(settings_frame, text="Settings", font=("Arial", 24), bg=themes[current_theme])
settings_title.pack(pady=30)

theme_var = tk.StringVar(value=current_theme)
theme_label = tk.Label(settings_frame, text="Choose Theme:", font=("Arial", 14), bg=themes[current_theme])
theme_label.pack()

theme_menu = ttk.Combobox(settings_frame, textvariable=theme_var, values=list(themes.keys()), state="readonly")
theme_menu.pack(pady=10)

apply_btn = tk.Button(settings_frame, text="Apply Theme", font=("Arial", 12), command=apply_theme)
apply_btn.pack(pady=10)

back_btn = tk.Button(settings_frame, text="⬅️ Back to Menu", font=("Arial", 12), command=lambda: show_frame(menu_frame))
back_btn.pack(pady=10)
# --------------------- Customize Frame ---------------------
customize_frame = tk.Frame(root, bg=themes[current_theme])
customize_frame.place(relwidth=1, relheight=1)

customize_title = tk.Label(customize_frame, text="Customize Hangman", font=("Arial", 24), bg=themes[current_theme])
customize_title.pack(pady=20)

style_var = tk.StringVar(value=current_style)
style_label = tk.Label(customize_frame, text="Choose Style:", font=("Arial", 14), bg=themes[current_theme])
style_label.pack()

style_menu = ttk.Combobox(customize_frame, textvariable=style_var, values=list(hangman_styles.keys()), state="readonly")
style_menu.pack(pady=10)

def apply_style():
    global current_style
    current_style = style_var.get()
    messagebox.showinfo("✔️ Style Applied", f"You selected: {current_style}")

apply_style_btn = tk.Button(customize_frame, text="Apply Style", font=("Arial", 12), command=apply_style)
apply_style_btn.pack(pady=10)

back_btn2 = tk.Button(customize_frame, text="⬅️ Back to Menu", font=("Arial", 12), command=lambda: show_frame(menu_frame))
back_btn2.pack(pady=10)

# --------------------- Category Selection Frame ---------------------
category_frame = tk.Frame(root, bg=themes[current_theme])
category_frame.place(relwidth=1, relheight=1)

category_title = tk.Label(category_frame, text="Choose a Category", font=("Arial", 20), bg=themes[current_theme])
category_title.pack(pady=30)

for category in words_by_category:
    btn = tk.Button(category_frame, text=category, font=("Arial", 14), width=20,
                    command=lambda c=category: [start_new_game(c), show_frame(play_frame)])
    btn.pack(pady=5)

# --------------------- Play Frame (Hangman Game) ---------------------
play_frame = tk.Frame(root, bg=themes[current_theme])
play_frame.place(relwidth=1, relheight=1)

hangman_title = tk.Label(play_frame, text="🎯 Hangman Game 🎯", font=("Arial", 20), bg=themes[current_theme])
hangman_title.pack(pady=10)

hangman_visual = tk.Label(play_frame, text="", font=("Courier", 18), bg=themes[current_theme])
hangman_visual.pack(pady=5)

word_display = tk.Label(play_frame, text="", font=("Courier", 24), bg=themes[current_theme])
word_display.pack(pady=10)

guesses_label = tk.Label(play_frame, text="Wrong Guesses: ", font=("Arial", 14), bg=themes[current_theme])
guesses_label.pack()

letter_frame = tk.Frame(play_frame)
letter_frame.pack(pady=10)

letter_buttons = []

back_to_menu_btn = tk.Button(play_frame, text="⬅️ Back to Menu", font=("Arial", 12), command=lambda: show_frame(menu_frame))
back_to_menu_btn.pack(pady=10)

# --------------------- Hangman Logic ---------------------
secret_word = ""
displayed_word = []
wrong_guesses = []


def create_letter_buttons():
    for widget in letter_frame.winfo_children():
        widget.destroy()
    letter_buttons.clear()
    for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        btn = tk.Button(letter_frame, text=letter, width=3, font=("Arial", 12),
                        command=lambda l=letter: make_guess(l.lower()))
        btn.grid(row=i // 9, column=i % 9, padx=2, pady=2)
        letter_buttons.append(btn)

def start_new_game(category):
    global secret_word, displayed_word, wrong_guesses
    secret_word = random.choice(words_by_category[category])
    displayed_word = ["_" for _ in secret_word]
    wrong_guesses = []
    update_display()
    create_letter_buttons()

def update_display():
    word_display.config(text=" ".join(displayed_word))
    guesses_label.config(text=f"Wrong Guesses: {', '.join(wrong_guesses)}")
    hangman_visual.config(text=hangman_styles[current_style][len(wrong_guesses)])

def make_guess(letter):
    if letter in secret_word:
        for i, l in enumerate(secret_word):
            if l == letter:
                displayed_word[i] = letter
    else:
        if letter not in wrong_guesses:
            wrong_guesses.append(letter)

    update_display()
    check_game_status()
    disable_button(letter)

def disable_button(letter):
    for btn in letter_buttons:
        if btn["text"].lower() == letter:
            btn.config(state="disabled", disabledforeground="gray")

def check_game_status():
    if "_" not in displayed_word:
        messagebox.showinfo("🎉 You Win!", f"Congratulations! The word was '{secret_word}'")
        show_frame(menu_frame)
    elif len(wrong_guesses) >= 6:
        messagebox.showwarning("💀 Game Over", f"You lost! The word was '{secret_word}'")
        show_frame(menu_frame)

# --------------------- Start App ---------------------
show_frame(welcome_frame)
root.mainloop()
