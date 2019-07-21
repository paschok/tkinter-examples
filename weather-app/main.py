from tkinter import *
import requests


def getWeather(city):
    print('This is our entry: ', city)
    WEATHER_KEY = 'b01c45bb278636ecf782bf59ae2302ff'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': WEATHER_KEY, 'q': city, 'units': 'Metric'}
    response = requests.get(URL, params=params)
    weather = response.json()
    label['text'] = display_current_weather(weather)

    # b01c45bb278636ecf782bf59ae2302ff
    # api.openweathermap.org/data/2.5/weather?q={city name},{country code}


def display_current_weather(weather):
    try:
        city_name = weather['name']
        weather_desc = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        final_output = 'City: %s, \nConditions: %s, ' \
                       '\nTemperature(Celsius): %s' % (city_name, weather_desc, temperature)
    except:
        final_output = 'There was a problem retrieving your information'

    return final_output


root = Tk()
root.title('Weather App')
canvas = Canvas(root, height=500, width=600)
canvas.pack()

bg_image = PhotoImage(file='img/landscape.png')
bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor=N)

entry = Entry(frame, font=('MS UI Gothic', 20))
entry.place(relwidth=0.6, relheight=1)

button = Button(frame, text='Get weather', font=('MS UI Gothic', 15),
                command=lambda: getWeather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

weather_frame = Frame(root, bg='#80c1ff', bd=10)
weather_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor=N)

label = Label(weather_frame, font=('MS UI Gothic', 20), anchor=NW, justify=LEFT, bd=5)
label.place(relwidth=1, relheight=1)

root.mainloop()


