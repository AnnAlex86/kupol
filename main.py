import tkinter as tk
from tkinter.filedialog import askdirectory
import os, time

window = tk.Tk()
window.title("Сканер технологического паспорта")
window.resizable(0, 0)
isRun = False
width = 500
height = 250

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

window.geometry('%dx%d+%d+%d' % (width, height, x, y))



def Run_folder(path_to_watch, is_run):
    before = dict([(f, None) for f in os.listdir(path_to_watch)])
    while is_run:
        time.sleep(10)
        after = dict([(f, None) for f in os.listdir(path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added: print("Added: ", ", ".join(added))
        if removed:
            print("Removed: ", ", ".join(removed))
        before = after


def choose_input_directory():
    directory = askdirectory()
    string_input_directory.set(directory)
    Run_folder(directory, True)


def choose_output_directory():
    directory = askdirectory()
    string_output_directory.set(directory)


def start():
    isRun = True

loadimage = tk.PhotoImage(file="in_button.png")
button_input = tk.Button(window, image=loadimage, command=choose_input_directory)
loadimage2 = tk.PhotoImage(file="out_button.png")
button_output = tk.Button(window, image=loadimage2, command=choose_output_directory)
button_launch = tk.Button(window, text="Запуск")

string_output_directory = tk.StringVar()
string_input_directory = tk.StringVar()
label_input_directory = tk.Label(window, textvariable=string_input_directory)
label_output_directory = tk.Label(window, textvariable=string_output_directory)

button_input.pack()
label_input_directory.pack()
button_output.pack()
label_output_directory.pack()
button_launch.pack()
label_input_directory.pack()

window.mainloop()

