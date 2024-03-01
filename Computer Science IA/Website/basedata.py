import sqlalchemy
from sqlalchemy import create_engine, text
import os
import ast
import pymysql

db_key = ""    
engine = create_engine(
db_key,
connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

# # # create database (have to comment it because it would cause an error if run again as the database already exists)
# with engine.connect() as conn:
#   conn.execute(text("CREATE TABLE reservations (id INTEGER, Reservation VARCHAR(2000))"))

#used to show what is in the database for testing purposes
with engine.connect() as conn:
    result = conn.execute(text("select * from reservations"))
    print(result.all())

#Retrieves all the rows from the database, stores it in result. Than iterated through and appended into a list
def load_reservations():
    with engine.connect() as conn:
      result = conn.execute(text("select * from reservations"))
      reserves = []
      for row in result.all():
        reserves.append(row) 
      return reserves

#Writes to database 
def write_reservations(data):
  with engine.connect() as conn:
    #inserts everything into the database as one line
    conn.execute(text("INSERT INTO reservations (Reservation) VALUES (:Reservation) "), {"Reservation": "Date: " +data['date'] + " |Time: "+ data['time'] + " |Name: "+ data['name'] +" |Phone: "+ data['phone'] + " |Party Size: "+ data['party-size']} ) 
    conn.commit()

print(sqlalchemy.__version__)







