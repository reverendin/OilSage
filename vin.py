import requests, json
from tkinter import *
from tkinter import messagebox

def get_vin(vin_num):
  answer = False
  while answer == False:
    #vin = input("Please enter vin number: ")
    if len(vin_num) != 17:
      return "short"

    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/'+ vin_num +'?format=json'
    r = requests.get(url)

    test = r.json()
    if test['Results'][0]['Make'] == '':
      print('Vin does not exist. Please try again')
      return "wrong_vin"
    else:
      car = test['Results'][0]
      make = car['Make']
      model = car['Model']
      year = car['ModelYear']
      cylinders = car['EngineCylinders']
      displacement = round(float(test['Results'][0]['DisplacementL']), 1)
      return(make, model, year, cylinders, displacement)
      answer = True
