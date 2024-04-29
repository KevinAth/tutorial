import tkinter as tk
import sys
class funcionG(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ventana")
        self.geometry("300x300")
        etiqueta = tk.Label(self,text="Hola mundo")
        etiqueta.pack()
        
    
    
    
if __name__ == "__main__":
    app = funcionG()
    app.mainloop()
