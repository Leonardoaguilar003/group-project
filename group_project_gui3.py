#importing tkinter, geopy(location), timezonefinder + datetime(display of time), requests from API, PIL(resizing images)
#pytz(date time conversion)
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import ImageTk, Image





def getWeather():
    # Creating time display
    city=textfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj = TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="Current Time")
    
    # Creating API requests and specifying the data we want to display 
    try:
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=2501263731530d63d7ea9b0c6e7fd60e"
        agent = requests.get(api).json()

        temp = int((agent['main']['temp']-273.15)*9/5+32)
        d.config(text=(temp, "℉"))
        

        humidity = agent['main']['humidity']
        h.config(text=(humidity,"%"))
    
        pressure = agent['main']['pressure']
        p.config(text=(pressure, "HPA"))
        
        wind = agent['wind']['speed']
        w.config(text=(wind,"m/s"))
    
    #Creating message box for input validation
    except Exception as e:
        messagebox.showerror("weather app","Invalid Entry, Please enter a valid city.")
        
    
    
#Creating Display Window
root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)
#root.configure(bg="cyan")


#create and place search box frame
Search_image=PhotoImage(file="C:\\Users\\laxhx\OneDrive\\Desktop\\PNG's\\search box.png") 
myimage=Label(image=Search_image)
myimage.place(x=220,y=20)



#create and place search box + user input
textfield=tk.Entry(root,justify="center",width=19,font=("Helvetica",25,"bold"), bg="#404040",border=1,fg="white")
textfield.place(x=275,y=40)
textfield.focus()
textfield.insert(INSERT,"Please enter a City!")


#search icon
search_icon=PhotoImage(file="C:\\Users\\laxhx\\OneDrive\\Desktop\\PNG's\\search_icon.png")
myimage_icon=Button(image=search_icon, borderwidth=0,cursor="hand1",bg="#404040", command=getWeather)
myimage_icon.place(x=600,y=34)

#time
name=Label(root,font=("Helvetica",15,"bold"))
name.place(x=100,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=100,y=130)



#Create and place windy logo
logo_image=Image.open("C:\\Users\\laxhx\\OneDrive\\Desktop\\PNG's\\windy logo.png")
resized=logo_image.resize((90,90))
new_logo=ImageTk.PhotoImage(resized)
myimage_logo=Label(image=new_logo)
myimage_logo.place(x=100, y=300)


#Create a humidty logo
logo_image1=Image.open("C:\\Users\\laxhx\\OneDrive\\Desktop\\PNG's\\humidity.png")
resized=logo_image1.resize((105,65))
new_logo1=ImageTk.PhotoImage(resized)
myimage_logo1=Label(image=new_logo1)
myimage_logo1.place(x=235, y=315)

#Create a temperature logo
logo_image2=Image.open("C:\\Users\\laxhx\\OneDrive\\Desktop\\PNG's\\temperature logo.png")
resized=logo_image2.resize((60,60))
new_logo2=ImageTk.PhotoImage(resized)
myimage_logo2=Label(image=new_logo2)
myimage_logo2.place(x=450, y=315)

#create pressure Logo
logo_image3=Image.open("C:\\Users\\laxhx\\OneDrive\\Desktop\\PNG's\\pressure logo.png")
resized=logo_image3.resize((80,80))
new_logo3=ImageTk.PhotoImage(resized)
myimage_logo3=Label(image=new_logo3)
myimage_logo3.place(x=660, y=310)

 
#Create main logo
logo_image4=Image.open("C:\\Users\\laxhx\\OneDrive\\Desktop\\PNG's\\main logo.png")
resized=logo_image4.resize((200,200))
new_logo4=ImageTk.PhotoImage(resized)
myimage_logo4=Label(image=new_logo4)
myimage_logo4.place(x=385, y=100)


#create and place bottom display box
frame_image=PhotoImage(file="C:\\Users\\laxhx\\OneDrive\\Desktop\\PNG's\\Copy of box.png") 
myframe_image=Label(image=frame_image)
myframe_image.pack(padx=5,pady=5, side=BOTTOM)

#create amd place headers + '...' within bottom display box
label1=Label(root,text="Wind",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)
label2=Label(root,text="Humidity",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)
label3=Label(root,text="Temperature",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)
label4=Label(root,text="Pressure",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("Helvetica",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("Helvetica",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("Helvetica",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("Helvetica",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("Helvetica",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("Helvetica",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)


root.mainloop()