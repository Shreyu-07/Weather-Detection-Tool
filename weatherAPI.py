import requests # pip install requests
import time # pip install time
import pyfiglet # pip install pyfiglet
from termcolor import colored # pip install termcolor
import pyttsx3 as sp # pip install pyttsx3
from tkinter import * # pip install tkinter

window = Tk()
window.geometry("400x400")
window.title("Weather detection")
window.config(background="black")

label = Label(window, text="Welcome to weather detection", font=("Arial", 20, "bold"), background="black", fg="white")
label.pack()

Label(window, text='Its me Shreyas', fg='white', bg="black", font=("Arial", 15)).pack()

photoOfWeather = PhotoImage(file="Lovepik_com-401059349-weather-vector-icon.png")
photoOfWeather = photoOfWeather.subsample(5, 10)
Label(window, image=photoOfWeather).pack()

# Scrollable Text Frame
frame = Frame(window, bg="black")
frame.pack(fill=BOTH, expand=True)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

output = Text(frame, yscrollcommand=scrollbar.set, bg="black", fg="white", font=("Arial", 14), wrap=WORD)
output.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar.config(command=output.yview)
# -------------------------------------------------------------------------------------------------
a = "welcome to weather detction tool"
b = a.upper()
fig = pyfiglet.figlet_format(b)
print(colored(fig, "light_blue"))
talk = sp.init()
talk.getProperty("rate")
talk.setProperty("rate", 100)
talk.say("welcome to weather detction tool")
talk.runAndWait()

nameOfTheplace = input("Enter the name of the palce : ")

url = "http://api.openweathermap.org/geo/1.0/direct"  # Geocoding API
url1 = "https://api.openweathermap.org/data/2.5/weather"  # Weather API

params = {
    "q": nameOfTheplace,
    "limit": "5",
    "appid": "9e52f00c9bdd9e0e54b17d861f6a5fa9"
}

respons = requests.get(url=url, params=params)

if respons.status_code == 200:
    output.insert(END, "Connecting to the Satellite...\n")
    for i in range(1, 6):
        output.insert(END, f"Testing {i} done\n")
        print(f"Testing {i} done")
        time.sleep(0.8)

    data = respons.json()
    Name = data[0]['name']
    country = data[0]['country']
    state = data[0]['state']
    lat = data[0]['lat']
    lon = data[0]['lon']
    print("The data assign is done")
    output.insert(END, "The data assign is done\n")

else:
    print('Failed (Geocoding API):', respons.status_code)
    output.insert(END, f"Failed (Geocoding API): {respons.status_code}\n")

params1 = {
    'lat': lat,
    'lon': lon,
    'appid': '9e52f00c9bdd9e0e54b17d861f6a5fa9'
}

respons1 = requests.get(url=url1, params=params1)

if respons1.status_code == 200:
    data1 = respons1.json()
    output.insert(END, f"\nName: {Name}\n")
    print('Name:', Name)
    output.insert(END, f"State: {state}\n")
    print('State:', state)
    output.insert(END, f"Latitude: {lat}\n")
    print('Latitude:', lat)
    output.insert(END, f"Longitude: {lon}\n")
    print('Longitude:', lon)
    output.insert(END, f"Main: {data1['weather'][0]['main']}\n")
    print('Main:', data1["weather"][0]["main"])
    output.insert(END, f"Description: {data1['weather'][0]['description']}\n")
    print('Description:', data1["weather"][0]["description"])
    output.insert(END, f"Temperature: {data1['main']['temp']}\n")
    print('Temperature:', data1["main"]['temp'])
    output.insert(END, f"Wind Speed: {data1['wind']['speed']}\n")
    print('Wind Speed:', data1["wind"]["speed"])

else:
    print("Failed (Weather API):", respons1.status_code)
    output.insert(END, f"Failed (Weather API): {respons1.status_code}\n")

window.mainloop()
