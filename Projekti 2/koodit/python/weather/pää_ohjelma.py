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
    user="atte", #oma
    password="atte",#oma
    autocommit=True
)

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
plane = "✈"
pelaaja_elamat = [1,2,3,4,5]

GERMANY = r"""
                       *                                     
                       * ****                                
                        *********    ***                     
                         ******************                  
                   ***********************                  
                    ************************                 
                    ***********************                  
                  **************************                 
                   **************************                
                ****************************                
                *****************************                
                ******************************               
                **************************                   
                 **********************                      
                *********************                        
                 ********************                        
                  *********************                      
                       ******************                    
                      *******************                   
                     *****************                      
                     ******************                      
                             ** *
"""

USA = r"""
                **********                                        *  
               ****************************                     **   
              ********************************* ** *           ***    
            *************************************  **      *****     
            ************************************* ****   *********    
            ************************************* ****  ********      
            ***************************************************       
             **************************************************       
             *************************************************        
              *************************************************       
              **********************************************         
                ********************************************          
                    ************************************            
                            ***************************             
                            *****************     * ***            
                                *******              ***           
                                ***                  **          
                                    *
"""

CHINA = r"""
                                                                *******        
                                                                **********   * 
                                *                              ***************** 
                            ****                               ************** 
                            ********                           ***************  
                        ***********                          *****************  
                        ***************                  ****************     
                 ***********************                ****************      
                *************************************************  **        
                ***********************************************  *          
                 ***********************************************  **         
                   ***********************************************           
                    *********************************************            
                    ***********************************************          
                     *********************************************** *                
                       *********************************************        
                        *******************************************        
                                ***     ***************************         
                                        **************************  **      
                                        **************************   *      
                                        ***********************             
                                        *****    ********                 
                                                        *                    
                                                    ***
"""

AUSTRALIA = r"""
                                            **             *               
                                        **********         **              
                                ***   ***********         ****             
                                *******************         ******           
                            ************************      ******           
                            ****************************   ********          
                            ***************************************          
                        ****************************************          
                    ************************************************       
                 *****************************************************      
                ********************************************************     
                **********************************************************     
                ********************************************************** 
                 *********************************************************** 
                    ********************************************************* 
                    ********************************************************* 
                    ***************          *****************************  
                    ***********               **************************   
                    ******                     **  *********************    
                                                    ******************      
                                                    ****************       
                                                    **************         
                                                        *** *******         
                                                                            
                                                                            
                                                        *****             
                                                            ****             
                                                            **
"""

SWEDEN = r"""                       
                                    *                        
                                   ****                      
                               **********                    
                             ************                   
                            *************                   
                            *************                   
                           ***************                   
                          ****************                   
                         *****************                  
                         **************                      
                        **************                       
                       **************                        
                        *************                        
                     ***************                         
                    **************                           
                    ************                             
                    ***********                              
                    **********                               
                    **********                               
                     *********                               
                     *********                               
                     ************                            
                    ************                            
                   ************                            
                  ************                               
                   *********                                
                    *********   **                            
                    ********    *                             
                      *******                                
                     ***                                  
                      **
"""

COUNTRIES = {
    "DE": GERMANY,
    "US": USA,
    "CN": CHINA,
    "AU": AUSTRALIA,
    "SE": SWEDEN,
}

world = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠SE⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀  ⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
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
print(f"Valitse viidestä maasta (Usa, Deutschland, Sweden, China tai Australia) mieluisa, jonne haluat mennä.") # lyhenteet poistettu

# Sallitut maat
sallitut_maat = ["US", "DE", "SE", "CN", "AU"]

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


def australia_kysymykset():
    global pelaaja_elamat 
    elamat = len(pelaaja_elamat)
    kysymykset = [
        {
            "kysymys": "Do you have a valid visa for your stay in Australia?",
            "vaihtoehdot": {
                "a": "Yes, I have an approved ETA visa for tourism.",
                "b": "No, I thought I could enter without one.",
                "c": "I'm not sure; can I apply at the airport?"
            },
            "oikea": "a",
            "rangaistus": {"b": 5, "c": 5}
        },
        {
            "kysymys": "Have you completed the Incoming Passenger Card correctly?",
            "vaihtoehdot": {
                "a": "Yes, but I guessed on some biosecurity questions.",
                "b": "Yes, I filled in everything honestly, including health and biosecurity details.",
                "c": "No, I skipped it; it's too long."
            },
            "oikea": "b",
            "rangaistus": {"a": 2, "c": 4}
        },
        {
            "kysymys": "Do you have any fruits, vegetables or plants in your luggage?",
            "vaihtoehdot": {
                "a": "Yes, but only a banana; it's harmless.",
                "b": "Maybe, I forgot to check my bag.",
                "c": "No, I have nothing to declare; I followed the rules online before travel."
            },
            "oikea": "c",
            "rangaistus": {"a": 2, "b": 3}
        },
        {
            "kysymys": "Did you declare all food and animal products on your Incoming Passenger Card?",
            "vaihtoehdot": {
                "a": "Yes, I declare everything to avoid fines; biosecurity protects Australia's unique wildlife.",
                "b": "No, just a little cheese for snacks.",
                "c": "Why bother? It's personal items."
            },
            "oikea": "a",
            "rangaistus": {"b": 2, "c": 3}
        },
        {
            "kysymys": "Are your bags ready for X-ray and sniffer dog inspection after baggage claim?",
            "vaihtoehdot": {
                "a": "No, I have some wooden souvenirs that might be restricted.",
                "b": "Yes, I packed according to rules: no fresh foods, seeds or wooden items without quarantine.",
                "c": "I didn't think about it; dogs won't find anything small."
            },
            "oikea": "b",
            "rangaistus": {"a": 3, "c": 2}
        },
        {
            "kysymys": "Do you have Australian dollars or a card for any potential fees or transport?",
            "vaihtoehdot": {
                "a": "Yes, but only cash; no card.",
                "b": "No, I'll use only euros; it's fine.",
                "c": "Yes, I exchanged some AUD and have a no-fee international card ready for ATMs or taxis."
            },
            "oikea": "c",
            "rangaistus": {"a": 1, "b": 2}
        },
        {
            "kysymys": "Someone bumps into you at the airport; will you say 'sorry' politely?",
            "vaihtoehdot": {
                "a": "Yes, it's polite in Australia even if it's not my fault.",
                "b": "No, only if I feel responsible.",
                "c": "I ignore and keep walking; it's busy."
            },
            "oikea": "a",
            "rangaistus": {"b": 2, "c": 3}
        },
        {
            "kysymys": "Are you applying sunscreen before going outside the airport?",
            "vaihtoehdot": {
                "a": "No, it's just a short walk to the taxi.",
                "b": "Yes, I always use SPF 50+ in Australia due to the hole in the ozone layer and high UV.",
                "c": "Only if it's very sunny; otherwise no need."
            },
            "oikea": "b",
            "rangaistus": {"a": 1, "c": 2}
        },
        {
            "kysymys": "How will you get from the airport to your accommodation?",
            "vaihtoehdot": {
                "a": "I'll use official airport taxi, Skytrain or rideshare app like.",
                "b": "Any random taxi outside; it's cheaper.",
                "c": "Walk; it's not far from the city."
            },
            "oikea": "a",
            "rangaistus": {"b": 2, "c": 3}
        },
        {
            "kysymys": "Do you know the fines for undeclared biosecurity items in Australia?",
            "vaihtoehdot": {
                "a": "No, probably just a warning and confiscation.",
                "b": "Yes, but only for large amounts; small snacks are ok.",
                "c": "Yes, up to 4200 AUD per item or even jail; I double-checked all rules."
            },
            "oikea": "c",
            "rangaistus": {"a": 2, "b": 3}
        }
    ]

    print("\nTervetuloa Australian lentokentälle! Sinulla on 5 elämää.")
    time.sleep(1)
    print("\nTulli-virkailija alkaa kysyä sinulta kysymyksiä englanniksi.")
    time.sleep(1)

    for indeksi, kysymys in enumerate(kysymykset, 1):
        print(f"\nKysymys {indeksi}: [{kysymys['kysymys']}]")
        time.sleep(0.5)
        for avain, vaihtoehto in kysymys["vaihtoehdot"].items():
            print(f"  {avain}) [{vaihtoehto}]")
            time.sleep(0.5)

        while True:
            vastaus = input("Vastauksesi (a/b/c): ").strip().lower()
            if vastaus in ["a", "b", "c"]:
                break
            else:
                print("Virheellinen vastaus! Yritä uudelleen (a/b/c). Ei rangaistusta.")
                time.sleep(0.5)
                for avain, vaihtoehto in kysymys["vaihtoehdot"].items():
                    print(f"  {avain}) [{vaihtoehto}]")
                time.sleep(0.5)

        if vastaus == kysymys["oikea"]:
            print("Oikein! Selvisit tästä haasteesta.")
            time.sleep(0.5)
        else:
            menetetty = kysymys["rangaistus"].get(vastaus, 0)
            elamat -= menetetty
            pelaaja_elamat = pelaaja_elamat[:elamat]  
            print(f"Väärin! Menetit {menetetty} elämää (valitsit {vastaus}). Jäljellä: {elamat}")
            time.sleep(0.5)
            if elamat <= 0:
                print("Menetit kaikki elämät. Peli päättyy Australian lentokentällä.")
                time.sleep(1)
                sys.exit()

    print("Onnittelut! Selvisit kaikista Australian lentokentän haasteista")
    time.sleep(1)
    return True

def kiina():
    takaisin = 0
    elämät = 5
    print(f"Saavut Kiinaan {lentokenttä_nimi} lentokentälle!")
    time.sleep(.5)
    print("你好欢迎来到中国!") # Welcome to China!
    time.sleep(1.2)
    print("您是来出差还是旅游?") # Are you here on business or pleasure?
    time.sleep(1.2)
    print("(A) öö...")
    time.sleep(1)
    print("(B) Sorry i don't speak chinese.")
    time.sleep(1)
    print("(C) 你好先生，我很高兴来这里.") # Hello sir i am here on pleasure
    time.sleep(1.5)

    while True:
        if takaisin == 1:
            vastaus = 'a'
            break
        if takaisin == 2:
            break
        if takaisin == 3:
            break
        else:
            vastaus = input("Miten vastaat? ")
            if takaisin == 2:
                break

            if vastaus.lower() == 'c': # Chinese arc
                print("这是生意，先生！") # Pleasure it is sir!
                time.sleep(1)
                print("我可以看一下你的护照吗?") # Could i have your passport?
                time.sleep(1)
                print("(A) Sorry that was all the chinese i knew..") # miinus elämä ja menee enkku arc
                time.sleep(1)
                print("(B) 先生，给您!") # Here you go sir!
                time.sleep(1)
                print("(C) 不，你不可以!") # No you may not! - häviää pelin
                time.sleep(1)
            
                while True:
                    if takaisin == 2:
                        break
                    vastaus = input("Miten vastaat? ")
                    if vastaus.lower() == 'a':
                        elämät = elämät -1
                        print(f"Kiusallista! Menetit yhden elämän, tämän seurauksena sinulla on {elämät} elämää.")
                        time.sleep(3)
                        takaisin = 1
                        break
                    elif vastaus.lower() == 'c':
                        print("Lentokentän vartiat tulevat ja vievät sinut putkaan")
                        time.sleep(3)
                        print("Hävisit pelin!") # häviää pelin
                        time.sleep(3)
                        sys.exit() # Peli sulkeutuu
                    elif vastaus.lower() == 'b':
                        print("好的，一切检查完毕。下一步!")
                        time.sleep(1.5)
                        print("Kävelet matkatavaroiden noutoon..")
                        time.sleep(1.5)
                        print("Kuulet naisen huutavan jotain..")
                        time.sleep(1.5)
                        print(f"这里有{pelaaja_nimi}吗?")
                        time.sleep(1.5)
                        print("(A) Kävelen naisen ohi") # miinus elämä
                        time.sleep(1)
                        print("(B) Menen puhumaan naiselle")
                        time.sleep(1.5)

                        while True:
                            vastaus = input("Mitä teet? ")
                            if vastaus.lower() == 'a':
                                print("Nainen kävelee pois.")
                                time.sleep(1)
                                print("Jäät odottamaan matkatavaroitasi")
                                time.sleep(2)
                                print("...")
                                time.sleep(0.8)
                                print("..")
                                time.sleep(0.8)
                                print(".")
                                time.sleep(0.8)
                                print("Matkatavarasi eivät saapuneet...")
                                time.sleep(1.5)
                                elämät = elämät -1
                                print(f"Kiusallista! Menetit yhden elämän, tämän seurauksena sinulla on {elämät} elämää.")
                                time.sleep(3)
                                print("Kävelet pois lentokentältä..") # loma alkaa
                                time.sleep(1.5)
                                takaisin = 2
                                break
                            if vastaus.lower() == 'b':
                                print(f"Sanot naiselle: 你好，我是{pelaaja_nimi}.")
                                time.sleep(1.5)
                                print(f"你好，{pelaaja_nimi}，你的行李在我这里.")
                                time.sleep(1.5)
                                print("Nainen antaa sinulle matkalaukkusi.")
                                time.sleep(1.5)
                                print("Kiität häntä ja poistut lentokentältä.") # loma alkaa
                                time.sleep(2)
                                takaisin = 2
                                break
                            print("Painoit nyt jotain väärää nappia, yritä uudestaan!\n")

            if vastaus.lower() in ['a', 'b']:
                if takaisin == 2:
                    break
                print("Sorry sir i speak english now, are you here on business or pleasure?") # engrish ver. So solly, I speak-a Engrish now. You here fo' business o' preasure, huh?
                time.sleep(2.5)
                print("(A) Pleasure, sir.") # jatkaa
                time.sleep(1)
                print("(B) Im not sure..") # miinus elämä
                time.sleep(1.5)
                while True:
                    vastaus = input("Miten vastaat? ")
                    if vastaus.lower() == 'a':
                        print("Have a good vacation sir!") # engrish ver. Hava good vacation, sah!
                        time.sleep(2)
                        takaisin = 3
                        break
                    if vastaus.lower() == 'b': # miinus elämä
                        elämät = elämät -1
                        print(f"Kiusallista! Menetit yhden elämän, tämän seurauksena sinulla on {elämät} elämää.")
                        time.sleep(2)
                        print("The way you dressed says pleasure so lets go with that okay?") # engrish ver. Da way you dress say happy time, so we go wit dat, huh?
                        time.sleep(2.5)
                        takaisin = 3
                        break
                    if takaisin == 3:
                        break
                    print("Painoit nyt jotain väärää nappia, yritä uudestaan!\n")
            if takaisin == 3:
                break
            print("Painoit nyt jotain väärää nappia, yritä uudestaan!\n")

    if takaisin == 3:
        print("Kävelet matkatavaroiden noutoon..")
        time.sleep(1.5)
        print("Kuulet naisen huutavan jotain..")
        time.sleep(1.5)
        print(f"Is there a {pelaaja_nimi} here?")
        time.sleep(1.5)
        print("(A) Kävelen naisen ohi") # miinus elämä
        time.sleep(1)
        print("(B) Menen puhumaan naiselle")
        time.sleep(1.5)
        while True:
            vastaus = input("Mitä teet? ")
            if vastaus.lower() == 'a':
                print("Nainen kävelee pois..")
                time.sleep(2)
                print("Jäät odottamaan matkatavaroitasi")
                time.sleep(2)
                print("...")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("Matkatavarasi eivät saapuneet...")
                time.sleep(3)
                elämät = elämät -1
                print(f"Kiusallista! Menetit yhden elämän, tämän seurauksena sinulla on {elämät} elämää.")
                time.sleep(3)
                print("Kävelet pois lentokentältä..") # loma alkaa
                time.sleep(2)
                break
            if vastaus.lower() == 'b':
                print(f"Sanot naiselle: 'Hello i am {pelaaja_nimi}'.")
                time.sleep(1.5)
                print("'I have your luggage' vastaa nainen")
                time.sleep(1.5)
                print("Nainen antaa sinulle matkalaukkusi")
                time.sleep(1.5)
                print("Kiität häntä ja poistut lentokentältä.") # loma alkaa
                time.sleep(2)
                break
            print("Painoit nyt jotain väärää nappia, yritä uudestaan!\n")

    print("Lomasi alkaa...")
    time.sleep(5)
    print("Onpas hauskaa...")
    time.sleep(5)
    print("Vuonna 1946 Kiina vaihtoi vasemmanpuolisesta liikenteestä oikeanpuoliseen yhdessä päivässä.")
    time.sleep(3)
    print("Se aiheutti valtavan kaaoksen mutta toimi.")
    time.sleep(5)
    print("Haluatko jatkaa lomaasi?")
    time.sleep(1)
    print("(A) Kyllä")
    time.sleep(0.5)
    print("(B) En")
    while True:
        vastaus = input("Mitä teet? ")
        if vastaus.lower() == 'b':
            time.sleep(1)
            print("Lähdet takas Suomeen.")
            time.sleep(3)
            print(f"Sinulle jäi {elämät} elämää.")
            time.sleep(3)
            end_screen()
            time.sleep(10)
            sys.exit()

        if vastaus.lower() == 'a':
            time.sleep(3)
            print("...")
            time.sleep(5)
            print("Eräässä kiinalaisessa kaupungissa järjestettiin 'luonnon äänien festivaali' jossa esiintyjinä oli 300 sammakkoa.")
            time.sleep(3)
            print("Liput myytiin loppuun.")
            time.sleep(5)

            print("Haluatko jatkaa lomaasi?")
            time.sleep(1)
            print("(A) Kyllä..")
            time.sleep(0.5)
            print("(B) En!")
            while True:
                vastaus = input("Mitä teet? ")
                if vastaus.lower() == 'b':
                    time.sleep(1)
                    print("Hyvä")
                    time.sleep(0.3)
                    print("Lähdet takas Suomeen.")
                    time.sleep(3)
                    print(f"Sinulle jäi {elämät} elämää.")
                    time.sleep(3)
                    end_screen()
                    time.sleep(10)
                    sys.exit()

                if vastaus.lower() == 'a':
                    time.sleep(5)
                    print("...")
                    time.sleep(5)
                    print("Eräässä kiinalaisessa kaupungissa koulutettiin apinoita vartijoiksi.")
                    time.sleep(3)
                    print("He poistivat lintujen pesiä lentokentän lähltä.")
                    time.sleep(3)
                    print("He onnistuivat siinä paremmin kuin ihmiset..")
                    time.sleep(5)
                    print("Poliisi tuli kertomaan sinulle että visasi on päättynyt..")
                    time.sleep(3)
                    print("Sinut lähetettiin takaisin Suomeen.") # miinus elämä
                    time.sleep(3)
                    elämät = elämät -1
                    print(f"Kiusallista! Menetit yhden elämän, tämän seurauksena sinulla on {elämät} elämää.")
                    time.sleep(3)
                    print(f"Sinulle jäi {elämät} elämää.")
                    time.sleep(3)
                    end_screen()
                    time.sleep(10)
                    sys.exit() 
                    
                print("Painoit nyt jotain väärää nappia, yritä uudestaan!\n")


def saksa(maa):
    elamat = 5
    # Sinulla on käytössä saksassa 3 elämää

    if maa == "DE":
        
        Turvatarkastus_vai_ei = random.randint(0, 1)
    # Arvotaan joudutko turvatarkastukseen vai et

        if Turvatarkastus_vai_ei == 0:
        # 0 = ei lisäkuulusteluja
            print("Tervetuloa saksaan! Nauti reissustasi")
            lomailu(pelaaja_nimi, elamat)
            return elamat
    time.sleep(1)
    print("Lentokentän tullimiehet pyytävät sinut lisäkuulusteluihin.")
    time.sleep(2)
    print("Millä kielellä haluat hoitaa kuulustelut:\n"
          "(A) Englanti (Virkailija ei osaa saksaa)")

    # kysytään kieliä kunnes saadaan hyväksytty vastaus
    while True:
        kielivalinta = input("Valitse kieli (A): ").strip().lower()
        if kielivalinta == "a":
            # Englanninkielinen
            time.sleep(0.7)
            print(f"Hello, {pelaaja_nimi}. What brings you to Deutschland?")
            time.sleep(0.7)
            print("(A) Vacation\n"
                  "(B) Visiting family/relatives\n"
                  "(C) I want to bomb this country")

            # kysymys 1: toistetaan kunnes saadaan hyväksytty vastaus
            while True:
                kysymys1_vastaus = input("Valitse (A, B tai C): ").strip().lower()
                if kysymys1_vastaus == "c":
                    time.sleep(1)
                    print("Valitettavasti tullimiehet eivät tykänneet uhkauksestasi.\n")
                    elamat = elamat - 1
                    time.sleep(1)
                    print(f"Menetit yhden elämistäsi, sinulla on jäljellä {elamat} elämää.")
                    # tässä voi päättää haluatko lopettaa pelin vai antaa jatkaa; käytetään sys.exit()
                    break
                elif kysymys1_vastaus in ("a", "b"):
                    print("Alright")
                    break
                else:
                    print("Teit jotain väärin, yritä uudelleen.")
            time.sleep(2)
            print("Do you have knives etc in your luggage?:\n"
                  "(A) No, i dont\n"
                  "(B) Yes, i do\n"
                  "(C) I'm not sure")

            while True:
                kysymys3_vastaus = input("Answer the question: (A, B, C): ").strip().lower()
                if kysymys3_vastaus == "b":
                    print("We found them, we will bring you to court.")
                    time.sleep(2)
                    print("Saksalaiset löysivät kolme eri veistä, sait 10-vuoden vankilatuomion.")
                    time.sleep(1)
                    print("Hävisit pelin.")
                    return 0
                elif kysymys3_vastaus == "c":
                    print("Alright, we're gonna search your bag")
                    time.sleep(1)
                    print("Searching")
                    time.sleep(2)
                    print(".")
                    time.sleep(2)
                    print(".")
                    time.sleep(2)
                    print(".")
                    time.sleep(1)
                    print("Bag searched succesfully.")
                    loytyko_teravia = random.randint(1, 3)
                    if loytyko_teravia == 3:
                        time.sleep(2)
                        print("We found knife from your luggage.")
                        elamat = elamat - 1
                        print(f"Menetit yhden elämän, sinulla on {elamat} elämää jäljellä.")
                        time.sleep(2)
                        print("We will have to seize your knife.")
                        time.sleep(2)
                        print("Security check is over.")
                        time.sleep(2)
                        if elamat == 0:
                            print("Hävisit pelin, menetit kaikki elämäsi.")
                            sys.exit()
                        else:
                            print("You're good to go, Have fun!")
                            lomailu(pelaaja_nimi, elamat)
                            return elamat
                    else:
                        print("We didnt find anything sharp, you're good to go, Have fun!")
                        lomailu(pelaaja_nimi, elamat)
                        return elamat
                elif kysymys3_vastaus == "a":
                    print("You're good to go, Have fun!")
                    lomailu(pelaaja_nimi, elamat)
                    return elamat
                else:
                    print("Teit jotain väärin, yritä uudelleen.")

        
        else:
            print("Nyt teit jotain väärin, yritä uudelleen.")
            # silmukka jatkuu ja kysyy kielivalinnan uudelleen
def lomailu(pelaaja_nimi, elamat):
    if elamat == 0:
        return
    else:
        time.sleep(2)
        print("Tervetuloa Saksaan! Lähde kävelylle (käsky)")
        time.sleep(2)
        print("Kävellään...")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print("Saksalainen mies kansallispuvussa lähestyy sinua ja tajuat että on Oktoberfest\n" \
        "Mitä aiot tehdä oktoberfestinä?:\n " \
        "(A) Juoda itsesi kaatokänniin\n" \
        "(B) Juon sivistyneesti\n" \
        "(C) Nukun lentokentällä\n")
    while True:
        kavely1 = str(input("Valitse vaihtoehto (A, B, C): "))

        if kavely1 == "a":
            print("Sinulla oli hauskaa muiden kanssa humalassa ja saksalaiset arvostivat sinua.")
            time.sleep(1.5)
            print("Ansaitsit yhden elämän lisää tästä!")
            elamat = elamat + 1
            print(f"Sinulla on nyt {elamat} elämää.")
        
        elif kavely1 in ("c", "b"):
            print("Saksalaiset pitivät sinua luuserina, koska et juonut perinteen mukaan kunnolla.")
            time.sleep(1.5)
            elamat = elamat - 1
            print(f"Sinulla on nyt {elamat} elämää.")
            if elamat == 0:
                print("Hävisit pelin.")
                sys.exit()
        else:
            print("Yritä uudelleen!")
        
        time.sleep(2)
        print("Haluatko mennä nukkumaan vai kuulla faktan saksasta?\n" \
        "(A) Nukkumaan"
        "(B) Haluan kuulla faktan")
        fakta_vai_ei = str(input("Valitse A vai B: "))
        
        if fakta_vai_ei == "a":
            print("Nukut nyt minuutin ajan, jonka jälkeen peli päättyy.")
            time.sleep(60)
            print(f"Lopulliset elämäsi olivat: {elamat} elämää.")
            print(f"Kiitos pelauksesta, {pelaaja_nimi}.")
            end_screen()
            time.sleep(5)
            sys.exit()
        elif fakta_vai_ei == "b":
            print("Tiesitkö että saksassa on 1500 eri leipälajia.")
            print(f"Lopulliset elämäsi olivat: {elamat} elämää.")
            print(f"Kiitos pelauksesta, {pelaaja_nimi}.")
            end_screen()
            time.sleep(5)
            sys.exit()
        else:
            print("Yritä uudelleen")

        
        
        
        
    

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

def lomailu_R():
  
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
    maa_input = input("\nKirjoita valitsemasi maa, kiitos! (sallitut: US, DE, SE, CN, AU): ").strip().upper()
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
elif lentokenttä_maa == "CN":
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
        print("Sallitut maat: US (USA), DE (Saksa), SE (Ruotsi), CN (Kiina), AU (Australia)")
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

def lennä(code):
    kartta = COUNTRIES[code]

    os.system('cls' if os.name == 'nt' else 'clear')  # Tyhjennä ruutu
    stop = 30 # kohta missä lentokone pysähtyy
    for x in range(stop + 1):
        clear()
        print(" " * x + plane)
        print(kartta)
        time.sleep(0.1)
    print(f"Tervetuloa {pelaaja_nimi}, {lentokenttä_maa}!")

lennä(lentokenttä_maa)

while True:
    #kelasin, että tähä tulis ne kyselyt

    if lentokenttä_maa == "SE":
        Ruotsi_kysely()
        lomailu_R()
        break
    elif lentokenttä_maa == "DE":
        saksa(maa=lentokenttä_maa)
    elif lentokenttä_maa == "AU":
        australia_kysymykset()
    elif lentokenttä_maa == "CN":
        kiina()
    elif lentokenttä_maa == "US":
        print("ICE lajiteteli sinut kiinann")
        time.sleep(5)
        kiina()
    else:
        lomailu()
        break

time.sleep(4)
end_screen()
