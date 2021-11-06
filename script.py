from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import base64
import requests
import subprocess

try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3


window=Tk()
window.geometry("700x700")

#width = screen.get_width()
#height = screen.get_height()
w = 700
h = 700

p = None

def learn_press():
        global learnClicked
        global p
        learnClicked = True
        # subprocess.call("ls -l")
        p = subprocess.Popen(["python3", "solved_hammer.py"])
        # subprocess.run(["python3", "solved_hammer.py"])
        print("LEARN!")

def play_press():
        global playClicked
        global p
        playClicked = True
        # subprocess.run(["python3", "main.py"])
        p = subprocess.Popen(["python3", "main.py"])
        print("PLAY!")

def exit_press():
        global exitClicked
        exitClicked = True
        print("EXIT!")
        p.terminate()
        window.destroy()

learnClicked = False
playClicked = False
exitClicked = False

style = Style()

style.configure('W.TButton', font =
               ('helvetica', 20, 'bold'),
                foreground = "#fe966e", background = "#0c9eb6", height = 150, width = 20)

# add widgets here

l = Label(window, text = "Test you skill!")
l.config(font =("helvetica", 30), foreground = "#0c9eb6", background = 'white')
#l.pack()
l.place(relx=0.5, rely=0.1, anchor=CENTER)

learn=Button(window, text="Learn!", style = 'W.TButton', command=learn_press)
learn.place(relx=0.5, rely=0.6, anchor=CENTER)

play=Button(window, text="Play!", style = 'W.TButton', command=play_press)
play.place(relx=0.5, rely=0.7, anchor=CENTER)

exit=Button(window, text="Exit!", style = 'W.TButton', command=exit_press)
exit.place(relx=0.5, rely=0.85, anchor=CENTER)


url = "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/f1a84856240191.59a64e6d80c00.jpg"
r = requests.get(url)
#pilImage = Image.open(StringIO(r.content))
pilImage = Image.open(BytesIO(r.content))
pilImage = pilImage.resize((200, 200), Image.ANTIALIAS)

image = ImageTk.PhotoImage(pilImage)

label = Label(image=image)
#label.pack()
label.place(relx=0.5, rely=0.35, anchor=CENTER)


window.configure(background='white')
window.title('Your AI Friend')
window.mainloop()
