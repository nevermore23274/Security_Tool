# import modules
from tkinter import *
from tkinter import messagebox
from iplookup import iplookup
import whois

# user define function
# for get domain information
def Domain_info():
    try:
        domain = whois.whois(str(e1.get()))
        ip = iplookup.iplookup
        result = ip(e1.get())

        res.set(result)
        server.set(domain.whois_server)
        exp_date.set(domain.expiration_date)
        reg_name.set(domain.name)
        org.set(domain.org)
        state.set(domain.state)
        city.set(domain.city)
        country.set(domain.country)
    except:
        messagebox.showerror("showerror", "Something went wrong.")
 
 
# object of tkinter
# and background set for red
master = Tk(className=' DNS Lookup Tool')
 
# Variable Classes in tkinter
server = StringVar()
res = StringVar()
exp_date = StringVar()
reg_name = StringVar()
org = StringVar()
state = StringVar()
city = StringVar()
country = StringVar()
 
# Creating label for each information
# name using widget Label
Label(master, text="Website URL: ").grid(row=0, sticky=W)
Label(master, text="IP: ").grid(row=2, sticky=W)
Label(master, text="Server Name:").grid(row=3, sticky=W)
Label(master, text="Expiration date:").grid(row=4, sticky=W)
Label(master, text="Register name:").grid(row=5, sticky=W)
Label(master, text="Origination:").grid(row=6, sticky=W)
Label(master, text="State:").grid(row=7, sticky=W)
Label(master, text="City:").grid(row=8, sticky=W)
Label(master, text="Country:").grid(row=9, sticky=W)

# Creating label for class variable
# name using widget Entry
Label(master,text="", textvariable=res).grid(row=2, column=1, sticky=W)
Label(master, text="", textvariable=server).grid(row=3, column=1, sticky=W)
Label(master, text="", textvariable=exp_date).grid(row=4, column=1, sticky=W)
Label(master, text="", textvariable=reg_name).grid(row=5, column=1, sticky=W)
Label(master, text="", textvariable=org).grid(row=6, column=1, sticky=W)
Label(master, text="", textvariable=state).grid(row=7, column=1, sticky=W)
Label(master, text="", textvariable=city).grid(row=8, column=1, sticky=W)
Label(master, text="", textvariable=country).grid(row=9, column=1, sticky=W)

e1 = Entry(master)
e1.grid(row=0, column=1)
 
# creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Show", command=Domain_info)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)
 
mainloop()