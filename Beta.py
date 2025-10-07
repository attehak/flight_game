import mysql.connector
import random
import time, math, os


connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="fligth_game",
    user="NIMI",
    password="salasana",
    autocommit=True
)

#
#
#
plane = "✈"
pelaaja_elämät = [1,2,3,4,5]


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
        return satunnainen 
    else:
        print(f"Kokeile kirjoittaa maa uudestaa, sillä maasta {maa} ei löytynyt tarpeeksi isoa lentokenttää.")
        return None


valittu_lentokenttä = hae_satunnainen_iso_lentokentta(str(input("Anna maa, kiitos (esim. US): ")))
time.sleep(1)


if valittu_lentokenttä:
    lentokenttä_nimi, lentokenttä_maa = valittu_lentokenttä
    if lentokenttä_maa == "US":
        print("TSA häämöttää")
    elif lentokenttä_maa == "AU":
        print("Varo hämähäkkejä")
    elif lentokenttä_maa == "CH":
        print("Bing chilling")
    elif lentokenttä_maa == "BR":
        print("BRRRRR")
    else:
        print(f"Valitsit lentokentän maasta {lentokenttä_maa}.")

#Tähän voi lisätä kommentteja valitusta maasta esim US voi heittää tsa varotusta

print(f"{pelaaja_nimi} sinulla on {len(pelaaja_elämät)} elämää, joten etene se mielessä.")
time.sleep(2)
print("Haluatko aloittaa matkasi maahan vai vaihdetaanko maata?")


while True:
    pelaaja_vaihto = input("Haluatko jatkaa vai vaihtaa maata 1 tai 2 ('jatka') ja ('vaihda'):")

    if pelaaja_vaihto == "2":
        uusi_maa = input("Kirjoita uusi maa: ")
        uusi_lentokenttä = hae_satunnainen_iso_lentokentta(uusi_maa)

        if uusi_lentokenttä:
            valittu_lentokenttä = uusi_lentokenttä
            lentokenttä_nimi, lentokenttä_maa = valittu_lentokenttä
#            print(f"Uudeksi lentokentäksi valikoitu: {lentokenttä_nimi}, {lentokenttä_maa} ")
            break
        
    elif pelaaja_vaihto == "1":
        break
    else:
        print("Kirjoitithan joko, '1' (jatka) tai '2' (vaihda)")


# ei pakollinen, mutta jos halutaan lisätä myöhemmin tai alussa maan vaihto eli uusi random lentokenttä

# Animaatio: lentokone liikkuu oikealle
time.sleep(3)
print("Lentokone lähtee pian, turvallista matkaa!")
time.sleep(2)

for i in range(30):
    os.system('cls' if os.name == 'nt' else 'clear')  # Tyhjennä ruutu
    print("> " * i + plane)
    time.sleep(0.3)

print(f"Tervetuloa {pelaaja_nimi}, {lentokenttä_maa}!")
    

