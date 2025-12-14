
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

THE_END_ART = r"""
████████╗██╗  ██╗███████╗     ███████╗███╗   ██╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝     ██╔════╝████╗  ██║██╔══██╗
   ██║   ███████║█████╗       █████╗  ██╔██╗ ██║██║  ██║
   ██║   ██╔══██║██╔══╝       ██╔══╝  ██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗     ███████╗██║ ╚████║██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ 
Prototype by: Aleksi, Atte, Eetu, Juuso ja Nipa
"""

SWEDEN_QUESTIONS = [
    {
        "kysymys": "Hejsan hur mår du?",
        "vaihtoehdot": [
            ("a", "Hä"),
            ("b", "Jag är bra, tack."),
            ("c", "Bastu bastu bastu!!!")
        ],
        "oikea": "b",
        "rangaistus": {"a": 1, "c": 3}
    },
    {
        "kysymys": "So who is better at ice hockey Finland or Sweden?",
        "vaihtoehdot": [
            ("a", "Winlandia"),
            ("b", "svenska"),
            ("c", "Dont care")
        ],
        "oikea": "a",
        "rangaistus": {"b": 2, "c": 1}
    },
    {
        "kysymys": "Do you like meatballs?",
        "vaihtoehdot": [
            ("a", "Ofc"),
            ("b", "mid"),
            ("c", "No")
        ],
        "oikea": "a",
        "rangaistus": {"b": 2, "c": 3}
    },
    {
        "kysymys": "Is minecraft best swedish creation?",
        "vaihtoehdot": [
            ("a", "Ofc not, you have nobel awards etc"),
            ("b", "Close, but no"),
            ("c", "Yes")
        ],
        "oikea": "c",
        "rangaistus": {"a": 1, "b": 1}
    },
    {
        "kysymys": "vill du ha fika",
        "vaihtoehdot": [
            ("a", "ja"),
            ("b", "No i dont fika"),
            ("c", "No thanks")
        ],
        "oikea": "a",
        "rangaistus": {"b": 2, "c": 1}
    }
]


def sweden_story(state, answer, carry=None):
    
    if not carry:
        elamat = 5
    else:
        elamat = int(carry)

    if state == 21:
        valinta = (answer or "").strip().lower()
        if "pelaa" in valinta or "uusi" in valinta:
            return {
                "text": [],
                "choices": [],
                "next_state": 0,
                "redirect": "/game",
                "ascii": SWEDEN,
                "carry": "5"
            }
        return {
            "text": [],
            "choices": [],
            "next_state": 0,
            "redirect": "/game",
            "ascii": SWEDEN,
            "carry": "5"
        }

    if state == 0:
        return {
            "text": [
                "Hello mate!",
                "Olet saapunut lentokentälle.",
                f"Sinulla on {elamat} elämää. Jokainen väärä vastaus vähentää 1 elämää.",
                "Tulli-virkailija alkaa kysyä sinulta kysymyksiä."
            ],
            "choices": ["Aloita kysymykset"],
            "next_state": 2,
            "ascii": SWEDEN,
            "carry": str(elamat)
        }

    if state % 2 == 0 and 2 <= state <= 20:
        question_index = state // 2 - 1
        if question_index >= len(SWEDEN_QUESTIONS):
            
            return {
                "text": [
                    "Selvisit kaikista Ruotsin lentokentän haasteista!",
                    f"Sinulla on {elamat} elämää jäljellä!",
                    "",
                    "Onneksi olkoon! 🎉"
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": THE_END_ART,
                "carry": str(elamat)
            }
        question = SWEDEN_QUESTIONS[question_index]
        return {
            "text": [
                f"Kysymys {question_index + 1}/5",
                f"Elämät jäljellä: {elamat} ❤️",
                question["kysymys"]
            ],
            "choices": [f"{opt[0]}) {opt[1]}" for opt in question["vaihtoehdot"]],
            "next_state": state + 1,
            "ascii": SWEDEN,
            "carry": str(elamat)
        }

    if state % 2 == 1 and 3 <= state <= 21:
        vastaus_index = (state - 3) // 2
        if vastaus_index >= len(SWEDEN_QUESTIONS):
            
            return {
                "text": [
                    "✅ Kaikki kysymykset oikein!",
                    f"Elämät jäljellä: {elamat} ❤️",
                    "Selvisit kaikista Ruotsin lentokentän haasteista!",
                    f"Saavuit perille {elamat} elämällä jäljellä!",
                    "",
                    "Onneksi olkoon! 🎉"
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": THE_END_ART,
                "carry": str(elamat)
            }

        question = SWEDEN_QUESTIONS[vastaus_index]

        selected = (answer or "").strip().lower()
        if selected and selected[0] in ["a", "b", "c"]:
            selected = selected[0]
        else:
            selected = None

        if selected == question["oikea"]:
            palaute = "✅ Oikein!"
        else:
            rangaistus = question["rangaistus"].get(selected, 0)
            elamat -= rangaistus
            palaute = f"❌ Väärin! Oikea vastaus: {question['oikea']} (-{rangaistus} elämää)"

        if elamat <= 0:
            return {
                "text": [
                    "💀 GAME OVER!",
                    "Menetit kaikki elämäsi Ruotsin lentokentällä.",
                    "Tulli-virkailija ei päästänyt sinua läpi!",
                    "Yritä uudelleen."
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": THE_END_ART,
                "carry": "5"
            }

        if vastaus_index == 9 or state >= 19:
            return {
                "text": [
                    palaute,
                    f"Elämät jäljellä: {elamat} ❤️",
                    "Selvisit kaikista Ruotsin lentokentän haasteista!",
                    f"Saavuit perille {elamat} elämällä jäljellä!",
                    "",
                    "Onneksi olkoon! 🎉"
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": SWEDEN,
                "carry": str(elamat)
            }

        return {
            "text": [
                palaute,
                f"Elämät jäljellä: {elamat} ❤️",
                f"Kysymys {vastaus_index + 1}/5 valmis. Jatka seuraavaan?"
            ],
            "choices": ["Seuraava"],
            "next_state": state + 1,
            "ascii": SWEDEN,
            "carry": str(elamat)
        }

    return {
        "text": ["Virhe: tuntematon tila."],
        "choices": ["Takaisin"],
        "next_state": 0,
        "ascii": SWEDEN,
        "carry": "5"
    }
