from tkinter import *
import requests
import json

window = Tk()
window.geometry('400x200')
window.title('IP Proxy Info')


def button_command_get():
    url = ('https://ipinfo.io/json')
    r = requests.get(url)
    data = json.loads(r.text)
    ip = data['ip']
    hostname = data['hostname']
    city = data['city']
    region = data['region']
    country = data['country']
    location = data['loc']
    organization = data['org']
    postal = data['postal']
    timezone = data['timezone']
    items = (f"IP Address: {ip}\nHostname: {hostname}\nCity: {city}\nRegion: {region}\nCountry: {country}\nLocation: {location}\nProvider: {organization}\nPostal: {postal}\nTimezone: {timezone}")
    print(items)
    ip_msg = f'Your {items}'
    output_text.set(ip_msg)
    
# Display Output
output_text = StringVar()
lbl_output = Label(window, textvariable=output_text)
lbl_output.pack()

Button(window, text="Get IP Info", command=button_command_get).pack()
       
window.mainloop()
    
