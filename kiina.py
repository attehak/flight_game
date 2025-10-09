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
        print("Painoit nyt jotain väärää nappia, yritä uudestaan!\n")
