import mysql.connector

#mysql connection with python
mydb = mysql.connector.connect(host="127.0.0.1", user="root",password="Dionusia1080")

mycursor = mydb.cursor()

mycursor.execute("Create database recycling")