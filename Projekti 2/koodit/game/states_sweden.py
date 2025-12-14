
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


def sweden_story(state, answer=None):
    # State 0 — alku
    if state == 0:
        option_texts = [
            ("A", "Hä?"),
            ("B", "Jag är bra, tack."),
            ("C", "Bastu bastu bastu!!!")
        ]
        return {
            "text": ["Hejsan hur mår du?"],
            "choices": ["A", "B", "C"],
            "option_texts": option_texts,
            "next_state": 1
        }


    # State 1 — eka kysely
    if state == 1:
        if answer == "A":
            text = ["Sorry, can I have some kinda official Finnish identification?"]
            option_texts = [("C", "Continue")]
            return {"text": text, "choices": ["C"], "option_texts": option_texts, "next_state": 2}

        elif answer == "B":
            text = [
                "Bra bra, har du en id?",
                "Ööööö yeees here i has!"
            ]
            option_texts = [("C", "Continue")]
            return {"text": text, "choices": ["C"], "option_texts": option_texts, "next_state": 2}

        elif answer == "C":
            text = [
                "Very funny, can I have your ID",
                "(Kiusallista! Menetit yhden elämän.)"
            ]
            option_texts = [("C", "Continue")]
            return {"text": text, "choices": ["C"], "option_texts": option_texts, "next_state": 2}

        text = ["Valitse A, B tai C."]
        option_texts = [("C", "Continue")]
        return {"text": text, "choices": ["C"], "option_texts": option_texts, "next_state": 0}


    # State 2 — toka kysely
    if state == 2:
        text = [
            "Looks good, a quick test to see if u pass our req",
            "So who is better at ice hockey — Finland or Sweden?"
        ]
        option_texts = [
            ("A", "Finland ofc?"),
            ("B", "You're dumb to even make the question."),
            ("C", "Jag är team svenska!")
        ]
        return {"text": text, "choices": ["A", "B", "C"], "option_texts": option_texts, "next_state": 3}


    # State 3 — vastaukset lätkää
    if state == 3:
        if answer == "A":
            text = ["Fair, I don't watch ice hockey anyways — you're good."]
            option_texts = [("C", "Continue")]
            return {"text": text, "choices": ["C"], "option_texts": option_texts, "next_state": 4}

        if answer == "B":
            text = [
                "Language young one! You failed this test by losing your cool!",
                "(Menetit yhden elämän.)"
            ]
            option_texts = [("C", "Continue")]
            return {"text": text, "choices": ["C"], "option_texts": option_texts, "next_state": 4}

        if answer == "C":
            text = [
                "Bra! You passed this test with flying colors!",
                "(Sait yhden elämän lisää.)"
            ]
            option_texts = [("C", "Continue")]
            return {"text": text, "choices": ["C"], "option_texts": option_texts, "next_state": 4}

        text = ["Valitse A, B tai C."]
        option_texts = [("C", "Continue")]
        return {"text": text, "choices": ["C"], "option_texts": option_texts, "next_state": 2}


    # State 4 — vika kysely
    if state == 4:
        text = [
            "TEEVETUULUA to Sweden, but frfr final question:",
            "Are you enjoying this game thus far?"
        ]
        option_texts = [
            ("A", "It's aight, I feel one with the game."),
            ("B", "Yes, I'd pay money for this artpiece!"),
            ("C", "Nah fam, this game is horrible.")
        ]
        return {"text": text, "choices": ["A", "B", "C"], "option_texts": option_texts, "next_state": 5}


    # State 5 — vika
    if state == 5:
        if answer == "A":
            return {"text": ["Thanks g, welcome to Sweden!"], "choices": [], "option_texts": [], "next_state": "end"}

        if answer == "B":
            text = [
                "Bless — here's a life for W glaze!",
                "(+1 elämä.)"
            ]
            return {"text": text, "choices": [], "option_texts": [], "next_state": "end"}

        if answer == "C":
            text = [
                "Yo, these devs work hard — chill!",
                "(-1 elämä.)"
            ]
            return {"text": text, "choices": [], "option_texts": [], "next_state": "end"}


    # error
    return {"text": ["Unexpected state."], "choices": [], "option_texts": [], "next_state": "end"}

