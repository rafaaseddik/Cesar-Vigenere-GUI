from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askopenfilename,asksaveasfilename

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pandas as pd
from PIL import Image, ImageTk
from dependencies.Cesar import *

class AnalyseGui(Frame):

    def __init__(self, master=None):
        self.frame = Toplevel(master)
        self.master = master
        self.init_window()
    #Creation of init_window
    def init_window(self):



        # creating labels
        self.mainTitle = Label(self.frame,text="Cesar Cryptanalizer",fg="red",font=("Courier", 20))
        self.keyLabel = Label(self.frame,text="Decoding Key",fg="red",font=("Courier", 20))
        # placing labels
        self.mainTitle.pack(fill=X)
        # creating buttons instances
        buttonFont = ("Helvetica", 15)

        self.openFileButton = Button(self.frame, text="Ouvrir un fichier", command = self.openfile,font=buttonFont)
        self.analyseButton = Button(self.frame, text="Analyser", command = self.analyse,font=buttonFont)
        self.decodeButton = Button(self.frame, text="Decoder", command = self.decode,font=buttonFont)
        self.saveFileButton = Button(self.frame, text="Exporter", command = self.export,font=buttonFont)

        # creating text area
        self.fileContent = Text(self.frame,height=20, width=100)
        self.keyContent = Text(self.frame,height=1, width=2,font=("Helvetica", 20))
        # making the key area readonly
        self.keyContent.bind("<Key>", lambda e: "break")


        # placing the button on my window
        self.openFileButton.pack(fill=X,padx=20,pady=5)
        self.fileContent.pack(fill=X,padx=20,pady=5)
        self.keyLabel.pack(side=LEFT,padx=20,pady=5)
        self.keyContent.pack(side=LEFT,padx=20,pady=5,ipadx=20)
        self.analyseButton.pack(side=LEFT,padx=20,pady=5,ipadx=20)
        self.decodeButton.pack(side=LEFT,padx=20,pady=5,ipadx=20)
        self.saveFileButton.pack(fill=X,padx=20,pady=5,ipadx=20)





    def openfile(self):
        self.filename =  askopenfilename(initialdir="C:\\",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        self.frame.focus()
        self.fileContent.delete(1.0,END)
        for line in lines:
            self.fileContent.insert(END,line)


    def analyse(self):
        self.plot_hist()
        text = self.fileContent.get(1.0, END)
        key = Cesar.analyse(text)
        self.keyContent.delete(1.0, END)
        self.keyContent.insert(END, key)
    def decode(self):
        text = self.fileContent.get(1.0,END)
        key = int(self.keyContent.get(1.0, END))
        decoded = Cesar.decode(text,key)
        self.fileContent.delete(1.0, END)
        self.fileContent.insert(END, decoded)
    def export(self):
        text = self.fileContent.get(1.0, END)
        self.output_file = asksaveasfilename(initialdir="C:\\", title="Save encoded file",
                                             filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        with open(self.output_file + ".txt", 'w') as f:
            f.write("%s\n" % text)

    def plot_hist(self):
        # Histogram
        hist_frame = Toplevel(self.master)
        df = pd.DataFrame(Cesar.histogram(self.fileContent.get(1.0,END)), columns=['char', 'frequency'])
        figure = plt.Figure(figsize=(6, 5), dpi=100)
        ax = figure.add_subplot(111)
        print(df['char'])
        ax.bar(Cesar.french_histo(None)[0],Cesar.french_histo(None)[1],label="histogramme de la langue FR")
        ax.bar(df['char'], df['frequency'],label="Text à decoder")
        ax.legend(loc='upper left')
        chart_type = FigureCanvasTkAgg(figure, hist_frame)
        chart_type.get_tk_widget().pack()
        # df.plot(kind='Chart Type such as bar', legend=True, ax=ax)
        ax.set_title('Frequence de chaque caractère')




