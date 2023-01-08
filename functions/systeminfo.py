import tkinter as tk
import subprocess
import threading
import sys

# --- Classes ---

class Redirect():

    #def __init__(self, widget, autoscroll=True):
    #    self.widget = widget
    #    self.autoscroll = autoscroll

    def write(self, text):
        self.widget.insert('end', text)
        #if self.autoscroll:
        #    self.widget.see("end")  # autoscroll
        
    #def flush(self):
    #    pass

# --- Functions ---

def run():
    threading.Thread(target=test).start()

def test():
    print("Thread: start")
    # traverse the info
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []

    # arrange the string into clear info
    for item in Id:
        new.append(str(item.split("\r")[:-1]))
    for i in new:
        print(i[2:-2])
    
    #p = subprocess.Popen("ping -c 4 stackoverflow.com".split(), stdout=subprocess.PIPE, bufsize=1, text=True)
    #while Id.poll() is None:
    #    msg = Id.stdout.readline().strip() # read a line from the process output
    #    if msg:
    #        print(msg)

    print("Thread: end")
"""
# --- Main ---

root = tk.Tk(className=' System Information')

# - Frame with Text and Scrollbar -

frame = tk.Frame(root)
frame.pack(expand=True, fill='both')

text = tk.Text(frame)
text.pack(side='left', fill='both', expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

text['yscrollcommand'] = scrollbar.set
scrollbar['command'] = text.yview

old_stdout = sys.stdout    
sys.stdout = Redirect(text)

# - rest -

button = tk.Button(root, text='Get Info', command=run)
button.pack()

root.mainloop()

# - after close window -

sys.stdout = old_stdout
"""
run()