from tkinter import *
from tkinter import filedialog
import databasetogis



class Window1:
    def __init__(self, master):
        self.master = master
        master.title('Converter GUI')


        #button
        self.filebtn = Button(master, text="browse", command=self.importfile)
        self.dirbtn = Button(master, text='select directory', command=self.directory)
        self.okbtn = Button(master, text='Convert', command=self.convert)
        self.extbtn= Button(master, text='Exit', command=quit)

        #button location

        self.filebtn.grid(row=0,column=0)
        self.dirbtn.grid(row=2,column=0)
        self.okbtn.grid(row=4,column=0)
        self.extbtn.grid(row=6, column=0)
        #set labels
        global dirpath, filepath, conpath

        filepath=Label(master)
        filepath.grid(row=0, column=1)
        dirpath = Label(master)
        dirpath.grid(row=2,column=1)
        conpath=Label(master)
        conpath.grid(row=4,column=1)

    def importfile(self):
        self.filename = filedialog.askopenfilename(initialdir='/', title="Select an CSV file", filetypes=(
            ('CSV', '*.csv'), ('allfiles', '*.*')))
        global fil
        fil = self.filename
        filepath.config(text=fil)

    # ask for directory
    def directory(self):
        self.directory = filedialog.askdirectory()
        global dirt
        dirt = self.directory
        dirpath.config(text=dirt)



    def convert(self):
        databasetogis.conversion(fil, dirt)
        conpath.config(text="Converted")



root=Tk()
root.geometry('500x200')
App = Window1(root)
root.mainloop()
