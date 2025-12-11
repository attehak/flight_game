r"""
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

AUSTRALIA_QUESTIONS = [
    {
        "kysymys": "Do you have a valid visa for your stay in Australia?",
        "vaihtoehdot": [
            ("a", "Yes, I have an approved ETA visa for tourism."),
            ("b", "No, I thought I could enter without one."),
            ("c", "I'm not sure; can I apply at the airport?")
        ],
        "oikea": "a",
        "rangaistus": {"b": 1, "c": 1}
    },
    {
        "kysymys": "Have you completed the Incoming Passenger Card correctly?",
        "vaihtoehdot": [
            ("a", "Yes, but I guessed on some biosecurity questions."),
            ("b", "Yes, I filled in everything honestly, including health and biosecurity details."),
            ("c", "No, I skipped it; it's too long.")
        ],
        "oikea": "b",
        "rangaistus": {"a": 1, "c": 1}
    },
    {
        "kysymys": "Do you have any fruits, vegetables or plants in your luggage?",
        "vaihtoehdot": [
            ("a", "Yes, but only a banana; it's harmless."),
            ("b", "Maybe, I forgot to check my bag."),
            ("c", "No, I have nothing to declare; I followed the rules online before travel.")
        ],
        "oikea": "c",
        "rangaistus": {"a": 1, "b": 1}
    },
    {
        "kysymys": "Did you declare all food and animal products on your Incoming Passenger Card?",
        "vaihtoehdot": [
            ("a", "Yes, I declare everything to avoid fines; biosecurity protects Australia's unique wildlife."),
            ("b", "No, just a little cheese for snacks."),
            ("c", "Why bother? It's personal items.")
        ],
        "oikea": "a",
        "rangaistus": {"b": 1, "c": 1}
    },
    {
        "kysymys": "Are your bags ready for X-ray and sniffer dog inspection after baggage claim?",
        "vaihtoehdot": [
            ("a", "No, I have some wooden souvenirs that might be restricted."),
            ("b", "Yes, I packed according to rules: no fresh foods, seeds or wooden items without quarantine."),
            ("c", "I didn't think about it; dogs won't find anything small.")
        ],
        "oikea": "b",
        "rangaistus": {"a": 1, "c": 1}
    },
    {
        "kysymys": "Do you have Australian dollars or a card for any potential fees or transport?",
        "vaihtoehdot": [
            ("a", "Yes, but only cash; no card."),
            ("b", "No, I'll use only euros; it's fine."),
            ("c", "Yes, I exchanged some AUD and have a no-fee international card ready for ATMs or taxis.")
        ],
        "oikea": "c",
        "rangaistus": {"a": 1, "b": 1}
    },
    {
        "kysymys": "Someone bumps into you at the airport; will you say 'sorry' politely?",
        "vaihtoehdot": [
            ("a", "Yes, it's polite in Australia even if it's not my fault."),
            ("b", "No, only if I feel responsible."),
            ("c", "I ignore and keep walking; it's busy.")
        ],
        "oikea": "a",
        "rangaistus": {"b": 1, "c": 1}
    },
    {
        "kysymys": "Are you applying sunscreen before going outside the airport?",
        "vaihtoehdot": [
            ("a", "No, it's just a short walk to the taxi."),
            ("b", "Yes, I always use SPF 50+ in Australia due to the hole in the ozone layer and high UV."),
            ("c", "Only if it's very sunny; otherwise no need.")
        ],
        "oikea": "b",
        "rangaistus": {"a": 1, "c": 1}
    },
    {
        "kysymys": "How will you get from the airport to your accommodation?",
        "vaihtoehdot": [
            ("a", "I'll use official airport taxi, Skytrain or rideshare app."),
            ("b", "Any random taxi outside; it's cheaper."),
            ("c", "Walk; it's not far from the city.")
        ],
        "oikea": "a",
        "rangaistus": {"b": 1, "c": 1}
    },
    {
        "kysymys": "Do you know the fines for undeclared biosecurity items in Australia?",
        "vaihtoehdot": [
            ("a", "No, probably just a warning and confiscation."),
            ("b", "Yes, but only for large amounts; small snacks are ok."),
            ("c", "Yes, up to 4200 AUD per item or even jail; I double-checked all rules.")
        ],
        "oikea": "c",
        "rangaistus": {"a": 1, "b": 1}
    }
]

def australia_story(state, answer, carry=None):
    
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
                "Hello mate!",
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
        if question_index >= len(AUSTRALIA_QUESTIONS):
            
            return {
                "text": [
                    "Selvisit kaikista Australian lentokentän haasteista!",
                    f"Sinulla on {elamat} elämää jäljellä!",
                    "",
                    "Onneksi olkoon! 🎉"
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": AUSTRALIA_ASCII,
                "carry": str(elamat)
            }
        question = AUSTRALIA_QUESTIONS[question_index]
        return {
            "text": [
                f"Kysymys {question_index + 1}/10",
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
        if vastaus_index >= len(AUSTRALIA_QUESTIONS):
            
            return {
                "text": [
                    "✅ Kaikki kysymykset oikein!",
                    f"Elämät jäljellä: {elamat} ❤️",
                    "Selvisit kaikista Australian lentokentän haasteista!",
                    f"Saavuit perille {elamat} elämällä jäljellä!",
                    "",
                    "Onneksi olkoon! 🎉"
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": AUSTRALIA_ASCII,
                "carry": str(elamat)
            }

        question = AUSTRALIA_QUESTIONS[vastaus_index]

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
                    "Menetit kaikki elämäsi Australian lentokentällä.",
                    "Tulli-virkailija ei päästänyt sinua läpi!",
                    "Yritä uudelleen."
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": AUSTRALIA_ASCII,
                "carry": "5"
            }

        if vastaus_index == 9 or state >= 19:
            return {
                "text": [
                    palaute,
                    f"Elämät jäljellä: {elamat} ❤️",
                    "Selvisit kaikista Australian lentokentän haasteista!",
                    f"Saavuit perille {elamat} elämällä jäljellä!",
                    "",
                    "Onneksi olkoon! 🎉"
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": AUSTRALIA_ASCII,
                "carry": str(elamat)
            }

        return {
            "text": [
                palaute,
                f"Elämät jäljellä: {elamat} ❤️",
                f"Kysymys {vastaus_index + 1}/10 valmis. Jatka seuraavaan?"
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
