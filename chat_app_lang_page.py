from tkinter import *
root = Tk()

def click():
    global type_lang
    type_lang = type_lang_input.get().lower()
    global know_lang
    know_lang = know_lang_input.get().lower()
    root.destroy()

# resize window
root.geometry("450x150")
root.title("Choose Languages")

# label for the language that the user wants to practice
type_lang_label = Label(root, text = "Enter the language you want to practice in the input box below")
type_lang_label.grid(row = 0, column = 0)

# the input box in which the user will input the language that they want to practice
type_lang_input = Entry(root, width = 70)
type_lang_input.grid(padx = 10, pady = 10, row = 1, column = 0)

# label for the language that the user already knows
know_lang_label = Label(root, text = "Enter a language you already know in the input box below")
know_lang_label.grid(row = 2, column = 0)

# the input box in which the user will input the language that they already know
know_lang_input = Entry(root, width = 70)
know_lang_input.grid(padx = 10, pady = 10, row = 3, column = 0)

# the enter button
enter_button = Button(root, text = "Enter", command = click)
enter_button.grid(row = 4, column = 0)

root.mainloop()
