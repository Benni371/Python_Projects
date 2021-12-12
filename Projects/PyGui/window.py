from tkinter import *
from tkinter import font
from PIL import ImageTk,Image
from stats import Statistics
import time

master = Tk()
master.title("Whatever you Want")
master.geometry('1080x1920')
width = 1080
height = 1920

#declaration of variables
weather = StringVar(master, name ="weather")
alm = StringVar(master, name ="alm")
covid = StringVar(master, name ="covid")
aqi = Statistics("Air Quality")
weather = Statistics("Weather Forecast")
alm = Statistics("Daily Almanac")
hack = Statistics("Daily Hacker News")
aqiStats = aqi.get_AQI()
forecast = weather.get_weather()
# almanac = alm.get_almanac()
news = hack.get_news()




# configures each row to be responsive, Im really not sure why it works?
for i in range(3):
    master.rowconfigure(i, weight=1)
    master.columnconfigure(i, weight=1)

bgImage = ImageTk.PhotoImage(file="./images/webback.jpg")
qr = PhotoImage(file="./images/article.png", )
qr = qr.zoom(25)
qr = qr.subsample(32)


# Define 4 seperate canvases
canvas1 = Canvas(master, width=width/2, height=height/2, relief='raised')
canvas2 = Canvas(master, width=width/2, height=height/2, relief='raised')
canvas3 = Canvas(master, width=width/2, height=height/2, relief='raised')
canvas4 = Canvas(master, width=width/2, height=height/2, relief='raised')


# define which columns the canvas is in

canvas1.create_image(250, 250, image = bgImage)
canvas2.create_image(250, 250, image = bgImage)
canvas3.create_image(250, 250, image = bgImage)
canvas4.create_image(250, 250, image = bgImage)



# define the sizes of the rectangles and other attributes
# top left
headTr   = canvas1.create_rectangle(0, 50, width, 0, fill="white") 
bgLabel  = Label(canvas1,bg="green",width=45, height=17).place(relx=0.5,rely=0.2, anchor="n")
title    = Label(canvas1, text=aqi.name, font=("Helvetica",20),bg="white", fg="black").place(relx=0.5, rely=0.03, anchor='n') # top text
desc     = Label(canvas1, text=f"Reporting Area: { aqiStats['Area']}\n\nCategory: {aqiStats['Category']}\n\nAQI: { aqiStats['Quality']}" , font=("Helvetica",20), foreground="black", bg=aqiStats['Bg'])
desc.place(relx=0.5, rely=0.3, anchor='n')

#top right
headTl   = canvas2.create_rectangle(0, 50, width, 0,  fill="white") 
bgLabel2 = Label(canvas2, bg="green",width=45, height=17).place(relx=0.5,rely=0.2, anchor="n")
title2   = Label(canvas2, text="Weather", font=("Helvetica",20),bg="white", fg="black").place(relx=0.5, rely=0.03, anchor='n') # top text
desc2    = Label(canvas2, text=f"Reporting Area: { forecast['name']}\nTemp: {forecast['temp']}\nHigh: {forecast['high']}\nLow: { forecast['low']}" , font=("Helvetica",20), foreground="black", bg=aqiStats['Bg']).place(relx=0.5, rely=0.3, anchor='n') # top text

#bottom left
headBl   = canvas3.create_rectangle(0, 50, width, 0,  fill="white") 
bgLabel3 = Label(canvas3, bg="green",width=45, height=17).place(relx=0.5,rely=0.2, anchor="n")
title3   = Label(canvas3, text=aqi.name, font=("Helvetica",20),bg="white", fg="black").place(relx=0.5, rely=0.03, anchor='n') # top text
desc3    = Label(canvas3, text=f"Title: {news['Title']}" , font=("Helvetica",20), foreground="black", bg=aqiStats['Bg']).place(relx=0.5, rely=0.3, anchor='n') # top text
title3   = Label(canvas3,image=qr).place(relx=0.5, rely=0.5, anchor='n') # top text
#bottom right
headBr   = canvas4.create_rectangle(0, 50, width, 0,  fill="white") 
bgLabel4 = Label(canvas4, bg="green",width=45, height=17).place(relx=0.5,rely=0.2, anchor="n")
title4   = Label(canvas4, text=aqi.name, font=("Helvetica",20),bg="white", fg="black").place(relx=0.5, rely=0.7, anchor='n') # top text
desc4    = Label(canvas4, text=f"Reporting Area: { aqiStats['Area']}\nCategory: {aqiStats['Category']}\nAQI: { aqiStats['Quality']}" , font=("Helvetica",20), foreground="black", bg=aqiStats['Bg']).place(relx=0.5, rely=0.3, anchor='n') # top text



canvas1.grid(column=0, row=0, sticky='nwse')
canvas2.grid(column=1, row=0, sticky='nwse')
canvas3.grid(column=0, row=1, sticky='nwse')
canvas4.grid(column=1, row=1, sticky='nwse')

master.mainloop()

def updateInfo():
    while True:
        print(1)