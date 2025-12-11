import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="atte", #oma
    password="atte", #oma
    autocommit=True
)