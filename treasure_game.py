print(''' _                                     _   
  _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_| ''')
                                                                 

print("welcome to tragure ")
choise1 = input("your mission is to chouse one of the 'left', 'Right' :- " ).lower()

if choise1 == "left":
  choise2 = input("Swim or wait ").lower()
  if choise2 == "wait":
      choise3 = input("which door 'red', 'Blue', 'Yellow' ")
      if choise3 == "Yellow":
        print("You win !")
      elif choise3 == "Red" or "Blue":
        print("Game over!")  
  else:
      print("game over")
else:
    print("game over")
    
    #to un this code go to the website iamom1.github.io/treasure_game
    # give the code a star
