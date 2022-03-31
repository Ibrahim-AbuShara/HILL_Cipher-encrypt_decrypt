# import tkinter module
from tkinter import *
from hill import start_decryption,start_encryption

# import other necessary modules
import random
import time
import datetime

# creating root object
root = Tk()

# defining size of window
root.geometry("1200x6000")

# setting up the title of window
root.title("Message Encryption and Decryption")

Tops = Frame(root, width = 1600, relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root, width = 800, height = 700,
							relief = SUNKEN)
f1.pack(side = LEFT)

# ==============================================
#				 TIME
# ==============================================
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'),
		text = "SECRET MESSAGING \n HILL cipher",
					fg = "Black", bd = 10, anchor='w')
					
lblInfo.grid(row = 0, column = 0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'),
			text = localtime, fg = "Steel Blue",
						bd = 10, anchor = 'w')
						
lblInfo.grid(row = 1, column = 0)

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# exit function
def qExit():
	root.destroy()

# Function to reset the window
def Reset():
	rand.set("")
	Msg.set("")
	key.set("")
	mode.set("")
	Result.set("")




# labels
lblMsg = Label(f1, font = ('arial', 16, 'bold'),
		text = "MESSAGE/CYPHER", bd = 16, anchor = "w")
		
lblMsg.grid(row = 1, column = 0)

txtMsg = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = Msg, bd = 10, insertwidth = 4,
				bg = "powder blue", justify = 'right')
				
txtMsg.grid(row = 1, column = 1)

lblkey = Label(f1, font = ('arial', 16, 'bold'),
			text = "KEY", bd = 16, anchor = "w")
			
lblkey.grid(row = 2, column = 0)

txtkey = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = key, bd = 10, insertwidth = 4,
				bg = "powder blue", justify = 'right')
				
txtkey.grid(row = 2, column = 1)

lblmode = Label(f1, font = ('arial', 16, 'bold'),
		text = "MODE(e for encrypt, d for decrypt)",
								bd = 16, anchor = "w")
								
lblmode.grid(row = 3, column = 0)

txtmode = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = mode, bd = 10, insertwidth = 4,
				bg = "powder blue", justify = 'right')
				
txtmode.grid(row = 3, column = 1)

lblService = Label(f1, font = ('arial', 16, 'bold'),
			text = "The Result-", bd = 16, anchor = "w")
			
lblService.grid(row = 2, column = 2)

txtService = Entry(f1, font = ('arial', 16, 'bold'),
			textvariable = Result, bd = 10, insertwidth = 4,
					bg = "powder blue", justify = 'right')
						
txtService.grid(row = 2, column = 3)





def Ref():
	print("Message= ", (Msg.get()))

	clear = Msg.get().lower()
	k = key.get().lower()
	m = mode.get().lower()

	if (m == 'e'):
		Result.set(start_encryption(k, clear))
	else:
		Result.set(start_decryption(k, clear))

# Show message button
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
						font = ('arial', 16, 'bold'), width = 10,
					text = "Show Message", bg = "powder blue",
						command = Ref).grid(row = 7, column = 1)

# Reset button
btnReset = Button(f1, padx = 16, pady = 8, bd = 16,
				fg = "black", font = ('arial', 16, 'bold'),
					width = 10, text = "Reset", bg = "green",
				command = Reset).grid(row = 7, column = 2)

# Exit button
btnExit = Button(f1, padx = 16, pady = 8, bd = 16,
				fg = "black", font = ('arial', 16, 'bold'),
					width = 10, text = "Exit", bg = "red",
				command = qExit).grid(row = 7, column = 3)

# keeps window alive
root.mainloop()
