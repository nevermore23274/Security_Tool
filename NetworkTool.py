import customtkinter
import subprocess
from functions.systeminfo import *

# Default appearance
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


class App(customtkinter.CTk):
   def __init__(self):
      super().__init__()

      # --- Main ---

      self.title("Network Tool")
      # Set window size
      self.geometry(f"{1100}x{580}")
      # set grid layout 1x2
      #self.grid_rowconfigure(0, weight=1)
      #self.grid_columnconfigure(1, weight=1)
      # configure grid layout (4x4)
      self.grid_columnconfigure(1, weight=1)
      self.grid_columnconfigure((2, 3), weight=0)
      self.grid_rowconfigure((0, 1, 2), weight=1)

      # create navigation frame
      self.navigation_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
      self.navigation_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
      self.navigation_frame.grid_rowconfigure(4, weight=1)
      self.logo_label = customtkinter.CTkLabel(self.navigation_frame, text="App Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
      self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

      # System info frame
      self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="System Info",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.print_to_gui)
      self.home_button.grid(row=1, column=0, sticky="ew")
      
      # DNS info frame
      self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="DNS Info",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.dns_info)
      self.frame_2_button.grid(row=2, column=0, sticky="ew")

      # DVWA Search frame
      self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="DVWA Search",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.dvwa_search)
      self.frame_3_button.grid(row=3, column=0, sticky="ew")

      # Appearance and scaling frames
      self.appearance_mode_label = customtkinter.CTkLabel(self.navigation_frame, text="Appearance Mode:", anchor="w")
      self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
      self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
      self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=10, sticky="s")
      self.scaling_label = customtkinter.CTkLabel(self.navigation_frame, text="UI Scaling:", anchor="w")
      self.scaling_label.grid(row=7, column=0, padx=20, pady=(20, 0))
      self.scaling_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
      self.scaling_menu.grid(row=8, column=0, padx=20, pady=(10, 20))

      # create home frame
      self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
      self.home_frame.grid_columnconfigure(0, weight=1)
      
      self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="")
      self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
      
      self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="")
      self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
      self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", compound="right")
      self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
      self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", compound="top")
      self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
      self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", compound="bottom", anchor="w")
      self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)
      
      # create textbox
      self.textbox = customtkinter.CTkTextbox(self, width=250)
      self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

      # create second frame
      self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
      
      # create third frame
      self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

      # Default values
      self.scaling_menu.set("100%")
      self.appearance_mode_menu.set("Dark") # Modes: system (default), light, dark
      self.textbox.insert("0.0", "")


   # --- Functions ---

   # Display a string in `out_label`
   def print_to_gui(self):
      self.textbox.insert("0.0", run())

   def run_program(self):
      subprocess.call(["python", "functions/my_python_program.py"])

   def system_info(self):
      subprocess.call(["python", "functions/systeminfo.py"])

   def dns_info(self):
      subprocess.call(["python", "functions/dnsinfo.py"])

   def dvwa_search(self):
      subprocess.call(["python", "functions/dvwa_search.py"])
   
   def change_appearance_mode_event(self, new_appearance_mode):
      customtkinter.set_appearance_mode(new_appearance_mode)
   
   def change_scaling_event(self, new_scaling: str):
      new_scaling_float = int(new_scaling.replace("%", "")) / 100
      customtkinter.set_widget_scaling(new_scaling_float)
   
   def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "system_info" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "dnsinfo" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "system_info":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "dnsinfo":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

if __name__ == "__main__":
   app = App()
   app.mainloop()