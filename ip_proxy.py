from tkinter import *
import requests
window = Tk()
window.geometry('400x200')
window.title('IP Proxy Info')

def button_command_get():
    url = requests.get('http://ipinfo.io/json')
    print(url.text)
    ip_msg = f'Your ip info {url.text}'
    output_text.set(ip_msg)

# Display Output
output_text = StringVar()
lbl_output = Label(window, textvariable=output_text)
lbl_output.pack()

Button(window, text="Get IP Info", command=button_command_get).pack()
       
window.mainloop()