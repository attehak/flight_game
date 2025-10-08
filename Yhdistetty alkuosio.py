import mysql.connector
import random
import time
import math
import os
import sys

# MySQL-yhteys (korvaa omilla tiedoil)
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="juuso", #oma
    password="root",#oma
    autocommit=True
)

plane = "✈"
pelaaja_elamat = [1,2,3,4,5]


world = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⣼GB⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿US⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿DE⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿CN⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿AU⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡇⠀⠀⢀⣼⠗⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
print(world)

# While-silmukka pelaajan nimen valintaan estää nyt tyhjän syötteen
pelaaja_nimi = ""
while not pelaaja_nimi.strip():
    pelaaja_nimi = input("Hei, mikä on nimesi matkustaja?: ").strip()
    if not pelaaja_nimi:
        print("Nimi ei voi olla tyhjä! Anna nimi uudelleen.")
time.sleep(0.3)
print(f"Terve {pelaaja_nimi} ja tervetuloa seikkailemaan maailman ympäri")
time.sleep(1)
print(f"Valitse viidestä maasta (Usa, Deutschland, Ruotsi, China tai Australia) mieluisa, jonne haluat mennä.") # lyhenteet poistettu

# Sallitut maat
sallitut_maat = ["US", "DE", "SE", "CH", "AU"]

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

def hae_satunnainen_iso_lentokentta(maa):
    sql = f"SELECT name, iso_country FROM airport WHERE iso_country = '{maa}' AND type = 'large_airport'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    lentokentat = cursor.fetchall()

    if lentokentat:
        satunnainen = random.choice(lentokentat)
        print(f"Lentokenttäsi valitusta maasta '{maa}' on tänään: {satunnainen[0]} ({satunnainen[1]})")
        return satunnainen 
    else:
        print(f"Maasta {maa} ei löytynyt iso lentokenttää tietokannasta.")
        return None

def lomailu():
  
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
# Voidaan kutsua milloin vain, vaikka kyselyn lopussa jos halutaan lomailla.
def end_screen ():

    the_end = r"""
████████╗██╗  ██╗███████╗     ███████╗███╗   ██╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝     ██╔════╝████╗  ██║██╔══██╗
   ██║   ███████║█████╗       █████╗  ██╔██╗ ██║██║  ██║
   ██║   ██╔══██║██╔══╝       ██╔══╝  ██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗     ███████╗██║ ╚████║██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ 
"""
    print(the_end)
    print("Prototype by: \n --> Aleksi, Atte, Eetu ja Juuso <--")
#Voidaan heittää loppuun taikka kyselyn if lauseeseen if elämät <0 = end_screen() ja sys exit

# While-silmukka maan valintaan nyt toimii oikein 
valittu_maa = None
valittu_lentokenttä = None
while valittu_maa is None or valittu_lentokenttä is None:
    maa_input = input("\nKirjoita valitsemasi maa, kiitos! (sallitut: US, DE, SE, CH, AU): ").strip().upper()
    if maa_input not in sallitut_maat:
        print(f"Virheellinen maa tai syöte! Sallitut vaihtoehdot ovat: {', '.join(sallitut_maat)}. Yritä uudelleen.")
        valittu_maa = None  
        continue
    valittu_maa = maa_input  
    valittu_lentokenttä = hae_satunnainen_iso_lentokentta(valittu_maa)
    if valittu_lentokenttä is None:
        print("Ei sopivaa lentokenttää maasta. Valitse toinen maa.")
        valittu_maa = None 

lentokenttä_nimi, lentokenttä_maa = valittu_lentokenttä  
if lentokenttä_maa == "US":
    print("TSA häämöttää") #valitkaa oma
elif lentokenttä_maa == "AU":
    print("Varo hämähäkkejä")
elif lentokenttä_maa == "CH":
    print("Ni hao!") #valitkaa oma
elif lentokenttä_maa == "SE":
    print("jättebra")  #valitkaa oma
elif lentokenttä_maa == "DE":
    print("Guten Tag!") #valitkaa oma 
else:
    print(f"Valitsit lentokentän maasta {lentokenttä_maa}.")

print(f"{pelaaja_nimi} sinulla on {len(pelaaja_elamat)} elämää, joten etene se mielessä.")
time.sleep(2)

# Visuaalinen muutos maanvaihtoon
print("\n-------------------")
print("Haluatko varmasti jatkaa valittuun maahan vai vaihtaa?")
print("1 - Jatka matkaa")
print("2 - Vaihda maata")
print("-------------------\n")

while True:
    pelaaja_maavaihto = input("Valintasi (1 tai 2): ").strip()
    
    if pelaaja_maavaihto == "2":
        uusi_valittu_maa = None
        uusi_valittu_lentokenttä = None
        
        print("\n-------------------")
        print("Uusi maa")
        print("Sallitut maat: US (USA), DE (Saksa), SE (Ruotsi), CH (Kiina), AU (Australia)")
        print("-------------------\n")
        
        while uusi_valittu_maa is None or uusi_valittu_lentokenttä is None:
            uusi_maa_input = input("Anna uusi maa (esim. US): ").strip().upper()
            
            if uusi_maa_input not in sallitut_maat:
                print(f"Virheellinen maa! Sallitut: {', '.join(sallitut_maat)}. Yritä uudelleen.\n")
                continue
            
            uusi_valittu_maa = uusi_maa_input
            uusi_valittu_lentokenttä = hae_satunnainen_iso_lentokentta(uusi_valittu_maa)
            
            if uusi_valittu_lentokenttä is None:
                print("Ei sopivaa lentokenttää maasta. Valitse toinen maa.\n")
                uusi_valittu_maa = None
        
        valittu_maa = uusi_valittu_maa
        valittu_lentokenttä = uusi_valittu_lentokenttä
        lentokenttä_nimi, lentokenttä_maa = valittu_lentokenttä
        
        print(f"\nUudeksi valittu maa: {lentokenttä_maa}")
        break
    
    elif pelaaja_maavaihto == "1":
        break
    
    else:
        print("\nVirheellinen syöte! Kirjoita '1' jatkaaksesi tai '2' vaihtaaksesi maata.\n")


# Seuraava on animaatio: time.sleep(3) – Jatkaa normaalisti tästä

# Animaatio
time.sleep(3)
print("Lentokoneesi lähtee pian, turvallista matkaa!")
time.sleep(2)

for i in range(30):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("> " * i + plane)
    time.sleep(0.3)

print(f"Saavuit {pelaaja_nimi}, {lentokenttä_nimi}!")

while True:
    #kelasin, että tähä tulis ne kyselyt

    if lentokenttä_maa == "SE":
        Ruotsi_kysely()
    else:
        lomailu()

time.sleep(4)
end_screen()