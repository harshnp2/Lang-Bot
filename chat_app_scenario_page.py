from tkinter import *
from translate import Translator
from chat_app_lang_page import know_lang

root = Tk()

root.state("zoomed")
root.title("Scenarios")

def clicked(scenario_num):
    global scene_num
    scene_num = scenario_num
    root.destroy()

scenario_translator = Translator(from_lang = "english", to_lang = know_lang)
scenario1_trans = scenario_translator.translate("Greeting Friends and Family")
scenario2_trans = scenario_translator.translate("Ordering Food At A Restaurant")
scenario3_trans = scenario_translator.translate("Going to the Doctor's Office")
scenario4_trans = scenario_translator.translate("Meeting someone for the first time")


scenario1 = Button(root, text = scenario1_trans, borderwidth = 0.5, command = lambda: clicked(1))
scenario2 = Button(root, text = scenario2_trans, borderwidth = 0.5, command = lambda: clicked(2))
scenario3 = Button(root, text = scenario3_trans, borderwidth = 0.5, command = lambda: clicked(3))
scenario4 = Button(root, text = scenario4_trans, borderwidth = 0.5, command = lambda: clicked(4))


scenario1.place(relx = 0.03, rely = 0, relwidth = 0.3, relheight = 0.4)
scenario2.place(relx = 0.36, rely = 0, relwidth = 0.3, relheight = 0.4)
scenario3.place(relx = 0.69, rely = 0, relwidth = 0.3, relheight = 0.4)
scenario4.place(relx = 0.03, rely = 0.5, relwidth = 0.3, relheight = 0.4)


root.mainloop()