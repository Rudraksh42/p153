##https://www.loom.com/share/46bbad6520ca41bdbd34f7b9d39bb675

from tkinter import *
import random 
hello = Tk()
hello.title("hello")
hello.geometry("500x500")
hello.configure(bg  = "Light Blue")

entry1 = Entry(hello)
label1 = Label(hello)
label2 = Label(hello)

array =[[["Head" , "Tail", "Cat" , "Dog" , "Hello" , "hi" , "goal" , "Yo" , "nice", "puppet"],["A","B","C","D","E","F","G","H","I","J"],["-","+","*","&","^","%","$","#","@","!"]]]

  
def hi():
    item1 = entry1.get()
    print(item1)
    label1["text"] = "Password gussed is " + item1
      
    
    v1 = random.randint(0,9)
    v2 = random.randint(0,9)
    v3 = random.randint(0,9)
    
    letter1 = array[0][0][v1]
    letter2 = array[0][1][v2]
    letter3 = array[0][2][v3]
    label2["text"] = letter1 + letter2 + letter3
    
    
btn1 = Button(hello , text= "Click me to reveal the password", command=hi)
btn1.place(relx= 0.5 , rely = 0.6 , anchor =CENTER)
entry1.place(relx= 0.5, rely = 0.4, anchor = CENTER)
label1.place(relx= 0.5, rely = 0.5, anchor = CENTER)
label2.place(relx= 0.5, rely = 0.7, anchor = CENTER)
     
hello.mainloop()
