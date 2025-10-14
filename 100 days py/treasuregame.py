print(r'''
*      _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1= input('You\'re at a crossroad , '
               'where do you want to go? '
               'Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2= input('You\'ve come to a lake. '
                   'There is a island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is house with 3 door. "
                        "One red one yellow and one blue."
                        "Which color do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire.Game over")
        elif choice3 == "yellow":
            print("You found the treasure.You win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over")
        else:
            print("You choose a door doesn't exist. Game over")
    else:
        print("You got attacked by an angry trout. "
              "Game Over")
else:
    print("You fell in to a hole. Game Over")