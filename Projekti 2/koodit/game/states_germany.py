GERMANY_ASCII = r"""
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
THE_END_ART = r"""
████████╗██╗  ██╗███████╗     ███████╗███╗   ██╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝     ██╔════╝████╗  ██║██╔══██╗
   ██║   ███████║█████╗       █████╗  ██╔██╗ ██║██║  ██║
   ██║   ██╔══██║██╔══╝       ██╔══╝  ██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗     ███████╗██║ ╚████║██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ 
Prototype by: Aleksi, Atte, Eetu, Juuso ja Nipa
"""

GERMANY_QUESTIONS = [
    {
        "kysymys": "What brings you to Germany?",
        "vaihtoehdot": [
            ("a", "Vacation"),
            ("b", "Visiting relatives"),
            ("c", "I want to bomb this country")
        ],
        "oikea": "a",
        "rangaistus": {"b": 0, "c": 1}
    },
    {
        "kysymys": "Do you have knives or sharp items in your luggage?",
        "vaihtoehdot": [
            ("a", "No, I don't."),
            ("b", "Yes, I do."),
            ("c", "I'm not sure.")
        ],
        "oikea": "a",
        "rangaistus": {"b": 2, "c": 1}
    },
    {
        "kysymys": "It's Oktoberfest. What do you do?",
        "vaihtoehdot": [
            ("a", "Drink until blackout drunk."),
            ("b", "Drink moderately."),
            ("c", "Sleep at the airport.")
        ],
        "oikea": "a",
        "rangaistus": {"b": 1, "c": 1}
    },
    {
        "kysymys": "Do you want to hear a fact about Germany?",
        "vaihtoehdot": [
            ("a", "No, I just sleep."),
            ("b", "Yes, tell me a fact.")
        ],
        "oikea": "b",
        "rangaistus": {"a": 0}
    }
]

def germany_story(state, answer=None, carry=None):

    # Elämät samalla tavalla kuin Australiassa
    elamat = int(carry) if carry else 5

    # Restart
    if state == 21:
        return {
            "text": [],
            "choices": [],
            "next_state": 0,
            "redirect": "/game",
            "ascii": GERMANY_ASCII,
            "carry": "5"
        }

    # Intro
    if state == 0:
        return {
            "text": [
                "GERMANY 🇩🇪",
                "Willkommen in Deutschland!",
                f"Sinulla on {elamat} elämää ❤️",
                "Tullivirkailija alkaa kysyä kysymyksiä."
            ],
            "choices": ["Aloita"],
            "next_state": 2,
            "ascii": GERMANY_ASCII,
            "carry": str(elamat)
        }

    # Kysymykset (parilliset statet)
    if state % 2 == 0 and 2 <= state <= 8:
        index = state // 2 - 1
        question = GERMANY_QUESTIONS[index]

        return {
            "text": [
                f"Kysymys {index + 1}/{len(GERMANY_QUESTIONS)}",
                f"Elämät jäljellä: {elamat} ❤️",
                question["kysymys"]
            ],
            "choices": [f"{o[0]}) {o[1]}" for o in question["vaihtoehdot"]],
            "next_state": state + 1,
            "ascii": GERMANY_ASCII,
            "carry": str(elamat)
        }

    # Vastaukset (parittomat statet)
    if state % 2 == 1:
        index = (state - 3) // 2
        question = GERMANY_QUESTIONS[index]

        selected = (answer or "").strip().lower()
        selected = selected[0] if selected else None

        if selected == question["oikea"]:
            palaute = "✅ Oikein!"
        else:
            penalty = question["rangaistus"].get(selected, 1)
            elamat -= penalty
            palaute = f"❌ Väärin! (-{penalty} elämää)"

        # Game over
        if elamat <= 0:
            return {
                "text": [
                    "💀 GAME OVER!",
                    "Saksan tulliviranomaiset eivät päästäneet sinua maahan."
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": THE_END_ART,
                "carry": "5"
            }

        # Viimeinen kysymys
        if index == len(GERMANY_QUESTIONS) - 1:
            return {
                "text": [
                    palaute,
                    f"Elämät jäljellä: {elamat} ❤️",
                    "Selvisit Saksan seikkailusta!",
                    "Fun fact: Saksassa on yli 1500 leipälajia 🥨"
                ],
                "choices": ["Pelaa uudestaan"],
                "next_state": 21,
                "ascii": THE_END_ART,
                "carry": str(elamat)
            }

        # Jatko
        return {
            "text": [
                palaute,
                f"Elämät jäljellä: {elamat} ❤️",
                "Jatketaanko seuraavaan kysymykseen?"
            ],
            "choices": ["Seuraava"],
            "next_state": state + 1,
            "ascii": GERMANY_ASCII,
            "carry": str(elamat)
        }

    # Fallback
    return {
        "text": ["Virhe: tuntematon tila."],
        "choices": ["Takaisin"],
        "next_state": 0,
        "ascii": GERMANY_ASCII,
        "carry": "5"
    }
