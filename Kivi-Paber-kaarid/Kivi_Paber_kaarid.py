import random

options = ["Kivi","Paber","Käärid"]
voor = 1
player_one_wins = 0
player_two_wins = 0
try:
    player_one = input("Sisestage esimese mängija nimi: ")
except:
    ValueError

try:
    player_two = input("Sisestage teise mängija nimi (või tippige robotmängija jaoks *Bot*): ")
except:
    ValueError

while True:
    # Esimene mängija teeb valiku
    player_one_choice = input(f"{player_one}: Kivi, Paber või käärid? ").capitalize()
    if player_one_choice not in options:
        print("Kehtetu valik. Valige kivi, paber või käärid.")
        continue

    # Mängija kaks teeb valiku (arvuti genereerib juhuslikult, kui mängija_kaks on robot)
    if player_two == "Bot":
        player_two_choice = random.choice(options)
    else:
        player_two_choice = input(f"{player_two}: Kivi, Paber või käärid? ").capitalize()
        if player_two_choice not in options:
            print("Kehtetu valik. Valige kivi, paber või käärid.")
            continue

    print(f"{player_one} valinud {player_one_choice} ja {player_two} valinud {player_two_choice}")
    # Kontrollige vooru tulemust
    if player_one_choice == player_two_choice:
        result = "viig"
    elif (player_one_choice == "Kivi" and player_two_choice == "Käärid") or (player_one_choice == "Paber" and player_two_choice == "Kivi") or (player_one_choice == "Käärid" and player_two_choice == "Paber"):
        result = player_one
        player_one_wins += 1
    else:
        result = player_two
        player_two_wins += 1
    if result == "Viik":
        print(f"Voor {voor}: {result}")
        voor+=1
    else:
        print(f"Voor {voor}: {result} võidab")
        voor+=1

    # Kontrollige, kas mängija on võitnud 3 vooru
    if player_one_wins == 3:
        print(f"{player_one} võidab mängu!")
        break
    elif player_two_wins == 3:
        print(f"{player_two} võidab mängu")
        break
