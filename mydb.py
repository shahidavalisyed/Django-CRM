import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root123'
    
)

# preapring the cursor object
cursorObject=dataBase.cursor()

#Create DataBase

cursorObject.execute("CREATE DATABASE DCRM")

print("ALl done re")