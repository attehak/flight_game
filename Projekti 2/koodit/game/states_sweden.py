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

def sweden_story(state, answer=None):
    # State 0 — intro + ASCII art
    if state == 0:
        text = [
            SWEDEN,
            "Hejsan hur mår du?"
        ]
        return {
            "text": text,
            "choices": ["A: Hä?", "B: Jag är bra, tack.", "C: Bastu bastu bastu!!!"],
            "next_state": 1
        }

    # State 1 — eka kysely
    if state == 1:
        if answer == "A":
            text = ["Sorry, can I have some kinda official Finnish identification?"]
            return {"text": text, "choices": ["Continue"], "next_state": 2}

        elif answer == "B":
            text = [
                "Bra bra, har du en id?",
                "Ööööö yeees here i has!"
            ]
            return {"text": text, "choices": ["Continue"], "next_state": 2}

        elif answer == "C":
            text = [
                "Very funny, can I have your ID",
                "(Kiusallista! Menetit yhden elämän.)"
            ]
            return {"text": text, "choices": ["Continue"], "next_state": 2}

        return {"text": ["Valitse A, B tai C."], "choices": ["Continue"], "next_state": 0}

    # State 2 — toka kysely
    if state == 2:
        text = [
            "Looks good, a quick test to see if u pass our req",
            "So who is better at ice hockey — Finland or Sweden?"
        ]
        return {
            "text": text,
            "choices": [
                "A: Finland ofc?",
                "B: You're dumb to even make the question.",
                "C: Jag är team svenska!"
            ],
            "next_state": 3
        }

    # State 3 — vastaukset lätkää
    if state == 3:
        if answer == "A":
            return {
                "text": ["Fair, I don't watch ice hockey anyways — you're good."],
                "choices": ["Continue"],
                "next_state": 4,
            }

        if answer == "B":
            return {
                "text": [
                    "Language young one! You failed this test by losing your cool!",
                    "(Menetit yhden elämän.)"
                ],
                "choices": ["Continue"],
                "next_state": 4
            }

        if answer == "C":
            return {
                "text": [
                    "Bra! You passed this test with flying colors!",
                    "(Sait yhden elämän lisää.)"
                ],
                "choices": ["Continue"],
                "next_state": 4
            }

        return {"text": ["Valitse A, B tai C."], "choices": ["Continue"], "next_state": 2}

    # State 4 — vika kysely
    if state == 4:
        text = [
            "TEEVETUULUA to Sweden, but frfr final question:",
            "Are you enjoying this game thus far?"
        ]
        return {
            "text": text,
            "choices": [
                "A: It's aight, I feel one with the game.",
                "B: Yes, I'd pay money for this artpiece!",
                "C: Nah fam, this game is horrible."
            ],
            "next_state": 5
        }

    # State 5 — vika
    if state == 5:
        if answer == "A":
            return {"text": ["Thanks g, welcome to Sweden!"], "choices": [], "next_state": "end"}

        if answer == "B":
            return {
                "text": [
                    "Bless — here's a life for W glaze!",
                    "(+1 elämä.)"
                ],
                "choices": [],
                "next_state": "end"
            }

        if answer == "C":
            return {
                "text": [
                    "Yo, these devs work hard — chill!",
                    "(-1 elämä.)"
                ],
                "choices": [],
                "next_state": "end"
            }

    # error
    return {"text": ["Unexpected state."], "choices": [], "next_state": "end"}
