import requests
from tkinter import *

url = "http://api.open-notify.org/iss-now.json"

#Okno
window = Tk()
window.minsize(700, 400)
window.resizable(False, False)
window.title("ISS")

# Funkce
def iss_coordinates():
    response = requests.get(url)
    response.raise_for_status() #postara se o chbouvou hlasku
    data = response.json()
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    latitude_label["text"] = f"Zemepisna sirka ISS je: {latitude}"
    longitude_label["text"] = f"Zemeisna delka ISS je: {longitude}"


# Vozeni obrazku pomoci Canavasu
canavas = Canvas(window, width=500, height=280)
canavas.pack()
iss_img = PhotoImage(file="gif/iss.gif")
canavas.create_image(0, 0, anchor="nw", image=iss_img)

#Framy
coordinates_frame = Frame(window)
coordinates_frame.pack()

#Button
recount_button = Button(coordinates_frame, text="Soucasne souradnice ISS", command=iss_coordinates)
recount_button.pack()

#Labels
latitude_label = Label(font=("Helvetica", 12, "bold"))
latitude_label.pack(pady=7)
longitude_label = Label(font=("Helvetica", 12, "bold"))
longitude_label.pack()

window.mainloop()
