from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d0da23f3d5d98117c82081dcce75ebbe").json()
    wa_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data['weather'][0]['description'])
    temp_label1.config(text=str(int(data['main']['temp']-273.15)))
    per_label1.config(text=data['main']['pressure'])
    humidity_label1.config(text=data['main']['humidity'])
    wind_label1.config(text=data['wind']['speed'])

win=Tk()
win.title("Nishant kumar")
win.config(bg='aqua')



win.geometry("500x710")
name_label=Label(win,text='Weather Information',font=('Time New Roman',30,'bold'))
name_label.place(x=25,y=50,height=50,width=450)
city_name=StringVar()



list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa",
           "Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand",
           "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram",
           "Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
           "Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh",
           "Dadra and Nagar Haveli","Daman and Diu","Lakshadweep",
           "National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,values=list_name,font=('arial',20,'bold'),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)




wa_label=Label(win,text='Weather',font=('helvetica',20),bd=3,fg='#c45dc3')
wa_label.place(x=25,y=260,height=50,width=210)
wa_label1=Label(win,text='',font=('helvetica',20),bd=3)
wa_label1.place(x=250,y=260,height=50,width=210)

wb_label=Label(win,text='Weather Discription',font=('helvetica',17),bd=3,fg='#c45dc3')
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1=Label(win,text='',font=('helvetica',17),bd=3)
wb_label1.place(x=250,y=330,height=50,width=210)

temp_label=Label(win,text='Temperature',font=('helvetica',20),bd=3,fg='#c45dc3')
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1=Label(win,text='',font=('helvetica',20),bd=3)
temp_label1.place(x=250,y=400,height=50,width=210)

per_label=Label(win,text='Pressure',font=('helvetica',20),bd=3,fg='#c45dc3')
per_label.place(x=25,y=470,height=50,width=210)
per_label1=Label(win,text='',font=('helvetica',20),bd=3)
per_label1.place(x=250,y=470,height=50,width=210)

humidity_label=Label(win,text='Humidity',font=('helvetica',20),bd=3,fg='#c45dc3')
humidity_label.place(x=25,y=540,height=50,width=210)
humidity_label1=Label(win,text='',font=('helvetica',20),bd=3)
humidity_label1.place(x=250,y=540,height=50,width=210)

wind_label=Label(win,text='Wind speed',font=('helvetica',20),bd=3,fg='#c45dc3')
wind_label.place(x=25,y=610,height=50,width=210)
wind_label1=Label(win,text='',font=('helvetica',20),bd=3)
wind_label1.place(x=250,y=610,height=50,width=210)

done_button=Button(win,text='GET',font=('arial',20,'bold'),bg='aqua',fg='green',command=data_get)
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()