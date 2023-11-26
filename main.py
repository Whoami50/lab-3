import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



def stop_progressbar(ungenned):
    progressbar.stop()
    progressbar['value'] = 100
    genned = str(ungenned) + '-' + str(ungenned)[3:5] + str(ungenned)[0:3] + '-' + str(ungenned)
    messagebox.showinfo("Ключ успешно сгенерирован", "Ваш ключ: {}".format(genned))


def on_button_click(entry_widget):
    user_input = entry_widget.get()

    if len(user_input) == 5:
        messagebox.showinfo("Введено успешно", "Вы ввели: {}".format(user_input.upper()))
        progressbar.start()
        root.after(ms=5500, func=stop_progressbar(user_input.upper()))


    else:
        messagebox.showerror("Ошибка", "Введите ровно 5 символов!")


root = tk.Tk()
root.title("Keygen")

bg_image = tk.PhotoImage(file='bg.gif')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

root.geometry('1024x513')

entry = tk.Entry(root, width=100, justify="center")
entry.pack(pady=100)

button = tk.Button(root, text="Сгенерировать", command=lambda: on_button_click(entry))
button.pack()

progressbar = ttk.Progressbar(root, maximum=99, mode='determinate', length=300)
progressbar.pack(pady=10)

root.mainloop()
