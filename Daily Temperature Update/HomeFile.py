import backclassfile as bcf
from tkinter import *
from PIL import ImageTk, Image

# Define resultFinal in the global scope
resultFinal = ""

def handle_login():
    global resultFinal
    city = city_input.get()
    s = bcf.TemperatureByLocation(city_input.get())
    resultFinal = s.TemperatureByLocation_fun()

    # Update the text of text_label1
    text_label1.config(text=resultFinal)

root = Tk()
root.title('Temperature details')
root.minsize(300, 400)
root.geometry('350x500')
root.configure(background='#0096DC')

img = Image.open('tempimage.png')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

text_label = Label(root, text='Temperature', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 20))

city_label = Label(root, text='Enter City Name', fg='white', bg='#0096DC')
city_label.pack(pady=(20, 5))
city_label.config(font=('verdana', 20))

city_input = Entry(root, width=50)
city_input.pack(ipady=6, pady=(1, 15))

login_btn = Button(root, text='Search', bg='White', fg='black', width=15, height=1, command=handle_login)
login_btn.pack(pady=(10, 10))
login_btn.config(font=('verdana', 20))

# Create text_label1 with an empty string
text_label1 = Label(root, text=resultFinal, fg='white', bg='#0096DC')
text_label1.pack()
text_label1.config(font=('verdana', 15))

root.mainloop()
