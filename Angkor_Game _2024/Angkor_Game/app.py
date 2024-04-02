import tkinter as tk
from PIL import ImageTk, Image
import webbrowser
import subprocess
import ctypes

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        # Get screen resolution
        user32 = ctypes.windll.user32
        width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        screen_resolution = f"{width}x{height}"
        
        self.root.geometry(screen_resolution)
        self.background_image = Image.open("background.jpg")
        self.background_image = self.background_image.resize((width, height))
        self.background_image = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create start world button
        self.gener_button = tk.Button(root, text="General Knowledge", font=("Copperplate Gothic Bold", 24), bg="green", fg="white", padx=20,
                                        pady=10, command=self.start_gener)
        self.gener_button.place(relx=0.830, rely=0.6, anchor=tk.CENTER)
        self.his_button = tk.Button(root, text="History Knowledge", font=("Copperplate Gothic Bold", 24), bg="green", fg="white", padx=20,
                                        pady=10, command=self.start_his)
        self.his_button.place(relx=0.85, rely=0.730, anchor=tk.CENTER)

        # Create Link button
        self.link_button = tk.Button(root, text="MY WEBSITE", font=("Eras Bold ITC", 18), bg="blue", fg="white", padx=20,
                                        pady=10, command=self.open_link)
        self.link_button.place(relx=0.0, rely=0.9, anchor='sw')

        # Create Profile button
        self.download_button = tk.Button(root, text="DOWNLOAD GAME", font=("Eras Bold ITC", 18), bg="red", fg="lime", padx=20,
                                        pady=10, command=self.open_download)
        self.download_button.place(relx=0.41, rely=0.9, anchor='se')
        
        
    def open_link(self):
        webbrowser.open("index.html")
    def open_download(self):
        webbrowser.open("https://drive.google.com/file/d/19fgA9KWtt6OUCno-AlK8dX6DhKwWlGMW/view?usp=drive_link")
        
    def start_gener(self):
        subprocess.run(["python", "general.py"])
        
    def start_his(self):
        subprocess.run(["python", "history.py"])
        
    
root = tk.Tk()
game = Game(root)
root.mainloop()
