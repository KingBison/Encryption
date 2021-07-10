from typing import Collection
from Decoder import Decoder
from Encoder import Encoder
from Encryption_Key import Encryption_Key


from tkinter import *

root = Tk()




message_label = Label(root, text="Message",padx=15,pady=15)
message_box = Entry(root)
choice_label = Label(root, text="Encrypt or Decrypt",padx=15,pady=15)
choice = StringVar(root)
choice.set("Encrypt") # default value
choice_menu = OptionMenu(root, choice, "Encrypt", "Decrypt",)
key_label = Label(root, text="Key Used",padx=15,pady=15)
key_box = Entry(root)
result_label = Label(root, text="",padx=15,pady=15)

spacers = Label(root, text="                 ",padx=15,pady=15)

new_key_label= Label(root, text="New Key",padx=15)
new_key_entry = Entry(root)
new_key_message = Label(root, text="")


def compute():
    new_key_message.config(text="")
    if key_box.get() == "":
        print("Missing Key")
    elif message_box.get() == "":
        print("Missing Message")
    else:
        try:
            
            key_file=open(key_box.get()+".txt")
            key_file.close() 
            key = Encryption_Key()
            key.subKeyFromTxt(key_box.get())

            if choice.get() == "Decrypt":
                decoder = Decoder(key.getKey())
                print("check")
                out = decoder.decrypt(message_box.get())
                print("check2")
                result_label.config(text=out)
            else:
                encoder = Encoder(key.getKey())
                print("checkE")
                out = encoder.encrypt(message_box.get())
                print("check2E")
                result_label.config(text=out)
            
        
        except:
            print("key unavailable")


def generateNewKey():
    if new_key_entry.get() == "":
        print("Key Name Missing")
    else:
        new_key=Encryption_Key()
        new_key.saveKey(new_key_entry.get())
        new_key_message.config(text="Key Created!")


compute_button = Button(root, text="Compute", command=compute)
new_key_button = Button(root, text="Generate", command=generateNewKey)



message_label.grid(column=0, row=0)
choice_label.grid(column=0, row=1)
key_label.grid(column=0, row=2)
message_box.grid(column=1, row=0)
choice_menu.grid(column=1, row=1)
key_box.grid(column=1, row=2)
compute_button.grid(column=0, row=3)
result_label.grid(column=1,row=3)
spacers.grid(column=2, row=0)

new_key_label.grid(column=3,row=0)
new_key_entry.grid(column=3,row=1)
new_key_button.grid(column=3,row=2)
new_key_message.grid(column=3,row=3)


root.mainloop()







        





