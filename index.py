import random

print("""
                   !!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!!
                   !!                                                     !!
                   !!       ROCK          PAPER          SCISSORS         !!
                   !!                                                     !!
                   !!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!!
                   """)

print("""
                                         r => Rock
                                         p => Paper
                                         s => Scissors
                            """)
    
turns = 10
no_of_turns = 0
player_point = 0
computer_point = 0

list = ["r", "p", "s"]

while no_of_turns < turns:
    player_input = input("Rock(r), Paper(p), Scissors(s) : ")
    computer_input = random.choice(list)

    if player_input == computer_input:
      print("This is a tie!!")

#rock
    elif player_input == "r" and computer_input == "p":
       computer_point = computer_point + 1
       print(f"You select '{player_input}' and computer select '{computer_input}'")
       print("Computer won 1 point")
       print(f"Your point is : '{player_point}' and computer point is : '{computer_point}'")

    elif player_input == "r" and computer_input == "s":
       player_point = player_point + 1
       print(f"You select '{player_input}' and computer select '{computer_input}'")
       print("You won 1 point")
       print(f"Your point is : '{player_point}' and computer point is : '{computer_point}'")

#paper
    elif player_input == "p" and computer_input == "r":
       player_point = player_point + 1
       print(f"You select '{player_input}' and computer select '{computer_input}'")
       print("You won 1 point")
       print(f"Your point is : '{player_point}' and computer point is : '{computer_point}'")

    elif player_input == "p" and computer_input == "s":
       computer_point = computer_point + 1
       print(f"You select '{player_input}' and computer select '{computer_input}'")
       print("Computer won 1 point")
       print(f"Your point is : '{player_point}' and computer point is : '{computer_point}'")

#scissors
    elif player_input == "s" and computer_input == "r":
       computer_point = computer_point + 1
       print(f"You select '{player_input}' and computer select '{computer_input}'")
       print("Computer won 1 point")
       print(f"Your point is : '{player_point}' and computer point is : '{computer_point}'")

    elif player_input == "s" and computer_input == "p":
       player_point = player_point + 1
       print(f"You select '{player_input}' and computer select '{computer_input}'")
       print("You won 1 point")
       print(f"Your point is : '{player_point}' and computer point is : '{computer_point}'")

    else:
       print(f"""   Enter the correct option!!!
 (Rock(r), Paper(p), Scissors(s))""")
    
    no_of_turns = no_of_turns +1
    print(f"You have '{turns - no_of_turns}' turns out of '{turns}'")
    print("_______________________________________________")
    print("   ")
print("                                       --- GAME  OVER ---  ")

if player_point == computer_point:
  print(f"""
                   ||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||
                   ||                                                    ||
                   ||            <<<< THE GAME IS TIE >>>>               ||
                   ||                                                    ||
                   ||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||
            """)

elif player_point > computer_point:
  print(f"""
                   ||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||
                   ||                                                    ||
                   ||                  <<<< YOU WON >>>>                 ||
                   ||     Your point is '{player_point}' and computer point is '{computer_point}'    ||
                   ||                                                    ||
                   ||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||
            """)

else:
  print(f"""
                   ||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||
                   ||                                                    ||
                   ||             <<<< COMPUTER WON >>>>                 ||
                   ||     Your point is '{player_point}' and computer point is '{computer_point}'    ||
                   ||                                                    ||
                   ||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||o||
                   """)
