import mysql.connector
import db_config as cfg
from tkinter import *


mydb = mysql.connector.connect(
  host=cfg.mysql['host'],
  user=cfg.mysql['user'],
  passwd=cfg.mysql['passwd'],
  database=cfg.mysql['database'],
)

cur =mydb.cursor()

window = Tk()

window.wm_title("Data Entry")

year_label = Label(window, text = 'Year: ').grid(row=1, column=1, padx=10, pady=5)
year_entry = Entry(window)
year_entry.grid(row=1, column=2, padx=10)
year_entry.focus()

make_label = Label(window, text = 'Make: ').grid(row=2, column=1, padx=10, pady=5)
make_entry = Entry(window)
make_entry.grid(row=2, column=2, padx=10)

model_label = Label(window, text = 'Model: ').grid(row=3, column=1, padx=10, pady=5)
model_entry = Entry(window)
model_entry.grid(row=3, column=2, padx=10)

cyl_label = Label(window, text = 'Cylinders: ').grid(row=4, column=1, padx=10, pady=5)
cyl_entry = Entry(window)
cyl_entry.grid(row=4, column=2, padx=10)

engSize_label = Label(window, text = 'Engine Size: ').grid(row=5, column=1, padx=10, pady=5)
engSize_entry = Entry(window)
engSize_entry.grid(row=5, column=2, padx=10)

weight_label = Label(window, text = 'Weight: ').grid(row=6, column=1, padx=10, pady=5)
weight_entry = Entry(window)
weight_entry.grid(row=6, column=2, padx=10)

type_label = Label(window, text = 'Oil Type: ').grid(row=7, column=1, padx=10, pady=5)
type_entry = Entry(window)
type_entry.grid(row=7, column=2, padx=10)

quantity_label = Label(window, text = 'Quantity: ').grid(row=8, column=1, padx=10, pady=5)
quantity_entry = Entry(window)
quantity_entry.grid(row=8, column=2, padx=10)

torque_label = Label(window, text = 'Torque: ').grid(row=9, column=1, padx=10, pady=5)
torque_entry = Entry(window)
torque_entry.grid(row=9, column=2, padx=10)

ofilter_label = Label(window, text = 'Oil Filter: ').grid(row=10, column=1, padx=10, pady=5)
ofilter_entry = Entry(window)
ofilter_entry.grid(row=10, column=2, padx=10)

afilter_label = Label(window, text = 'Air Filter: ').grid(row=11, column=1, padx=10, pady=5)
afilter_entry = Entry(window)
afilter_entry.grid(row=11, column=2, padx=10)

cafilter_label = Label(window, text = 'Cabin Filter: ').grid(row=12, column=1, padx=10, pady=5)
cafilter_entry = Entry(window)
cafilter_entry.grid(row=12, column=2, padx=10)

#cancel_button = Button(window, text = 'Cancel', command=window.destroy).grid(row=13, column=1)
ok_button = Button(window, text = 'OK').grid(row=13, column=2)

window.mainloop()
