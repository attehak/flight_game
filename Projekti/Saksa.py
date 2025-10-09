import time
import random
import sys


print(f"Valitse maa mihin haluaisit mennä (US, BR, DE, CH, AU):")
time.sleep(0.5)

def saksa(maa):
    elamat = 3
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
            sys.exit()
        elif fakta_vai_ei == "b":
            print("Tiesitkö että saksassa on 1500 eri leipälajia.")
            print(f"Lopulliset elämäsi olivat: {elamat} elämää.")
            print(f"Kiitos pelauksesta, {pelaaja_nimi}.")
            sys.exit()
        else:
            print("Yritä uudelleen")

        
        
        
        
        
        
        
        #Tämä kuuluu yhteiseen osaan
        if maa == "de" or "DE":
            saksa(maa)