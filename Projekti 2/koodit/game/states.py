from airport_data import get_random_large_airport
from weather import get_weather
from flask import session

def intro(state, answer=None, carry=None):
    

    # 0 — Nimi kysely
    if state == 0:
        return {
            "text": ["Mikä on nimesi?"],
            "choices": None,
            "input_type": "text",
            "next_state": 1
        }

    # 1 — maan valinta
    if state == 1:
        pelaaja_nimi = answer.strip()
        option_texts = [
            ("US", "USA"),
            ("DE", "Germany"),
            ("SE", "Sweden"),
            ("CN", "China"),
            ("AU", "Australia")
        ]
        return {
            "text": [
                f"Terve {pelaaja_nimi}!",
                "Valitse maa:"
            ],
            "choices": ["US", "DE", "SE", "CN", "AU"],
            "option_texts": option_texts,
            "next_state": 2,
            "carry": pelaaja_nimi
    }

    # 2 — lentokentän arvonta
    if state == 2:
        maa = answer
        kentta = get_random_large_airport(maa)
        
        if kentta:
            # Puretaan kolme arvoa: nimi, koodi, kaupunki
            nimi, koodi, kaupunki = kentta
            # Tallennetaan kaupunki sessioon myöhempää sää-hakua varten
            session['city'] = kaupunki
        else:
            nimi, koodi, kaupunki = ("Tuntematon", "N/A", "Tuntematon")
            session['city'] = ""

        return {
            "text": [
                f"Lentokenttäsi valitusta maasta '{maa}' on: {nimi} ({koodi})",
                f"Sijainti: {kaupunki}",
                "Haluatko varmasti jatkaa vai vaihtaa maata?"
            ],
            "choices": ["Jatka", "Vaihda"],
            "next_state": 3,
            "carry": maa
        }
    if state == 3:
        if answer == "Vaihda":
            return {
                "text": ["Valitse uusi maa:"],
                "choices": ["US", "DE", "SE", "CN", "AU"],
                "next_state": 2
            }

        return {
            "text": ["Lento lähtee!"],
            "choices": ["Aloita lento"],
            "next_state": 4,
            "carry": carry
        }

    # 4 — tervetuloa
    if state == 4:
        maa = carry
        kaupunki = session.get('city', '')
        
        # Haetaan sää
        saa_teksti = get_weather(kaupunki)
        
        return {
            "text": [
                f"Saavuit maahan {maa} (Kaupunki: {kaupunki})!",
                saa_teksti
            ],
            "choices": ["Jatka seikkailua"],
            "next_state": 5,
            "carry": maa
        }
    
    

    # 5 — sisäinen maan valinta funktio
    if state == 5:
        maa = carry

        if maa == "SE": return {"redirect": "/story/sweden"}
        if maa == "DE": return {"redirect": "/story/germany"}
        if maa == "AU": return {"redirect": "/story/australia"}
        if maa == "CN": return {"redirect": "/story/china"}
        if maa == "US": return {"redirect": "/story/us"}

        return {
            "text": ["Tuntematon maa."],
            "choices": ["Aloita alusta"],
            "next_state": 0
        }
