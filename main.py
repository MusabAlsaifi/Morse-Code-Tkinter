from tkinter import *

LARGE_FONT = ("Verdana", 35)

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


class MorseCodeApp(Tk):

    # __init__ function for class MorseCodeApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Home, TextToCode, CodeToText):
            frame = F(container, self)

            # initializing frame of that object from
            # Home, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    #  TODO: Dynamically resizable window


# first window frame
class Home(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # label of frame Layout 2
        label = Label(self, text="Home", font=LARGE_FONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        # -------------------------Buttons------------------------------ #
        button1 = Button(self, text="Text To Code",
                         command=lambda: controller.show_frame(TextToCode))
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text layout2
        button2 = Button(self, text="Code To Text",
                         command=lambda: controller.show_frame(CodeToText))
        button2.grid(row=2, column=1, padx=10, pady=10)


# second window frame page1
class TextToCode(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # -------------------------Labels------------------------------ #
        label = Label(self, text="Text To Code", font=LARGE_FONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        text_label = Label(self, text="text:")
        text_label.grid(row=1, column=0)

        morse_label = Label(self, text="Morse:")
        morse_label.grid(row=3, column=0)

        # -------------------------Text Boxes------------------------------ #
        self.encryption_box = Text(self, width=100, height=10)
        self.encryption_box.grid(row=3, column=1, columnspan=2)

        self.text_box = Text(self, width=100, height=10, highlightthickness=0, bd=1)
        self.text_box.grid(column=1, row=1, columnspan=2)
        self.text_box.focus()

        # -------------------------Buttons------------------------------ #
        # button to show frame 2 with text
        # layout2
        button1 = Button(self, text="Home",
                         command=lambda: controller.show_frame(Home))
        button1.grid(row=4, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = Button(self, text="Code To Text",
                         command=lambda: controller.show_frame(CodeToText))
        button2.grid(row=5, column=1, padx=10, pady=10)

        # to translate plain text to morse code
        # bind with encrypt method
        encrypt_button = Button(self, text="Encrypt", command=self.show_encryption)
        encrypt_button.grid(row=2, column=4)
        encrypt_button.bind_all('<Return>', lambda event: self.show_encryption())

    def encrypt(self):
        encryption = ""
        for letter in self.text_box.get("1.0", "end-1c").upper():
            if letter in MORSE_CODE_DICT:
                encryption += MORSE_CODE_DICT[letter] + ' '
            elif letter == " ":
                encryption += " "

        return encryption

    # get the result from encrypt method and display it in encryption_box
    def show_encryption(self):
        self.reset()
        return self.encryption_box.insert("end", f"{self.encrypt()}")

    # clear previous encryption_box data whenever encrypt_button is pressed
    def reset(self):
        return self.encryption_box.delete("1.0", "end")

    # TODO: method to clear all data
    # TODO: method to check if empty


# third window frame page2
class CodeToText(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # -------------------------Labels------------------------------ #
        label = Label(self, text="Text To Code", font=LARGE_FONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        text_label = Label(self, text="text:")
        text_label.grid(row=3, column=0)

        morse_label = Label(self, text="Morse:")
        morse_label.grid(row=1, column=0)

        # -------------------------Text Boxes------------------------------ #
        self.decryption_box = Text(self, width=100, height=10)
        self.decryption_box.grid(row=1, column=1, columnspan=2)
        self.decryption_box.focus()

        self.text_box = Text(self, width=100, height=10, highlightthickness=0, bd=1)
        self.text_box.grid(row=3, column=1, columnspan=2)

        # -------------------------Buttons------------------------------ #
        # button to show frame 2 with text
        button1 = Button(self, text="Text To Code",
                         command=lambda: controller.show_frame(TextToCode))
        button1.grid(row=5, column=1, padx=10, pady=10)

        # button to show frame 3
        button2 = Button(self, text="Home",
                         command=lambda: controller.show_frame(Home))
        button2.grid(row=4, column=1, padx=10, pady=10)

        # button to translate morse to plain text
        # bind with decrypt method
        decrypt_button = Button(self, text="Decrypt", command=self.show_decryption)
        decrypt_button.grid(row=2, column=4)

    def decrypt(self):
        message = self.decryption_box.get("1.0", "end-1c")
        morse = ""
        decipher = ""

        message += " "
        for code in message:
            if code != " ":
                num_of_spaces = 0
                morse += code
            else:
                num_of_spaces += 1
                if num_of_spaces == 2:
                    decipher += " "
                else:
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse)]
                    morse = ""

        return decipher

    # get the result from decrypt method and display it in text_box
    def show_decryption(self):
        self.reset()
        return self.text_box.insert("end", f"{self.decrypt()}")

    # clear previous text_box data whenever decrypt_button is pressed
    def reset(self):
        return self.text_box.delete("1.0", "end")

    # TODO: method to clear all data
    # TODO: method to check if empty


# TODO LAST: reorganise everything
# Driver Code
app = MorseCodeApp()
app.title("Morse Code Translator")
app.mainloop()
