from tkinter import *
from tkinter import messagebox
import vin


def search_vin():
  vin_win=Tk()
  vin_win.wm_title('Search by Vin')
  vin_win.wm_attributes('-topmost', 1)
  vin_win.focus()
  w=str(vin_win.winfo_screenwidth()//4)
  h=str(vin_win.winfo_screenheight()//3)
  vin_win.geometry(f'800x200+{w}+{h}')
  def vin_ok():
    if vin.get_vin(search_entry.get()) == "short":
      messagebox.showerror("Error", "Vin Must Be 17 Characters", parent=vin_win)
      search_entry.delete(0, END)
    elif vin.get_vin(search_entry.get()) == "wrong_vin":
      messagebox.showerror("Error","That vin does not exist, Please Try Again", parent=vin_win)
    else:
      car_details = vin.get_vin(search_entry.get())
      print(car_details)
      vin_win.destroy()
      display_info(car_details)

  def display_info(car_details):
    info_display=Tk()
    info_display.wm_title('Car Info')
    info_display.wm_attributes('-topmost', 1)
    info_display.focus()
    w=str(info_display.winfo_screenwidth()//4*3)
    h=str(info_display.winfo_screenheight()//2)
    #info_display.geometry(f'{w}x{h}')
    info_display.attributes('-zoomed', True)
    info_display.grid_columnconfigure(0, weight=1)
    info_display.grid_columnconfigure(6, weight=1)
    info_display.grid_rowconfigure(0, weight=1)
    info_display.grid_rowconfigure(3, weight=1)
    info_display.grid_rowconfigure(6, weight=1)
    year_label = Label(info_display, text = f'Year : {car_details[2]}', font=('Helvetica',16)).grid(row=1, column=1)
    make_label = Label(info_display, text = f'Make : {car_details[0]}', font=('Helvetica',16)).grid(row=1, column=3)
    model_label = Label(info_display, text = f'Model : {car_details[1]}', font=('Helvetica',16)).grid(row=1, column =5)
    cylinder_label = Label(info_display, text = f'Engine : V{car_details[3]}', font=('Helvetica',16)).grid(row=2, column = 2)
    disp_label = Label(info_display, text = f'Engine Size : {str(car_details[4])}', font=('Helvetica',16)).grid(row=2, column = 4)
    weight_label = Label(info_display, text = 'Oil Weight : 0w20  ', font=('Helvetica',16)).grid(row=4, column=1)
    type_label = Label(info_display, text = 'Oil Type : synthetic  ', font=('Helvetica',16)).grid(row=4, column=2)
    quantity_label = Label(info_display, text = 'Oil Quantity : 4.5q  ', font=('Helvetica',16)).grid(row=4, column=3)
    plug_label = Label(info_display, text='Plug Torque : ', font=('Helvetica',16)).grid(row=4, column=4)
    ofilter_label = Label(info_display, text='Oil Filter : ',font=('Helvetica',16)).grid(row=4, column=5)
    afilter_label = Label(info_display, text='Air Filter : ',font=('Helvetica',16)).grid(row=5, column=2)
    cafilter_label = Label(info_display, text='Cabin Filter : ',font=('Helvetica',16)).grid(row=5, column=4)
    ok_button = Button(info_display, text='OK', font=('Helvetica',16), command=info_display.destroy).grid(row=6, column = 3)


  vin_win.grid_columnconfigure(0, weight=1)
  vin_win.grid_columnconfigure(3, weight=1)
  title_label=Label(vin_win, text='Search by Vin', font=('Helvetica', 16)).grid(row=0, column=1, columnspan=2, pady=(40,0))
  search_label = Label(vin_win, text="Enter Vin: ", pady=20, padx=20, font=('Helvetica',16)).grid(row=1, column=1)
  search_entry = Entry(vin_win, font=('Helvetica', 16))
  search_entry.grid(row=1, column=2, padx=(0,40))
  search_entry.focus_set()
  cancel_button = Button(vin_win, text='Cancel', font=('Helvetica', 16), command=vin_win.destroy).grid(row=2,column = 1, pady=(0, 20), padx=(80,0))
  ok_button = Button(vin_win, text='OK', font = ('Helvetica', 16), command=vin_ok).grid(row=2,column=2, pady=(0,20))

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