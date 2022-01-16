import tkinter.font
from tkinter import *
from translate import Translator
from chat_app_lang_page import type_lang, know_lang
from chat import get_response, bot_name


bot_translator = Translator(from_lang = "english", to_lang = type_lang)
translator = Translator(from_lang = type_lang, to_lang = "english")

BG_GRAY = "#ABB2B9"
BG_COLOUR = "#17202A"
TEXT_COLOUR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

T_BG_COLOUR = "#0048BA"


class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self.T_lang = type_lang
        self.K_lang = know_lang
        self.times_translated = 0
        self.num_messages = 0
        # sets up the window
        self.setup()

    def run(self):
        self.window.mainloop()

    def setup(self):
        self.window.title("Chat")
        #self.window.resizable(width=False, height=False)
        self.window.state("zoomed")

        main_frame = Frame(self.window)
        main_frame.place(relx=0,rely=0,relwidth=1,relheight=1)

        left_frame = Frame(main_frame)
        left_frame.place(relx=0,rely=0,relwidth=0.7,relheight=1)

        right_frame = Frame(main_frame, bg = "#89CFF0")
        right_frame.place(relx=0.7,rely=0,relwidth=0.3,relheight=1)

        # head label
        head_label = Label(left_frame, bg=BG_COLOUR, fg=TEXT_COLOUR, text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(left_frame, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(left_frame, width=20, height=2, bg=BG_COLOUR, fg=TEXT_COLOUR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(left_frame, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOUR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self.on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda: self.on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        # done button
        done_button = Button(head_label, text = "DONE", font = FONT_BOLD, bg = "#0DFFF6", command = self.done_pressed)
        done_button.place(relx = 0.7, rely = 0.1, relheight = 0.7, relwidth = 0.22)

        # translator label
        translator_header = Label(right_frame, bg=T_BG_COLOUR, fg=TEXT_COLOUR, text="Translator", font=FONT_BOLD, pady=10)
        translator_header.place(relwidth=1)

        # Swap languages button
        swap_button = Button(right_frame, text = "<-->", bg = "#7CB9E8", command = self.swap_pressed)
        swap_button.place(relx = 0.45, rely = 0.85)

        # Language labels
        self.type_lang_subtitle = Label(right_frame, text = self.T_lang.upper(), bg = "#2E5894", fg = TEXT_COLOUR, borderwidth = 2, relief = "sunken")
        self.type_lang_subtitle.place(relx = 0.1, rely = 0.85, relwidth = 0.25, relheight = 0.05)

        self.know_lang_subtitle = Label(right_frame, text = self.K_lang.upper(), bg="#2E5894", fg=TEXT_COLOUR, borderwidth=2, relief="sunken")
        self.know_lang_subtitle.place(relx=0.65, rely=0.85, relwidth = 0.25, relheight = 0.05)

        # Input and Output Labels
        INPUT_LABEL = Label(right_frame, text="INPUT", bg="#2E5894", fg=TEXT_COLOUR, borderwidth=2, relief="sunken")
        INPUT_LABEL.place(relx=0.1, rely=0.2, relwidth=0.25, relheight=0.05)

        OUTPUT_LABEL = Label(right_frame, text="OUTPUT", bg="#2E5894", fg=TEXT_COLOUR, borderwidth=2, relief="sunken")
        OUTPUT_LABEL.place(relx=0.65, rely=0.2, relwidth=0.25, relheight=0.05)

        # Translation Input Box
        self.trans_entry = Text(right_frame, bg="#2C3E50", fg=TEXT_COLOUR, font=FONT)
        self.trans_entry.place(relwidth=0.4, relheight=0.45, rely=0.28, relx=0.02)

        # clear button
        self.clear_button = Button(right_frame, text = "CLEAR", bg = "#7CB9E8", command = self.delete_it)
        self.clear_button.place(relwidth = 0.42, relheight = 0.05, rely = 0.78, relx = 0.49)

        # Translation Output Box
        self.trans_output = Text(right_frame, bg = "#2C3E50", fg = TEXT_COLOUR, font = FONT)
        self.trans_output.place(relwidth=0.4, relheight=0.45, rely=0.28, relx=0.57)


        def retrieve_input():
            inputValue = self.trans_entry.get("1.0", "end-1c")
            print(inputValue)
            TRANSLATOR = Translator(from_lang = self.T_lang, to_lang = self.K_lang)
            translated = TRANSLATOR.translate(inputValue)
            self.trans_output.delete("1.0", "end")
            self.trans_output.insert(END, translated)
            self.times_translated += 1

        # translator enter button
        self.trans_enter_button = Button(right_frame, text = "ENTER", bg = "#7CB9E8", command=retrieve_input)
        self.trans_enter_button.place(relwidth=0.42, relheight=0.05, rely=0.78, relx=0.03)

    def delete_it(self):
        self.trans_entry.delete("1.0", "end")
        self.trans_output.delete("1.0", "end")

    def on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self.insert_message(msg, "You")

    def done_pressed(self):
        self.window.destroy()
        new_window = Tk()
        new_window.state("zoomed")
        new_window.title("Score")
        new_window.config(bg = "#24f3f0")
        if self.num_messages == 0:
            score = 1
        else:
            score = 1 - self.times_translated/self.num_messages
        percent_score = score*100
        font_style = tkinter.font.Font(size = 40)
        score_label = Label(new_window, text = f'Score:{percent_score}%', bg = "#24f3f0", fg = "navy", font = font_style, borderwidth = 2)
        score_label.place(relx = 0.1, rely = 0.3, relwidth = 0.8, relheight = 0.5)
        new_window.mainloop()

    def swap_pressed(self):
        print(f"BEFORE T_lang:{self.T_lang} K_lang:{self.K_lang}")
        temp = self.K_lang
        self.K_lang = self.T_lang
        self.T_lang = temp
        print("pressed")
        print(f"AFTER T_lang:{self.T_lang} K_lang:{self.K_lang}")
        self.type_lang_subtitle.configure(text=self.T_lang.upper())
        self.know_lang_subtitle.configure(text=self.K_lang.upper())


    def insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)


        translation = translator.translate(msg)

        # bot_translation = get_response(msg)
        bot_msg = get_response(translation)

        bot_translation = bot_translator.translate(bot_msg)


        msg2 = f"{bot_name}: {bot_translation}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

        self.num_messages += 2

if __name__ == "__main__":
    app = ChatApplication()
    app.run()