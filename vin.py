import requests, json

answer = False
while answer == False:
  vin = input("Please enter vin number: ")
  if len(vin) != 17:
    print("Vin must contain 17 characters!")
    continue

  url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/'+ vin +'?format=json'
  r = requests.get(url)

  test = r.json()
  if test['Results'][0]['Make'] == '':
    print('Vin does not exist. Please try again')
  else:
    answer = True

car = test['Results'][0]
make = car['Make']
model = car['Model']
year = car['ModelYear']
cylinders = car['EngineCylinders']
displacement = round(float(test['Results'][0]['DisplacementL']), 1)

print(year, make.lower().capitalize(), model, cylinders, displacement)

