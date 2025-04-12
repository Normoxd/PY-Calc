# THIS CODE IS LICENSED UNDER THE "GNU GENERAL PUBLIC LICENSE"

version = "v1.2"
whatsnew = "1. Adaptive Dark/Light mode for About and History window \n2. a Mini view mode \n3.Better code explaining and formatting \n4. The window title finally got renamed to PY-Calc for better project recognition.\n"
knownbugs = "1. [Not Fixed]\n\non Windows the emojis for buttons will be just unicode characters, i tried to make the button font to switch to Segoe UI Emoji but the problem is with the Emoji support on Python for Windows as i can say. I'm only using builtin fonts because i want this to be portable as much as possible. any solutions without custom fonts?\n\n2. [FIXED]\n\nWhen using the mini view button then revert will make the revert button be stuck on the regular view stopping you from switching to mini view. This happend because of a issue of the code that was there to detect the current mode\n"

import tkinter as tk
from tkinter import PhotoImage, Toplevel

# MAIN WINDOW CONFIGS
# The window size is hard coded into the code, Use the replace feature to correctly edit the window size

root = tk.Tk()
root.title("PY-Calc " + version)
root.geometry("250x440")
# Make the line below to (1, 1) to make the main window resizable
root.resizable(0, 0)

top_frame = tk.Frame(root, bg="#000000")
top_frame.grid(row=0, column=0, columnspan=4, pady=4, sticky="nsew")

top_frame.grid_columnconfigure(0, weight=0) # Dark/Light mode toggle
top_frame.grid_columnconfigure(1, weight=0) # History Button
top_frame.grid_columnconfigure(2, weight=0) # Mini/Regular view toggle
top_frame.grid_columnconfigure(3, weight=0) # About button

# WINDOW/COMMAND CONFIGS

about_window = None
history_window = None

def open_about():
    global about_window
    if about_window is None or not tk.Toplevel.winfo_exists(about_window):
        about_window = Toplevel(root)
        about_window.title("About")
        about_window.geometry("225x425")
        about_text = tk.Text(about_window, font=("Source Code Pro", 12), wrap=tk.WORD)
        about_text.pack(expand=True, fill=tk.BOTH)
        about_text.insert(tk.END, "🖩 PY-Calc " + version + "\n\n")
        about_text.insert(tk.END, "🏁 What's New!\n\n" + whatsnew + "\n\n")
        about_text.insert(tk.END, "⭕ Known Bugs:\n\n" + knownbugs)
        apply_theme_to_about()
    else:
        about_window.lift()

def open_history():
    global history_window
    if history_window is None or not tk.Toplevel.winfo_exists(history_window):
        history_window = Toplevel(root)
        history_window.title("History")
        history_window.geometry("245x400")
        history_text = tk.Text(history_window, wrap=tk.WORD, font=("Comfortaa", 22))
        history_text.pack(expand=True, fill=tk.BOTH)
        for calculation, result in previous_calculations:
            history_text.insert(tk.END, f"{calculation}\n", "calculation")
            history_text.insert(tk.END, f"= {result}\n\n", "result")
        history_text.tag_config("calculation", foreground="grey")
        history_text.tag_config("result", foreground="#00a973")
        history_text.config(state=tk.NORMAL)
        apply_theme_to_history()
    else:
        history_window.lift()

    apply_theme_to_about()
    apply_theme_to_history()

global miniview_is_enabled
miniview_is_enabled = False

def set_miniview_true():
    global miniview_is_enabled
    root.geometry("160x280")
    miniview_is_enabled = True

def set_miniview_false():
    global miniview_is_enabled
    root.geometry("250x440")
    miniview_is_enabled = False

def miniview_switcher():
    global miniview_is_enabled
    if miniview_is_enabled:
        set_miniview_false()
    else:
        set_miniview_true()

# THEME CONFIGS

is_dark_mode = True #Make it 'false' to make light mode the default
previous_calculations = []

def switch_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    apply_theme()


def apply_theme_to_about():
    if about_window is not None and tk.Toplevel.winfo_exists(about_window):
        for widget in about_window.winfo_children():
            if isinstance(widget, tk.Text):
                if is_dark_mode:
                    about_window.config(bg="#0e0e0e")
                    widget.config(bg="#0e0e0e", fg="#f0f0f0")
                else:
                    about_window.config(bg="#ffffff")
                    widget.config(bg="#ffffff", fg="#0e0e0e")

def apply_theme_to_history():
    if history_window is not None and tk.Toplevel.winfo_exists(history_window):
        if is_dark_mode:
            history_window.config(bg="#0e0e0e")
            for widget in history_window.winfo_children():
                if isinstance(widget, tk.Text):
                    widget.config(bg="#0e0e0e", fg="#f0f0f0")
        else:
            history_window.config(bg="#ffffff")
            for widget in history_window.winfo_children():
                if isinstance(widget, tk.Text):
                    widget.config(bg="#ffffff", fg="#0e0e0e")


def apply_theme():
    global about_window, history_window
    if is_dark_mode:
        top_frame.config(bg="#121212")
        root.configure(bg="#121212")
        entry.config(bg="#0e0e0e", fg="#f0f0f0")
        mode_button.config(text="☀", bg="#1e1e1e", fg="#ffffff", activebackground="#0e0e0e")
        history_button.config(bg="#1e1e1e", fg="#776633", activebackground="#0e0e0e")
        about_button.config(bg="#1e1e1e", fg="#771122", activebackground="#0e0e0e")
        miniview_button.config(bg="#1e1e1e", fg="#551188", activebackground="#0e0e0e")
        button_config(bg="#0e0e0e", fg="#f0f0f0", activebackground="#5e5e5e")
        equal_button.config(bg="#8a1d9d", fg="#ffffff", activebackground="#6a3d6d")
    else:
        top_frame.config(bg="#ffffff")
        root.configure(bg="#ffffff")
        entry.config(bg="#f0f0f0", fg="#0e0e0e")
        mode_button.config(text="🌙", bg="#f0f0f0", fg="#999900", activebackground="#d0d0d0")
        history_button.config(bg="#f0f0f0", fg="#776633", activebackground="#d0d0d0")
        about_button.config(bg="#f0f0f0", fg="#661122", activebackground="#d0d0d0")
        miniview_button.config(bg="#f0f0f0", fg="#551177", activebackground="#d0d0d0")
        button_config(bg="#f0f0f0", fg="#0e0e0e", activebackground="#ffffff")
        equal_button.config(bg="#9a1d9d", fg="#f0f0f0", activebackground="#7a4d7d")

    apply_theme_to_about()
    apply_theme_to_history()

# TOP BAR CONFIGS

mode_button = tk.Button(top_frame, text="☀️", padx=1, pady=1, command=switch_mode, font=("Noto Color Emoji", 12))
mode_button.grid(row=0, column=1, padx=2, pady=2)

history_button = tk.Button(top_frame, text="⏰", padx=1, pady=1, command=open_history, font=("Noto Color Emoji", 12))
history_button.grid(row=0, column=2, padx=2, pady=2)

miniview_button = tk.Button(top_frame, text="🪟", padx=1, pady=1, command=miniview_switcher, font=("Noto Color Emoji", 12))
miniview_button.grid(row=0, column=3, padx=2, pady=2)

about_button = tk.Button(top_frame, text="❓", padx=1, pady=1, command=open_about, font=("Noto Color Emoji", 12))
about_button.grid(row=0, column=6, padx=2, pady=2)

root.grid_columnconfigure(0, weight=2)
top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(8, weight=1)

# OUTPUT BAR CONFIGS (AKA: ENTRY BAR) 

entry = tk.Entry(root, width=16, borderwidth=0, font=("Comfortaa", 30), justify="right")
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# NUMBER/FUNTION BUTTONS CONFIG

def button_config(bg, fg, activebackground):
    for button in buttons:
        button.config(bg=bg, fg=fg, activebackground=activebackground, font=("Comfortaa", 17))

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        calculation = entry.get()
        result = str(eval(calculation))
        previous_calculations.append((calculation, result))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

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
        equal_button = tk.Button(root, text=text, padx=50, pady=50, font=("Comfortaa", 18, "bold"), command=button_equal)
        equal_button.grid(row=row, column=column, sticky="nsew")

    else:
        button = tk.Button(root, text=text, padx=50, pady=50, font=("Comfortaa", 18),
                           command=lambda txt=text: button_click(txt) if txt not in ["=", "C", "⌫"] else button_clear() if txt == 'C' else entry.delete(len(entry.get()) - 1) if txt == '⌫' else None)
        button.grid(row=row, column=column, sticky="nsew")
        buttons.append(button)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(2, 8):
    root.grid_rowconfigure(i, weight=1)

apply_theme()
root.mainloop()
