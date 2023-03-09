import tkinter as tk
import requests
from tkinter import font

#Variables
HEIGHT =700
WIDTH=800

#TK Window
root = tk.Tk()

#Canvas
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

#Functions:
def test_function(entry):
    print ("This is the entry:",entry)

def get_weather(city):
    weather_key = "68355c4a56cee35b914c578a0f3f0d29"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q":city, "units": "metric"}
    response = requests.get(url, params=params)
    weather = response.json()
    
    label["text"] = format_response(weather)

def format_response(weather):
    name = weather["name"]
    desc = weather["weather"][0]["description"]
    temp = weather["main"]["temp"]
    final_str = """City: %s
Conditions: %s
Tempreture (ºC): %s""" % (name, desc, temp)
    return (final_str)

#background_image=tk.PhotoImage(file="mountain.png")
#background_label = tk.Label(root,image=background_image)
#background_label.place(relwidth=1,relheight=1)

#Frame
frame=tk.Frame(root,bg="#bae5f5",bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor="n")

#Entry
entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

#Button
button = tk.Button(frame,text="Get Weather",font=40,fg="gray",command=lambda:get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

#Lower Frame
lower_frame = tk.Frame(root,bg="#bae5f5",bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor="n")


#Label
label = tk.Label(lower_frame,bg="#f2eeb6", font=("Lucida Calligraphy",40))
label.place(relwidth=1,relheight=1)

root.mainloop()

