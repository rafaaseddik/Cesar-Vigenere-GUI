from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from dependencies.Cesar import *
from CesarGUI import CesarGui
from VigenereGUI import VigenereGui


# Authors : Mohamed Rafaa Seddik
#           Mohamed Khalil Nouisser
#           Nour Hanana
#           Oussama Gastli
#
#           GL4 -  2018/2019
#           Security Project

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Encoder-Decoder")
        self.configure()

        # allowing the widget to take the full space of the root window

        # creating labels
        mainTitle = Label(self, text="Encoder-Decoder", fg="red", font=("Helvetica", 20))
        # placing labels
        mainTitle.pack(fill=X)
        # creating buttons instances
        buttonFont = ("Helvetica", 15)
        quitButton = Button(self, text="Exit", command=self.client_exit, font=buttonFont)
        cesarButton = Button(self, text="Cesar", command=self.go_to_cesar, font=buttonFont)
        vigenereButton = Button(self, text="Vigenere", command=self.go_to_vigenere, font=buttonFont)
        # placing the button on my window
        cesarButton.pack(fill=X, padx=100, pady=10)
        vigenereButton.pack(fill=X, padx=100, pady=10)
        quitButton.pack(fill=X, padx=100, pady=10)
        self.pack(fill=BOTH, expand=1)

    def client_exit(self):
        exit()

    def go_to_cesar(self):
        cesarGui = CesarGui(master=self.master)

    def go_to_vigenere(self):
        vigenereGui = VigenereGui(master=self.master)


def main():
    """s = ttk.Style();
    s.theme_use('xpnative')"""
    root = Tk()
    # size of the window
    root.geometry("400x300")

    app = Window(root)
    root.mainloop()


if __name__ == "__main__":
    main()
