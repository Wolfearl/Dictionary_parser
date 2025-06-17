from tkinter import Tk, ttk, StringVar, IntVar
import pandas as pd


def get_frame2(w, d):
    for widget in frame2.winfo_children():
        if isinstance(widget, (ttk.Label, ttk.Label)):
            widget.config(text="")
    lbl1 = ttk.Label(frame2, text=w[global_i.get()], style="My.TLabel", anchor="center")
    lbl1.grid(row=0, column=0, columnspan=2)

    lbl2 = ttk.Label(frame2, text=d[global_i.get()], style="D.TLabel", anchor="center", wraplength=400, justify="center")
    lbl2.grid(row=1, column=0, columnspan=2)


def change_frame2(how):
    match how:
        case 'd':
            if global_i.get() == len_data.get() - 1:
                global_i.set(0)
            else:
                global_i.set(global_i.get() + 1)
        case 'n':
            if global_i.get() == 0:
                global_i.set(len_data.get() - 1)
            else:
                global_i.set(global_i.get() - 1)

    main_filter()


def do_filter():
    return all_data[all_data['Слово'].str.startswith(letter_var.get())]

def main_filter():
    if letter_var.get() == "ВCE":
        len_data.set(len(all_data))
        d_word = all_data['Слово'].tolist()
        d_disc = all_data['Определение'].tolist()
        get_frame2(d_word, d_disc)
    else:
        get_data = do_filter()
        len_data.set(len(get_data))
        d_word = get_data['Слово'].tolist()
        d_disc = get_data['Определение'].tolist()
        get_frame2(d_word, d_disc)

def selected_filter(event):
    global_i.set(0)
    main_filter()


root = Tk()
root.geometry("500x500+500+150")
root.title("Словарь программиста")

style = ttk.Style()
style.theme_use("clam")
style.configure("My.TFrame", relief="raised")
style.configure("My.TLabel", font=("Lucida Sans Unicode", 18))
style.configure("D.TLabel", font=("Lucida Sans Unicode", 14))

letters = ["ВCE"] + [
                    'А', 'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',
                    'Т', 'У', 'Ф', 'Х'
                    ]
letter_var = StringVar(value=letters[0])
all_data = pd.read_excel("dictionary.xlsx", engine="openpyxl")
len_data = IntVar(value=0)
global_i = IntVar(value=0)

frame1 = ttk.Frame(style="My.TFrame")
frame1.place(relx=0.5, rely=0.15, relwidth=0.9, relheight=0.2, anchor='center')
for r in range(2): frame1.rowconfigure(index=r, weight=1)
frame1.columnconfigure(index=0, weight=1)
label1 = ttk.Label(frame1, text="Фильтр", style="My.TLabel")
label1.grid(row=0, column=0)
combobox = ttk.Combobox(frame1, textvariable=letter_var, values=letters, state="readonly")
combobox.grid(row=1, column=0)
combobox.bind("<<ComboboxSelected>>", selected_filter)

frame2 = ttk.Frame(style="My.TFrame")
frame2.place(relx=0.5, rely=0.62, relwidth=0.9, relheight=0.67, anchor='center')
for r in range(3): frame2.rowconfigure(index=r, weight=1)
for c in range(2): frame2.columnconfigure(index=c, weight=1)
button21 = ttk.Button(frame2, text="Дальше", command=lambda h='d': change_frame2(h))
button21.grid(row=2, column=1, sticky='e', padx=15)
button22 = ttk.Button(frame2, text="Назад", command=lambda h='n': change_frame2(h))
button22.grid(row=2, column=0, sticky='w', padx=15)



root.mainloop()