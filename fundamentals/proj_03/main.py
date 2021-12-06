#!/usr/bin/python3
"""
    Author     : Patrick Mwila
    Instructor : Dr. Angela Yu
    Description: This program simulates a simple adventure game.
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/patrick.
*******************************************************************************
''')

# display a message
print("Welcome to Treaure Island." + 
      "\nYour mission is to find the treasure."
     )

print("You're in a forest. Where do you want to go? \"left\" or \"right\"")
var_direction = input().lower()

# player survives if the answer is left
if (var_direction == "left"):
    print("\nYou find a river which splits the island in two." +
          "\nWhat do you do? \"swim\" or \"wait\""
         )
    var_choice = input().lower()

    # player survives if the answer is wait
    if (var_choice == "wait"):
        print("\nUpon waiting, a boat arrives and takes you to the other " + 
              "\nside of the island." + 
              "\nThere, you find a house having 3 doors of different colours."+
              "\nWhich door do you open? \"red\", \"blue\", or \"yellow\" door"
             )
        var_door = input().lower()

        # check the door selected
        if (var_door == "red"):
            print('''
                        Opps, you got burned by fire.
                        Game Over!
                            (  .      )
                       )           (              )
                             .  '   .   '  .  '  .
                    (    , )       (.   )  (   ',    )
                     .' ) ( . )    ,  ( ,     )   ( .
                  ). , ( .   (  ) ( , ')  .' (  ,    )
                 (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')
        elif (var_door == "blue"):
            print('''
                    Opps, you got eaten by a beast.
                    Game Over!
                              (    )
                          ((((()))
                          |o\ /o)|
                          ( (  _')
                           (._.  /\__
                          ,\___,/ '  ')
            '.,_,,       (  .- .   .    )
             \   \\     ( '        )(    )
              \   \\    \.  _.__ ____( .  |
               \  /\\   .(   .'  /\  '.  )
                \(  \\.-' ( /    \/    \)
                 '  ()) _'.-|/\/\/\/\/\|
                     '\\ .( |\/\/\/\/\/|
                       '((  \    /\    /
                       ((((  '.__\/__.')
                        ((,) /   ((()   )
                         "..-,  (()("   /
                    pils  _//.   ((() ."
                  _____ //,/" ___ ((( ', ___
                                   ((  )
                                    / /
                                  _/,/'
                                /,/,"
            ''')

        elif (var_door == "yellow"):
            print('''
            
              Hooray!!! You've won.

                  \'-=======-'/
                  _|   .=.   |_
                 ((|  {{1}}  |))
                  \|   /|\   |/
                   \__ '`' __/
                     _`) (`_
                   _/_______\_
                  /___________\

            ''')
        else:
            print("Invalid input!" + 
                  "\nGame over!")

    elif (var_choice == "swim"):
        print('''
        Opps, you got attacked by a crocodile.
        Game over!
                  .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                      (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'

        ''')
    else:
        print("Invalid input." +
              "\nGame over!"
             )
# if player chooses right --> Game over
elif (var_direction == "right"):
    print('''
            Opps, you got bitten by a snake and died.
            Game over!
                            _.--....
                 _....---;:'::' ^__/
               .' `'`___....---=-'`
              /::' (`
              '   `:.
               `\::.  ';-"":::-._  {}
            _.--'`\:' .'`-.`'`.' `{I}
         .-' `' .;;`\::.   '. _: {-I}`
       .'  .:.  `:: _):::  _;' `{=I}.:|
      /.  ::::`":::` ':'.-'`':. {_I}::/
      |:. ':'  :::::  .':'`:. `'|':|:'
        '--.:::...---'\:'.:`'`'
                       '-::..:::-'
          ''')

else:
    print("Invalid input." +
          "\nGame over!"
         )
