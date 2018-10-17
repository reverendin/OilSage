import mysql.connector
import db_config as cfg

mydb = mysql.connector.connect(
  host=cfg.mysql['host'],
  user=cfg.mysql['user'],
  passwd=cfg.mysql['passwd'],
  database=cfg.mysql['database'],
)

cur =mydb.cursor()

#cur.execute("CREATE TABLE vehicles (year VARCHAR(4), make VARCHAR(50), model VARCHAR(100), cylinders VARCHAR(10), engSize VARCHAR(10), weight VARCHAR(10), oilType VARCHAR(50), quantity VARCHAR(10), torque VARCHAR(10), ofilter VARCHAR(50), afilter VARCHAR(50), cafilter VARCHAR(50))")
#cur.execute("ALTER TABLE vehicles ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

sql = "select * FROM vehicles WHERE year ='2009' AND make = 'Honda' AND model = 'Odyssey' AND cylinders = '6' AND engSize = '3.5'"
cur.execute(sql)
results = cur.fetchall()


def search_vehicle(year, make, model, cylinders, engSize):
  sql = f"select * FROM vehicles WHERE year ='{year}' AND make = '{make}' AND model = '{model}' AND cylinders = '{cylinders}' AND engSize = '{engSize}'"
  cur.execute(sql)
  results = cur.fetchall()
  return results[0]
