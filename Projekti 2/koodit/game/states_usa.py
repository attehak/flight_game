AUSTRALIA_ASCII = r"""
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

THE_END_ART = r"""
████████╗██╗  ██╗███████╗     ███████╗███╗   ██╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝     ██╔════╝████╗  ██║██╔══██╗
   ██║   ███████║█████╗       █████╗  ██╔██╗ ██║██║  ██║
   ██║   ██╔══██║██╔══╝       ██╔══╝  ██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗     ███████╗██║ ╚████║██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ 
Prototype by: Aleksi, Atte, Eetu, Juuso ja Nipa
"""


USA_QUESTIONS = [
    {
        "kysymys": "Officer asks: 'What is the purpose of your visit and do you have an ESTA?'",
        "vaihtoehdot": [
            ("a", "Tourism, and yes, I have a valid ESTA."),
            ("b", "I'm looking for a job here."),
            ("c", "What is ESTA? I just booked a flight.")
        ],
        "oikea": "a",
        "rangaistus": {"b": 2, "c": 1}
    },
    {
        "kysymys": "You are at a restaurant and receive the bill. What about the tip?",
        "vaihtoehdot": [
            ("a", "I don't tip, service is included in the price."),
            ("b", "I leave 15-20% tip, it's mandatory here."),
            ("c", "I leave couple of coins from my pocket.")
        ],
        "oikea": "b",
        "rangaistus": {"a": 1, "c": 1}
    },
    {
        "kysymys": "A police officer pulls you over while driving. What do you do?",
        "vaihtoehdot": [
            ("a", "Get out of the car immediately to greet him."),
            ("b", "Stay inside, keep hands on the wheel and wait."),
            ("c", "Start digging into the glove compartment for papers quickly.")
        ],
        "oikea": "b",
        "rangaistus": {"a": 2, "c": 2}
    },
    {
        "kysymys": "Someone asks 'How are you?' while walking past you.",
        "vaihtoehdot": [
            ("a", "Stop and tell them about your day in detail."),
            ("b", "Ignore them, they are strangers."),
            ("c", "Say 'Good, thanks' and keep walking. It's just a greeting.")
        ],
        "oikea": "c",
        "rangaistus": {"a": 0, "b": 1}
    },
    {
        "kysymys": "You see a price tag of $10. You have exactly $10 bill.",
        "vaihtoehdot": [
            ("a", "Great, I'll buy it."),
            ("b", "I need more money, tax is added at the register."),
            ("c", "I try to haggle the price down.")
        ],
        "oikea": "b",
        "rangaistus": {"a": 0, "c": 0}
    }
]


def usa_story(state, answer, carry=None):
    
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
                "ascii": AUSTRALIA_ASCII,
                "carry": "5"
            }
        return {
            "text": [],
            "choices": [],
            "next_state": 0,
            "redirect": "/game",
            "ascii": AUSTRALIA_ASCII,
            "carry": "5"
        }

    if state == 0:
        return {
            "text": [
                "Howdy partner",
                "Olet saapunut lentokentälle.",
                f"Sinulla on {elamat} elämää. Jokainen väärä vastaus vähentää 1 elämää.",
                "Tulli-virkailija alkaa kysyä sinulta kysymyksiä."
            ],
            "choices": ["Aloita kysymykset"],
            "next_state": 2,
            "ascii": AUSTRALIA_ASCII,
            "carry": str(elamat)
        }

    if state % 2 == 0 and 2 <= state <= 20:
        question_index = state // 2 - 1
        if question_index >= len(USA_QUESTIONS):
            
            return {
                "text": [
                    "Selvisit kaikista Yhdysvaltojen lentokenttä haasteista!",
                    f"Sinulla on {elamat} elämää jäljellä!",
                    "",
                    "Onneksi olkoon! 🎉"
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": THE_END_ART,
                "carry": str(elamat)
            }
        question = USA_QUESTIONS[question_index]
        return {
            "text": [
                f"Kysymys {question_index + 1}/5",
                f"Elämät jäljellä: {elamat} ❤️",
                question["kysymys"]
            ],
            "choices": [f"{opt[0]}) {opt[1]}" for opt in question["vaihtoehdot"]],
            "next_state": state + 1,
            "ascii": AUSTRALIA_ASCII,
            "carry": str(elamat)
        }

    if state % 2 == 1 and 3 <= state <= 21:
        vastaus_index = (state - 3) // 2
        if vastaus_index >= len(USA_QUESTIONS):
            
            return {
                "text": [
                    "✅ Kaikki kysymykset oikein!",
                    f"Elämät jäljellä: {elamat} ❤️",
                    "Selvisit kaikista Yhdysvaltojen lentokenttä haasteista!",
                    f"Saavuit perille {elamat} elämällä jäljellä!",
                    "",
                    "Onneksi olkoon! 🎉"
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": THE_END_ART,
                "carry": str(elamat)
            }

        question = USA_QUESTIONS[vastaus_index]

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
                    "Menetit kaikki elämäsi Yhdysvaltojen lentokentällä.",
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
                    "Selvisit kaikista Kiinan lentokentän haasteista!",
                    f"Saavuit perille {elamat} elämällä jäljellä!",
                    "",
                    "Onneksi olkoon! 🎉"
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": THE_END_ART,
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
            "ascii": AUSTRALIA_ASCII,
            "carry": str(elamat)
        }

    return {
        "text": ["Virhe: tuntematon tila."],
        "choices": ["Takaisin"],
        "next_state": 0,
        "ascii": AUSTRALIA_ASCII,
        "carry": "5"
    }

