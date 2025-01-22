import tkinter as tk
from tkinter import PhotoImage, Toplevel

root = tk.Tk()
root.title("Calculator")
root.geometry("300x500")
root.resizable(0, 0)

is_dark_mode = True
previous_calculations = []

def switch_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    apply_theme()

def apply_theme():
    if is_dark_mode:
        top_frame.config(bg="#121213")
        root.configure(bg="#121213")
        entry.config(bg="#0e0e0e", fg="#f0f0f0")
        mode_button.config(text="☀", bg="#1e1e1e", fg="#999900", activebackground="#0e0e0e")
        history_button.config(bg="#1e1e1e", fg="#776633", activebackground="#0e0e0e")
        about_button.config(bg="#1e1e1e", fg="#771122", activebackground="#0e0e0e")
        button_config(bg="#0e0e0e", fg="#ffffff", activebackground="#666666")
        equal_button.config(bg="#6A0DAD", fg="#ffffff", activebackground="#9b3fA2")

    else:
        top_frame.config(bg="#ffffff")
        root.configure(bg="#ffffff")
        entry.config(bg="#f0f0f0", fg="#0e0e0e")
        mode_button.config(text="🌙", bg="#f0f0f0", fg="#999900", activebackground="#d0d0d0")
        history_button.config(bg="#f0f0f0", fg="#776633", activebackground="#d0d0d0")
        about_button.config(bg="#f0f0f0", fg="#661122", activebackground= "#d0d0d0")
        button_config(bg="#f0f0f0", fg="#1e1e1e", activebackground="#e0e0e0")
        equal_button.config(bg="#ffcc00", fg="#000000", activebackground="#ffd633")
   
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
        calculation = entry.get()
        result = str(eval(calculation))
        previous_calculations.append((calculation, result))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def open_about():
    about_window = Toplevel(root)
    about_window.title("About")
    about_window.geometry("350x350")

    about_text = tk.Text(about_window, bg="#0e0e0e", fg="#999999", font=("Source Code Pro", 17))
    about_text.pack(expand=True, fill=tk.BOTH)
    about_text.insert(tk.END, "\n🖩 PY-Calc v1.1\n")
    about_text.insert(tk.END, "\n\n\nWhat's New!\n\n- New colors\n- a About window\n- Icons got replaced by emojis\n\n")
    

def open_history():
    history_window = Toplevel(root)
    history_window.title("History")
    history_window.geometry("275x380")
    history_window.resizable(0, 0)

    history_text = tk.Text(history_window, wrap=tk.WORD, font=("Comfortaa", 19), bg="#121212")
    history_text.pack(expand=True, fill=tk.BOTH)

    for calculation, result in previous_calculations:
        history_text.insert(tk.END, f"{calculation}\n", "calculation")
        history_text.insert(tk.END, f"= {result}\n\n", "result")


    history_text.tag_config("calculation", foreground="grey")
    history_text.tag_config("result", foreground="#00a973")
    history_text.config(state=tk.NORMAL)

top_frame = tk.Frame(root, bg="#000000")
top_frame.grid(row=0, column=0, columnspan=4, pady=4, sticky="nsew")

top_frame.grid_columnconfigure(0, weight=0)
top_frame.grid_columnconfigure(1, weight=0)
top_frame.grid_columnconfigure(2, weight=0)
top_frame.grid_columnconfigure(3, weight=0)

mode_button = tk.Button(top_frame, text="☀️", padx=1, pady=1, command=switch_mode, font=("Noto Color Emoji", 12))
mode_button.grid(row=0, column=1, padx=2)

history_button = tk.Button(top_frame, text="⏰", padx=1, pady=1, command=open_history, font=("Noto Color Emoji", 12))
history_button.grid(row=0, column=2, padx=2)

about_button = tk.Button(top_frame, text="❓", padx=1, pady=1, command=open_about, font=("Noto Color Emoji", 12))
about_button.grid(row=0, column=3, padx=3)

root.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(4, weight=1)

entry = tk.Entry(root, width=16, borderwidth=0, font=("Comfortaa", 32), justify="right")
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
        equal_button = tk.Button(root, text=text, padx=50, pady=50, font=("Comfortaa", 18, "bold"),
                                 command=button_equal)
        equal_button.grid(row=row, column=column, sticky="nsew")
    else:
        button = tk.Button(root, text=text, padx=50, pady=50, font=("Comfortaa", 18),
                           command=lambda txt=text: button_click(txt) if txt not in ['=', 'C', '⌫'] else button_clear() if txt == 'C' else entry.delete(len(entry.get()) - 1) if txt == '⌫' else None)
        button.grid(row=row, column=column, sticky="nsew")
        buttons.append(button)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(2, 8):
    root.grid_rowconfigure(i, weight=1)

apply_theme()
root.mainloop()
