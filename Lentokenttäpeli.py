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


pelaaja_nimi = input("Hei, mikä on nimesi matkustaja?: ")
time.sleep(1)
print(f"Terve {pelaaja_nimi} ja tervetuloa seikkailemaan maailman ympäri")
time.sleep(1)
print(f"Ensimmäisenä valitse viidestä maasta (US, DE, BR, CH, AU) mieluisa, jonne haluat mennä")
time.sleep(0.5)


def hae_satunnainen_iso_lentokentta(maa):
    sql = f"SELECT name, iso_country FROM airport WHERE iso_country = '{maa}' AND type = 'large_airport'"
    cursor = connection.cursor()
    cursor.execute(sql)
    lentokentat = cursor.fetchall()

    if lentokentat:
        satunnainen = random.choice(lentokentat)
        print(f"Lentokenttäsi valitusta maasta '{maa}' on tänään: {satunnainen[0]} ({satunnainen[1]})")
    else:
        print(f"Kokeile kirjoittaa maa uudestaa, sillä maasta {maa} ei löytynyt isoa lentokenttää.")

hae_satunnainen_iso_lentokentta(str(input("Anna maa, kiitos (esim. US): ")))

# hakee maa perusteella esim US iso_country taulua käyttämällä random lentokentän, jonka type on large airport.