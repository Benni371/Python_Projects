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
# color pallette
blue = "#0F2C67"
red = "#CD1818"
yellow = "#F3950D"
lightTan= "#F4E185"



# position of the inner background for the labels
innerBgX= 0.5
innerBgY= 0.2
innerBgHeight = 22
innerBgWidth = 60
# fonts for the labels
titleFont = ("Helvetica",20, "bold")
bodyFont = ("Impact", 20)


#create four different canvases to display separate data on
canvas1 = Canvas(master, width=width/2, height=height/2, relief='raised')
canvas2 = Canvas(master, width=width/2, height=height/2, relief='raised')
canvas3 = Canvas(master, width=width/2, height=height/2, relief='raised')
canvas4 = Canvas(master, width=width/2, height=height/2, relief='raised')


#declaration of object variables
aqi = Statistics("Air Quality")
weather = Statistics("Weather Forecast")
dad = Statistics("Dad Joke of the Day")
hack = Statistics("Daily Hacker News")
#Get the stats using objects
aqiStats = aqi.get_AQI()
forecast = weather.get_weather()
dadJoke = dad.get_joke()
news = hack.get_news()
# configures each row to be responsive, Im really not sure why it works?
for i in range(3):
    master.rowconfigure(i, weight=1)
    master.columnconfigure(i, weight=1)
#set the image for the background
bgImage = ImageTk.PhotoImage(file="./images/webback.jpg")
# make a image object for the qr code and resize it
qr = PhotoImage(file="./images/article.png", )
qr = qr.zoom(22)
qr = qr.subsample(40)


#create backgrounds for the images
canvas1.create_image(250, 250, image = bgImage)
canvas2.create_image(250, 250, image = bgImage)
canvas3.create_image(250, 250, image = bgImage)
canvas4.create_image(250, 250, image = bgImage)



# define the sizes of the rectangles and other attributes
# top left
headTl   = canvas1.create_rectangle(0, 50, width, 0, fill="white") 
bgLabel  = Label(canvas1,bg=yellow,width=innerBgWidth, height=innerBgHeight).place(relx=innerBgX,rely=innerBgY, anchor="n")
title    = Label(canvas1, text=aqi.name, font=titleFont,bg="white", fg="black").place(relx=0.5, rely=0.02, anchor='n') 
desc     = Label(canvas1, text=f"Reporting Area: { aqiStats['Area']}\n\nCategory: {aqiStats['Category']}\n\nAQI: { aqiStats['Quality']}" , font=bodyFont, foreground="black", bg=yellow)
desc.place(relx=0.5, rely=0.3, anchor='n')

#top right
headTr   = canvas2.create_rectangle(0, 50, width, 0,  fill="white") 
bgLabel2 = Label(canvas2,bg="green",width=innerBgWidth, height=innerBgHeight).place(relx=innerBgX,rely=innerBgY, anchor="n")
title2   = Label(canvas2, text=weather.name, font=titleFont,bg="white", fg="black").place(relx=0.5, rely=0.02, anchor='n') 
desc2    = Label(canvas2, text=f"Reporting Area: { forecast['name']}\nTemp: {forecast['temp']}\nHigh: {forecast['high']}\nLow: { forecast['low']}" , font=bodyFont, foreground="black", bg=aqiStats['Bg']).place(relx=0.5, rely=0.3, anchor='n') 

#bottom left
headBl   = canvas3.create_rectangle(0, 50, width, 0,  fill="white") 
bgLabel3 = Label(canvas3,bg="green",width=innerBgWidth, height=innerBgHeight).place(relx=innerBgX,rely=innerBgY, anchor="n")
title3   = Label(canvas3, text=hack.name, font=titleFont,bg="white", fg="black").place(relx=0.5, rely=0.02, anchor='n') 
desc3    = Label(canvas3, text=f"{news['Title']}" , font=bodyFont, foreground="black", bg=aqiStats['Bg'], wraplength=300).place(relx=0.5, rely=0.25, anchor='n') 
qrCode   = Label(canvas3,image=qr).place(relx=0.5, rely=0.4, anchor='n') 

#bottom right
headBr   = canvas4.create_rectangle(0, 50, width, 0,  fill="white") 
bgLabel4 = Label(canvas4,bg="green",width=innerBgWidth, height=innerBgHeight).place(relx=innerBgX,rely=innerBgY, anchor="n")
title4   = Label(canvas4, text=dad.name, font=titleFont,bg="white", fg="black").place(relx=0.5, rely=0.02, anchor='n') 
desc4    = Label(canvas4, text=f"{dadJoke}" , font=bodyFont, foreground="black", bg=aqiStats['Bg'],wraplength=300).place(relx=0.5, rely=0.3, anchor='n') 

# places columns in their respective positions
canvas1.grid(column=0, row=0, sticky='nwse')
canvas2.grid(column=1, row=0, sticky='nwse')
canvas3.grid(column=0, row=1, sticky='nwse')
canvas4.grid(column=1, row=1, sticky='nwse')

master.mainloop()
