import time
import math
import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="nimi",
    password="salasana",
    autocommit=True
)


def hae_satunnainen_iso_lentokentta(maa):
    sql = f"SELECT name, type, iso_country FROM airport WHERE iso_country = '{maa}' AND type = 'large_airport'"
    cursor = connection.cursor()
    cursor.execute(sql)
    lentokentat = cursor.fetchall()

    if lentokentat:
        satunnainen = random.choice(lentokentat)
        print(f"Satunnainen iso lentokenttä maasta {maa}: {satunnainen[0]} ({satunnainen[1]})")
    else:
        print(f"Ei löytynyt isoja lentokenttiä maasta {maa}.")

hae_satunnainen_iso_lentokentta(str(input("Anna maan koodi (esim. US): ")))

# hakee maa perusteella esim US iso_country taulua käyttämällä random lentokentän, jonka type on large airport.