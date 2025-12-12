AUSTRALIA_ASCII = r"""
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

THE_END_ART = r"""
████████╗██╗  ██╗███████╗     ███████╗███╗   ██╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝     ██╔════╝████╗  ██║██╔══██╗
   ██║   ███████║█████╗       █████╗  ██╔██╗ ██║██║  ██║
   ██║   ██╔══██║██╔══╝       ██╔══╝  ██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗     ███████╗██║ ╚████║██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ 
Prototype by: Aleksi, Atte, Eetu, Juuso ja Nipa
"""



CHINA_QUESTIONS = [
    {
        "kysymys": "You want to check your Gmail or Facebook.",
        "vaihtoehdot": [
            ("a", "I just open the app, no problem."),
            ("b", "I need a VPN because they are blocked."),
            ("c", "I ask a police officer for wifi password.")
        ],
        "oikea": "b",
        "rangaistus": {"a": 0, "c": 1}
    },
    {
        "kysymys": "You are eating with chopsticks. Where do you put them when resting?",
        "vaihtoehdot": [
            ("a", "Stick them vertically into the rice bowl."),
            ("b", "Place them on the table or chopstick rest."),
            ("c", "Point them at the other guests.")
        ],
        "oikea": "b",
        "rangaistus": {"a": 1, "c": 1}
    },
    {
        "kysymys": "Someone hands you a business card or gift.",
        "vaihtoehdot": [
            ("a", "Take it with one hand and put it in your pocket."),
            ("b", "Take it with both hands and look at it respectfully."),
            ("c", "Refuse it politely.")
        ],
        "oikea": "b",
        "rangaistus": {"a": 1, "c": 1}
    },
    {
        "kysymys": "Do you need a visa to enter China as a tourist?",
        "vaihtoehdot": [
            ("a", "No, I can just walk in."),
            ("b", "Yes, usually need to apply in advance."),
            ("c", "I can pay the guard to let me in.")
        ],
        "oikea": "b",
        "rangaistus": {"a": 1, "c": 2}
    },
    {
        "kysymys": "You are offered tea. What do you do?",
        "vaihtoehdot": [
            ("a", "Drink it immediately."),
            ("b", "Tap the table with two fingers to say thanks."),
            ("c", "Pour it on the floor for good luck.")
        ],
        "oikea": "b",
        "rangaistus": {"a": 0, "c": 1}
    }
]

def china_story(state, answer, carry=None):
    
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
                "Nihao",
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
        if question_index >= len(CHINA_QUESTIONS):
            
            return {
                "text": [
                    "Selvisit kaikista Kiinan lentokentän haasteista!",
                    f"Sinulla on {elamat} elämää jäljellä!",
                    "",
                    "Onneksi olkoon! 🎉"
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": THE_END_ART,
                "carry": str(elamat)
            }
        question = CHINA_QUESTIONS[question_index]
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
        if vastaus_index >= len(CHINA_QUESTIONS):
            
            return {
                "text": [
                    "✅ Kaikki kysymykset oikein!",
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

        question = CHINA_QUESTIONS[vastaus_index]

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
                    "Menetit kaikki elämäsi Kiinan lentokentällä.",
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

