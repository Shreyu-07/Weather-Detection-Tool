<h1 align="center">🌤️ Weather Detection Tool</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" />
  <img src="https://img.shields.io/badge/GUI-Tkinter-orange" />
  <img src="https://img.shields.io/badge/API-OpenWeatherMap-4A90E2" />
</p>

<p align="center">
  A sleek Python-based application to check real-time weather using a beautiful GUI, speech feedback, and a touch of terminal magic 🎩✨
</p>

---

## 🖥️ Demo

![Weather GUI](https://user-images.githubusercontent.com/your-image-url/weather-demo.png)

---

## 🚀 Features

✅ Stylish GUI with **Tkinter**  
✅ Real-time data using **OpenWeatherMap API**  
✅ Speech output using **pyttsx3**  
✅ ASCII-styled terminal intro via **pyfiglet**  
✅ Scrollable weather info display  
✅ Interactive testing animation 🛰️  
✅ Works on **Windows**, **Linux**, and **macOS**

---

## 🧰 Tech Stack

| Tool           | Purpose                    |
|----------------|----------------------------|
| `Python`       | Programming language       |
| `Tkinter`      | GUI framework              |
| `pyttsx3`      | Text-to-speech engine      |
| `pyfiglet`     | ASCII banner in terminal   |
| `termcolor`    | Colored terminal output    |
| `requests`     | API calls                  |
| `OpenWeatherMap` | Real-time weather API    |

---

## 📦 Installation

### 1. Clone the Repo

bash

```git clone https://github.com/Shreyu-07/Weather-Detection-Tool.git```
```cd weather-detection-tool```

2. Install Dependencies
3. 
bash

pip install requests pyttsx3 pyfiglet termcolor

💡 tkinter is built-in with Python. If not, install it via your package manager:

bash

sudo apt-get install python3-tk  # For Ubuntu/Debian


3. Add Weather Icon
4. 
Place this image in your project folder:

cpp

Lovepik_com-401059349-weather-vector-icon.png

🛠️ How to Run
bash

python weather_gui.py

A GUI window will pop up 🪟


Enter the city name in the terminal ⌨️

Listen to the welcome message 🔊

Weather details will be shown in the GUI and terminal 🌡️

🌍 Example Output

██████████████████████████████████
WELCOME TO WEATHER DETECTION TOOL
██████████████████████████████████

Connecting to the Satellite...
Testing 1 done
...
Name       : Bengaluru
State      : Karnataka
Latitude   : 12.9716
Longitude  : 77.5946
Main       : Rain
Description: light rain
Temp       : 301.15 K
Wind Speed : 4.6 m/s


🔐 API Usage
This tool uses the OpenWeatherMap API. Get your free API key from:

🔗 https://openweathermap.org/api

Replace the appid in the code with your own key.

