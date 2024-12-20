# In case if you did not saw the readme, read the note down below

# NOTE: You have to make these changes to the line 10,11,12 to actually make it work

# Add the path of the Moon-icon, Sun-icon, History-icon by removing the fake path and adding your paths of those files (You can download them via a zip file in this repo or make your own ones)

import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Calculator")
root.geometry("320x500")
root.resizable(0, 0)

try:
    moon_icon = PhotoImage(file="/path/to/moon.png").subsample(6, 6)
    sun_icon = PhotoImage(file="/path/to/sun-icon.png").subsample(6, 6)
    history_icon = PhotoImage(file="/path/to/clock.png").subsample(6, 6)
except Exception as e:
    print(f"Error loading icons: {e}")
    root.destroy()

is_dark_mode = True

def switch_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    apply_theme()

def apply_theme():
    if is_dark_mode:
        root.configure(bg="#121212")
        entry.config(bg="#1e1e1e", fg="#ffffff")
        mode_button.config(image=sun_icon, bg="#1e1e1e", activebackground="#333333")
        history_button.config(bg="#1e1e1e", activebackground="#333333")
        button_config(bg="#333333", fg="#ffffff", activebackground="#444444")
        equal_button.config(bg="#6A0DAD", fg="#ffffff", activebackground="#7b1fa2")
        top_frame.config(bg="#121212")
    else:
        root.configure(bg="#ffffff")
        entry.config(bg="#f0f0f0", fg="#000000")
        mode_button.config(image=moon_icon, bg="#ffffff", activebackground="#d0d0d0")
        history_button.config(bg="#ffffff", activebackground="#d0d0d0")
        button_config(bg="#f0f0f0", fg="#000000", activebackground="#e0e0e0")
        equal_button.config(bg="#ffcc00", fg="#000000", activebackground="#ffd633")
        top_frame.config(bg="#ffffff")

def button_config(bg, fg, activebackground):
    for button in buttons:
        button.config(bg=bg, fg=fg, activebackground=activebackground)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

top_frame = tk.Frame(root, bg="#000000")
top_frame.grid(row=0, column=0, columnspan=4, pady=4, sticky="nsew")

top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=0)
top_frame.grid_columnconfigure(2, weight=0)
top_frame.grid_columnconfigure(3, weight=1)

mode_button = tk.Button(top_frame, image=sun_icon, padx=10, pady=10, command=switch_mode)
mode_button.grid(row=0, column=1, padx=2)

history_button = tk.Button(top_frame, image=history_icon, padx=10, pady=10)
history_button.grid(row=0, column=2, padx=2)

root.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(3, weight=1)

entry = tk.Entry(root, width=16, borderwidth=0, font=('Google Sans', 36), justify='right')
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

buttons = []
button_texts = [
    ('%', 2, 0), ('CE', 2, 1), ('C', 2, 2), ('⌫', 2, 3),
    ('1/x', 3, 0), ('x²', 3, 1), ('√', 3, 2), ('/', 3, 3),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('*', 4, 3),
    ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('-', 5, 3),
    ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('+', 6, 3),
    ('±', 7, 0), ('0', 7, 1), ('.', 7, 2), ('=', 7, 3)
    ]

for (text, row, column) in button_texts:
    if text == '=':
        equal_button = tk.Button(root, text=text, padx=50, pady=50, font=('Comfortaa', 18, 'bold'),
                                 command=button_equal)
        equal_button.grid(row=row, column=column, sticky="nsew")
    else:
        button = tk.Button(root, text=text, padx=50, pady=50, font=('Comfortaa', 18),
                           command=lambda txt=text: button_click(txt) if txt not in ['=', 'C', '⌫'] else button_clear() if txt == 'C' else entry.delete(len(entry.get()) - 1) if txt == '⌫' else None)
        button.grid(row=row, column=column, sticky="nsew")
        buttons.append(button)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(2, 8):
    root.grid_rowconfigure(i, weight=1)

apply_theme()
root.mainloop()

