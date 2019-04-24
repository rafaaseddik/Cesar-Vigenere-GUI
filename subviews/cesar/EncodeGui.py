from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename

from PIL import Image, ImageTk
from dependencies.Cesar import *

class EncodeGui(Frame):

    def __init__(self, master=None):
        self.frame = Toplevel(master)
        self.master = master
        self.init_window()
    #Creation of init_window
    def init_window(self):

        # creating labels
        self.mainTitle = Label(self.frame,text="Cesar Encoder",fg="red",font=("Courier", 20))
        self.keyLabel = Label(self.frame,text="Encoding Key",fg="red",font=("Courier", 20))
        # placing labels
        self.mainTitle.pack(fill=X)
        # creating buttons instances
        buttonFont = ("Helvetica", 15)

        self.openFileButton = Button(self.frame, text="Ouvrir un fichier", command = self.openfile,font=buttonFont)
        self.encodeButton = Button(self.frame, text="Encoder", command = self.encode,font=buttonFont)
        self.saveFileButton = Button(self.frame, text="Exporter", command = self.export, font=buttonFont)

        # creating text area
        self.fileContent = Text(self.frame,height=20, width=100)
        self.keyContent = Text(self.frame,height=1, width=2,font=("Helvetica", 20))


        # placing the button on my window
        self.openFileButton.pack(fill=X,padx=20,pady=5)
        self.fileContent.pack(fill=X,padx=20,pady=5)
        self.keyLabel.pack(side=LEFT,padx=20,pady=5)
        self.keyContent.pack(side=LEFT,padx=20,pady=5,ipadx=20)
        self.encodeButton.pack(side=LEFT,padx=20,pady=5,ipadx=20)
        self.saveFileButton.pack(fill=X,padx=20,pady=5,ipadx=20)



    def openfile(self):
        self.filename =  askopenfilename(initialdir="C:\\",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        self.frame.focus()
        self.fileContent.delete(1.0,END)
        for line in lines:
            self.fileContent.insert(END,line)
        """encoded = [Cesar.encode(i,5) for i in myNames]
        self.output_file = asksaveasfilename(initialdir = "C:\\Users\\rafaa\\Desktop",title = "Save encoded file",filetypes = (("text files","*.txt"),("all files","*.*")))
        with open(self.output_file+".txt", 'w') as f:
            for item in encoded:
                f.write("%s\n" % item)"""
    def encode(self):
        text = self.fileContent.get(1.0,END)
        key = int(self.keyContent.get(1.0, END))
        encoded = Cesar.encode(text,key)
        self.fileContent.delete(1.0, END)
        self.fileContent.insert(END, encoded)
    def export(self):
        text = self.fileContent.get(1.0, END)
        self.output_file = asksaveasfilename(initialdir="C:\\", title="Save encoded file",
                                             filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        with open(self.output_file + ".txt", 'w') as f:
            f.write("%s\n" % text)





