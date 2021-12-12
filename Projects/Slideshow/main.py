import tkinter as tk
from typing import Counter
from PIL import Image, ImageTk
import random
import glob

class gui:
    def __init__(self, mainwin):
        self.counter = 0
        self.colorCount = 0
        self.mainwin = mainwin
        self.mainwin.title('Tkinter Picture Frame')
        try:
            self.mainwin.state('zoomed')
        except(tk.TclError):
            self.mainwin.maxsize()

        self.mainwin.configure(bg = 'yellow')

        self.frame = tk.Frame(mainwin)
        self.img = tk.Label(self.frame)
        self.frame.place(relheight=0.8, relwidth=0.9, relx = 0.05, rely=0.1)
        self.img.pack()

        self.pic()
        self.color()
        

    def color(self):
        self.colors = ['#a94343', '#bd4e33', '#db6735', '#d28546','#e5935b'] #autumn colors
        if self.colorCount == len(self.colors) - 1:
            self.colorCount = 0
        else:
            self.colorCount = self.colorCount + 1 
        c =  self.colors[self.colorCount]
        self.mainwin.configure(bg = c)
        self.frame.configure(bg = c)
        
        root.after(4000, self.color)
    def pic(self):
        self.pic_list = []
        for name in glob.glob(r'C:\Users\Koy Bennion\OneDrive - BYU\Desktop\Slideshow\photos\*'):
            val = name
            self.pic_list.append(val)
        
        if self.counter == len(self.pic_list)-1:
            self.counter = 0
        else:
            self.counter = self.counter + 1
        c = random.randrange(0, len(self.pic_list), 1)
        self.file = self.pic_list[c]

        self.load = Image.open(self.file)
        self.pic_width = self.load.size[0]
        self.pic_height = self.load.size[1]

        self.real_aspect = self.pic_width/self.pic_height
        self.cal_width = int(self.real_aspect * 800)
        self.load2 = self.load.resize((self.cal_width, 800))
        self.render = ImageTk.PhotoImage(self.load2)
        self.img.config(image = self.render)
        self.img.image = self.render
        root.after(4000, self.pic)





root = tk.Tk()
myprog = gui(root)
root.mainloop()
