from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title("Test")
root.geometry("400x250")

def skrivutnamn(namn):
    print("Hello "+namn)
    print("Bye "+namn)

def skrivutnamnpåskärm(namn):
    return "Hello "+namn+ "\n Bye "+namn


skrivutnamn("mayson")
skrivutnamn("Jocke")
skrivutnamn("Adam")
skrivutnamn("Loke")
skrivutnamn("Greger")
T = Text(root, height=4, width=50)
#img = ImageTk.PhotoImage(Image.open("test2.jpg"))
#photo=PhotoImage(file='../test2.jpg')
B = Button(root, height=4, width=50, text="Hej")
T.pack()
T.insert(END, skrivutnamnpåskärm("mayson"))
B.pack()

root.mainloop()
