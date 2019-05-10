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
        self.filebtn.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.dirbtn.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.okbtn.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.extbtn.place(relx=0.5, rely=0.8, anchor=CENTER)
        #set lavels
        global dirpath, filepath

        filepath=Label(master)
        filepath.place(relx=0.1,rely=0.2)
        dirpath = Label(master)
        dirpath.place(relx=0.1, rely=0.4)

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


root=Tk()
root.geometry('600x200')
App = Window1(root)
root.mainloop()
