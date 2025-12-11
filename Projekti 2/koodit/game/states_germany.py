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


def germany_story(state, answer=None):
    #Intro
    if state == 0:
        text = [
            "GERMANY",
            "Willkommen in Deutschland!",
            "Joudutko lisäkuulusteluun lentokentällä?"
        ]
        return {
            "text": text,
            "choices": [
                "A: toivottavasti en...",
                "B: Antaa tulla!"
            ],
            "next_state": 1
        }
    #Arvotaan turvatarkastus
    elif state == 1:
        import random
        tarkastus = random.randint(0, 1)

        if tarkastus == 0:
            return {
                "text": [
                    "Et joutunut lisäkuulusteluun, tervetuloa Saksaan"
                ],
                "choices": ["Continue"],
                "next_state": 99 #Lomailun alkuun
            }
        return {
            "text": ["Jouduit lisäkuulusteluihin.",
                     "Millä kielellä haluat hoitaa kuulustelut?"
            ],
            "choices": ["A: Englanti (virkailija ei osaa saksan kieltä)"],
            "next_state": 2
        }
    #Kielivalinta
    elif state == 2:
        if answer == "A":
            return {
                "text": [
                    "Hello, there. What brings you to Germany?"],
                "choices": [
                    "A: Vacation",
                    "B: Visiting relatives",
                    "C: I want to bomb this country"
                ],
                "next_state": 3
            }

        return {
            "text": ["Valitse vaihtoehdoista."],
            "choices": ["Continue"],
            "next_state": 2
        }
    #Syy reissulle
    elif state == 3:
        if answer == "C":
            return {
                "text": [
                    "Virkailija ei pitänyt uhkauksestasi.",
                    "(-1 elämä)"
                ],
                "choices": ["Continue"],
                "next_state": 4
            }
        if answer in ("A", "B"):
            return {
                "text": ["Alright, next question."],
                "choices": ["Continue"],
                "next_state": 4
            }
        return {"text": ["Valitse A, B tai C"], "choices": ["Continue"], "next_state": 3}
    #Tarkastus terävistä esineistä
    elif state == 4:
        return {
            "text": ["Do you have knives or sharp items in your luggage?"],
            "choices": [
                "A: No, i dont.",
                "B: Yes, i do",
                "C: I'm not sure"
            ],
            "next_state": 5
        }
    #Tulokset veitsikyselystä
    elif state == 5:
        if answer == "B":
            return {
                "text": [
                    "We found them.",
                    "You are being taken to court.",
                    "(Hävisit pelin.)"
                ],
                "choices": [],
                "next_state": "end"
            }
        if answer == "C":
            import random
            loytyi = random.randint(1, 3)

            if loytyi == 3:
                return {
                    "text": [
                        "We found a knife in your luggage.",
                        "(-1 elämä)",
                        "You're free to go, but the knife is seized."
                    ],
                    "choices": ["Continue"],
                    "next_state": 99
                }
            else:
                return {
                    "text": [
                        "We didn't find anything sharp.",
                        "You're good to go!"
                    ],
                    "choices": ["Continue"],
                    "next_state": 99
                }
        if answer == "A":
            return {
                "text": [
                    "You're good to go!",
                    "Have fun in Germany!"
                ],
                "choices": ["Continue"],
                "next_state": 99
            }
        return {"text": ["Valitse A, B tai C"], "choices": ["Continue"], "next_state": 4}
    #Lomailun alku
    elif state == 99:
        return {
            "text": [
                "Tervetuloa Saksaan!",
                "On oktoberfest, mitä teet?"
            ],
            "choices": [
                "A: Juon itseni kaatokänniin",
                "B: Juon sivistyneesti",
                "C: Nukun lentokentällä"
            ],
            "next_state": 100
        }
    #Oktoberfest tulokset
    elif state == 100:
        if answer == "A":
            return {
                "text": [
                    "Saksalaiset tykkäsivät että kunnioitit heidän kulttuuria!",
                    "(+1 Elämä)"
                ],
                "choices": ["Continue"],
                "next_state": 101
            }
        if answer in ("B", "C"):
            return {
                "text": [
                    "Saksalaiset pitivät sinua tylsänä.",
                    "(-1 elämä)"
                ],
                "choices": ["Continue"],
                "next_state": 101
            }
        return {"text": ["Valitse A, B tai C"], "choices": ["Continue"], "next_state": 99}
    #Viimeinen valinta
    elif state == 101:
        return {
            "text": [
                "Haluatko mennä nukkumaan puiston penkille vai kuulla faktan saksasta?"
            ],
            "choices": [
                "A: Nukkumaan",
                "B: Haluan kuulla faktan"
            ],
            "next_state": 102
        }
    #Lopetus
    elif state == 102:
        if answer == "A":
            return {
                "text": [
                    "Nukuit unesi ja peli päättyy.",
                    "Kiitos pelaamisesta!"
                ],
                "choices": [],
                "next_state": "end"
            }
        if answer == "B":
            return {
                "text": [
                    "Saksassa on 1500 erilaista leipälajia.",
                    "Kiitos pelaamisesta!"
                ],
                "choices": [],
                "next_state": "end"
            }
        return {"text": ["Valitse A tai B."], "choices": ["Continue"], "next_state": 101}

    return {"text": ["Unexpected state."], "choices": [], "next_state": "end"}