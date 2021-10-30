import tkinter
from PIL import Image
from PIL import ImageTk

import random

dict  = {'hey':['hi','hello','hey'],
         'hi':['hi','hello','hey'],
         'hello':['hi','hello','hey'],
         'who is your creator':['Pradyumn Kumar Pandey','My Creator is Pradyumn Kumar Pandey'],
         'who is your inventor':['Pradyumn Kumar Pandey','I am invented by Pradyumn Kumar Pandey'],
         'creator':['Pradyumn Kumar Pandey','My Creator is Pradyumn Kumar Pandey'],
         'name':['Nia',"I'm Nia, The Chatbot"],
         'what is your name':['Nia',"I'm Nia, The Chatbot"],
         'age':['I"m Young XD'],
         'introduction':['I am Nia, the Chatbot. I am created by Pradyumn Kumar pandey, a prefinal year student at SIET, Prayagraj.']
         }
#dictionary to questions.

def reply():
    msg=user_text.get("1.0","end-1c")
    msg=msg.lower()
    if not msg:
        reply_bot.config(text="Please Enter Some Text")
        return
    if msg in dict.keys():
        ind=random.randint(0,len(dict[msg])-1)
        rep=dict[msg][ind]
    else:
        rep="Currently I Don't Have Any Answer To This" 
    reply_bot.config(text=rep)

#function created for the bot to reply to the user    



#Code for the GUI starts here.
window=tkinter.Tk()
window.title('CHATBOT')
window.geometry('750x500')
window.iconbitmap('bot.ico')
window.resizable(width=False,height=False)
intro=tkinter.Label(window,text='CHATBOT',font=('Algerian',20))
intro.place(x=325)

#bot image display in window.
myimg = Image.open('bot.png')
myimage = myimg.resize((100,100))
img = ImageTk.PhotoImage(myimage)


label1=tkinter.Label(window,image=img)
label1.image=img
label1.place(x=0,y=30)


msg1=tkinter.Label(window,text="Hey, Kindly type your message in the textbox to talk")
msg1.place(x=0,y=130)

msg2=tkinter.Label(window,text="Enter Message Here: ")
msg2.place(x=0,y=220)


#user entry box.
user_text=tkinter.Text(window,height=2,width=65)
user_text.place(x=120,y=220)

send_btn=tkinter.Button(window,text="Send",command=lambda:reply())
send_btn.place(x=650,y=220)


label2=tkinter.Label(window,text="BOT's Reply")
label2.place(x=335,y=300)


reply_bot=tkinter.Label(window,text='',width=98)
reply_bot.place(x=25,y=325)

#label created to display the reply given by bot.

window.mainloop()

#end of code........