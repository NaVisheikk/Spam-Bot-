import pyautogui, time
from tkinter import *
window = Tk()
window.title("Spermer bot")
window.geometry('350x200')

lbl = Label(window, text="Click on the spam button to start", font=("Arial Bold",9))
lbl.grid(column=0, row=0)



def spam():
    time.sleep(5)
    filepath = open("textt", 'r')
    for word in filepath:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
btn= Button(window, text="Spam", bg="white", fg="black", command=spam)
btn.grid(column=1, row=0)

def instruc():
    lbl.configure(text="Enter Whatsapp, select a person then \n click on the spam button and\n then click again on the \n convo thennn \n let it rainnnnnnnnnnnnnnnnnnnnnnnnnnn \n    *navi*")
btn = Button(window, text="Instruction", command=instruc)
btn.grid(column=1, row=2)

lbl = Label(window, text="Navi")
lbl.grid(column=0, row=13)

window.mainloop()