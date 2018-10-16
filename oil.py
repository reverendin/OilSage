from tkinter import *
from tkinter import messagebox
import vin

#def vin_ok():
 # if vin.get_vin(ok_text) == "short":
 #   messagebox.showerror("Error", "Error message", parent=vin_win)


def search_vin():
  vin_win=Tk()
  vin_win.wm_title('Search by Vin')
  vin_win.wm_attributes('-topmost', 1)
  vin_win.focus()
  w=str(vin_win.winfo_screenwidth()//4)
  h=str(vin_win.winfo_screenheight()//3)
  vin_win.geometry(f'800x200+{w}+{h}')

  def vin_ok():
    if vin.get_vin(ok_text) == "short":
      messagebox.showerror("Error", "Vin Must Be 17 Characters", parent=vin_win)
      search_entry.delete(0, END)

  vin_text = StringVar()
  vin_win.grid_columnconfigure(0, weight=1)
  vin_win.grid_columnconfigure(3, weight=1)
  title_label=Label(vin_win, text='Search by Vin', font=('Helvetica', 16))
  title_label.grid(row=0, column=1, columnspan=2, pady=(40,0))
  search_label = Label(vin_win, text="Enter Vin: ", pady=20, padx=20, font=('Helvetica',16))
  search_label.grid(row=1, column=1)
  search_entry = Entry(vin_win,textvariable = vin_text, font=('Helvetica', 16))
  search_entry.grid(row=1, column=2, padx=(0,40))
  cancel_button = Button(vin_win, text='Cancel', font=('Helvetica', 16), command=vin_win.destroy)
  cancel_button.grid(row=2,column = 1, pady=(0, 20), padx=(80,0))
  global ok_text
  ok_text = vin_text.get()
  ok_button = Button(vin_win, text='OK', font = ('Helvetica', 16), command=vin_ok)
  ok_button.grid(row=2,column=2, pady=(0,20))

window=Tk()

window.wm_title("Oil Sage")
#window.overrideredirect(True)
#window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.attributes('-zoomed', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(3, weight=1)
#window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_columnconfigure(4, weight=1)


l1=Label(window,text='Search Method', pady=40, font=('Helvetica', 32))
l1.grid(row=1, column=2)
b1=Button(window, text="Vin", height=1, width=8, font=('Helvetica', 16), command=search_vin)
b1.grid(row=2, column= 1)
b2=Button(window, text='Make/Model', font=('Helvetica', 16))
b2.grid(row=2, column=3)

window.mainloop()
