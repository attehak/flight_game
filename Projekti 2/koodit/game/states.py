import random

def intro(state, answer=None):
    """
    Käsittelee
     - pelaajan nimen kysynnän
     - tervetulo viesti
     - maan valinta
     - lentokentän arvonta
     - varmistus haluuko lähtee
    """

    # 0 — nimi kysely
    if state == 0:
        text = ["Hei, mikä on nimesi matkustaja?"]
        return {
            "text": text,
            "choices": None,   # Käyttäjä kirjoittaa nimen formi kenttään
            "input_type": "text",
            "next_state": 1
        }

    # 1 — säilyttää nimen
    if state == 1:
        pelaaja_nimi = answer.strip()
        if not pelaaja_nimi:
            return {
                "text": ["Nimi ei voi olla tyhjä! Anna nimi uudelleen."],
                "choices": None,
                "input_type": "text",
                "next_state": 1
            }

        text = [
            f"Terve {pelaaja_nimi} ja tervetuloa seikkailemaan maailman ympäri!",
            "Valitse viidestä maasta (US, DE, SE, CN, AU) mieluisa paikka jonne haluat mennä."
        ]
        return {
            "text": text,
            "choices": ["US", "DE", "SE", "CN", "AU"],
            "next_state": 2,
            "store": {"nimi": pelaaja_nimi}
        }

    # 2 — arpoo lentokentän
    if state == 2:
        maa = answer
        from airport_data import get_random_large_airport
        
        kentta = get_random_large_airport(maa)
        if not kentta:
            return {
                "text": [f"Ei löytynyt isoja lentokenttiä maasta {maa}. Valitse toinen maa."],
                "choices": ["US", "DE", "SE", "CN", "AU"],
                "next_state": 2
            }

        nimi, koodi = kentta

        small_greeting = {
            "US": "TSA häämöttää",
            "AU": "Varo hämähäkkejä",
            "CN": "Ni hao!",
            "SE": "jättebra",
            "DE": "Guten Tag!"
        }.get(koodi, f"Maa: {koodi}")

        text = [
            f"Lentokenttäsi: {nimi} ({koodi})",
            small_greeting,
            "Sinulla on 5 elämää.",
            "",
            "Haluatko jatkaa valittuun maahan vai vaihtaa?"
        ]

        return {
            "text": text,
            "choices": ["Jatka", "Vaihda"],
            "store": {"maa": maa, "kentta_nimi": nimi, "kentta_koodi": koodi},
            "next_state": 3
        }

    # 3 — haluatko vaihtaa
    if state == 3:
        if answer == "Vaihda":
            return {
                "text": ["Valitse uusi maa:"],
                "choices": ["US", "DE", "SE", "CN", "AU"],
                "next_state": 2
            }

        else:  # lento lähtee
            text = ["Lentokoneesi lähtee pian, turvallista matkaa!"]
            return {
                "text": text,
                "choices": ["Aloita lento"],
                "next_state": 4
            }

    # 4 animaatiot ei toimi verkkoversios
    if state == 4:
        # tervetuloa
        maa = answer
        text = [
            f"Lento suoritettu!",
            f"Tervetuloa perille maahan {maa}."
        ]
        return {
            "text": text,
            "choices": ["Jatka tarinaan"],
            "next_state": 5
        }

    # 5 — sisäinen maan valinta eli mikä funktio ajetaan
    if state == 5:
        maa = answer
        if maa == "SE":
            return {"redirect": "/story/sweden"}
        if maa == "DE":
            return {"redirect": "/story/germany"}
        if maa == "AU":
            return {"redirect": "/story/australia"}
        if maa == "CN":
            return {"redirect": "/story/china"}
        if maa == "US":
            return {"redirect": "/story/us"}

        return {
            "text": ["Tuntematon maa?"],
            "choices": ["Aloita alusta"],
            "next_state": 0
        }
