import tkinter as tk
import CreateFile
Window = tk.Tk()
Window.title("Shmup Creator ULTRA")
Window.geometry("800x600")
Title = tk.Label(text = "Shmup Creator ULTRA", font = ("", 25))
Title.pack()
CreateFile.CreateFile("game.bsc", "ULTRAgame.bsc")
Window.mainloop()