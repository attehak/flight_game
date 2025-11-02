<<<<<<< HEAD
import mysql.connector
=======
import mariadb
>>>>>>> ae5bffb (Teen chatbotin ja lisään sen yhteydenottosivulle)
import random
import time, math, os


<<<<<<< HEAD
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="fligth_game",
    user="NIMI",
    password="salasana",
    autocommit=True
)

=======
connection = mariadb.connect(
    host="127.0.0.1",
    port=3307,
    database="flight_game",
    user="root",
    password="12345",
    autocommit=True
)



>>>>>>> ae5bffb (Teen chatbotin ja lisään sen yhteydenottosivulle)
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

def lomailu():
# voidaan kutusa myöhemssä vaiheessa, jos haluaa "lomailla".
    while True:
        aika_input = input("Kauan haluat lomailla (sekunteina)?: ")
        if aika_input.isdigit():
            aika = int(aika_input)
            break
        else:
            print("Anna numeroita, kiitos.")

        

    print(f"Lomailu alkaa... ({aika} sekuntia)")
    while 0 <= aika:
        print(".")
        aika = aika - 1
        time.sleep(1)

    print("Lomailu loppui!")



def Ruotsi_kysely ():
    print("Hejsan hur mår du?")
    elämät = 5

    while True:
        print("A: Hä?")
        print("B: Jag är bra, tack.")
        print("C: Bastu bastu bastu!!!")
        kysymys1 = input("Vastaa, joko A, B tai C: ")
        time.sleep(2)
        if kysymys1 == "A":
            print("Sorry, can I have some kinda offical finnish identification?: ")
            break
        elif kysymys1 == "B":
            print("Bra bra, har du en id?")
            print("Ööööö yeees here i has!")
            break
        elif kysymys1 == "C":
            elämät = elämät - 1
            print("Very funny, can I have your ID")
            time.sleep(1)
            print(f"(kiusallista! Menetit yhden elämän, tämän seurauksena sinulla on {elämät} elämää.)")

            break
        else:
            print("Vastaathan A, B tai C.")
            time.sleep(2)
            print("\n")
            continue
    time.sleep(2)
    print("\nLooks good, a quick test to see if u pass our req")
    print("So who is better at ice hockey Finland or Sweden?\n")

    while True:
        print("A: Finland ofc?")
        print("B: You're dumb to even make a question than obvious.")
        print("C: Jag är team svenska! ")
        kysymys1 = input("Vastaa, joko A, B tai C: ")
        time.sleep(2)
        if kysymys1 == "A":
            print("Fair I dont watch ice hockey anyways so you're good.")
            break
        elif kysymys1 == "B":
            print("Language young one, you failed this test by losing your cool!")
            elämät = elämät - 1
            print(f"(Ei voi olla! Menetit yhden elämän, tämän seurauksena sinulla on {elämät} elämää.)")
            break
        elif kysymys1 == "C":
            elämät = elämät + 1
            print("Bra, you passed this test with flying colors or smth like that")
            time.sleep(1)
            print(f"Joskus kannattaa olla humble tai Ruotsi fani, tämän seurauksena sinulla on {elämät} elämää.")

            break
        else:
            print("Vastaathan A, B tai C.")
            time.sleep(2)
            print("\n")
            continue

    time.sleep(2)
    print("\n TEEVETUULUA to sweden, but frfr final question")
    print("Are you enjoying this game thus far!?\n")


    while True:
        print("A: Its aight, it works for now and I feel like im one with the game")
        print("B: Yes I would pay money for this artpiece!")
        print("C: Nah fam, this piece of game is horrible and devs shouldn't continue this prototype.")
        kysymys1 = input("Vastaa, joko A, B tai C: ")
        time.sleep(2)
        if kysymys1 == "A":
            print("Thanks g, welcome to Sweden!")
            break
        elif kysymys1 == "B":
            print("Bless, heres a life for W glaze!")
            elämät = elämät + 1
            print(f"(+glaze, tämän seurauksena sinulla on {elämät} elämää.)")
            break
        elif kysymys1 == "C":
            elämät = elämät - 1
            print("Yo, these devs work hard for your enjoyment chill bro")
            time.sleep(1)
            print(f"- aura, jonka seurauksena elämäsi on {elämät}.")

            break
        else:
            print("Vastaathan A, B tai C.")
            time.sleep(2)
            print("\n")
            continue
            

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
    

