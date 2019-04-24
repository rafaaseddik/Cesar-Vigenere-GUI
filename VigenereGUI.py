from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename

from PIL import Image, ImageTk
from dependencies.Cesar import *
from subviews.vigenere.EncodeGui import EncodeGui
from subviews.vigenere.DecodeGui import DecodeGui
from subviews.vigenere.AnalyseGui import AnalyseGui

class VigenereGui(Frame):

    def __init__(self, master=None):
        self.frame = Toplevel(master)
        self.master = master
        self.init_window()
    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        #self.master.title("Cesar Encoder-Decoder")
        self.frame.configure()


        # creating labels
        mainTitle = Label(self.frame,text="Vigenere Encoder-Decoder",fg="red",font=("Helvetica", 20))
        # placing labels
        mainTitle.pack(fill=X)
        # creating buttons instances
        buttonFont = ("Helvetica", 15)

        encodeButton = Button(self.frame, text="Encoder un fichier", command = self.encode,font=buttonFont)
        decodeButton = Button(self.frame, text="Decoder un fichier", command = self.decode,font=buttonFont)
        cryptanalButton = Button(self.frame, text="Cryptanaliser un fichier", command = self.cryptanal,font=buttonFont)
        # placing the button on my window
        encodeButton.pack(fill=X,padx=100,pady=10)
        decodeButton.pack(fill=X,padx=100,pady=10)
        cryptanalButton.pack(fill=X,padx=100,pady=10)


    def encode(self):
        encodeGui = EncodeGui(master = self.master)
    def decode(self):
        decodeGui = DecodeGui(master=self.master)
    def cryptanal(self):
        analyseGui = AnalyseGui(master=self.master)




