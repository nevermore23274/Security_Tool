import psutil
from tkinter import *

root = Tk()

# Get system uptime
uptime = psutil.boot_time()

# Get CPU usage
cpu_percent = psutil.cpu_percent()

# Get memory usage
virtual_memory = psutil.virtual_memory()

# consolidate the System info
text="System uptime: " + str(uptime) + "\n" + "CPU usage: " + cpu_percent + "\n" + "Virtual memory usage: "+ virtual_memory + "\n" 

# Create a Label widget
label = Label(root, text=text)

# Pack the Label widget
label.pack()

root.mainloop()
