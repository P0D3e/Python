import random

def play_game():
    rps_list = ("rock", "paper", "scissors")

    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        player_choice = input("Enter a choice (rock, paper, scissors): ")
        computer_choice = random.choice(rps_list)

        print(f"\nYou chose {player_choice}, computer chose {computer_choice}.\n")

        tie = f"You both selected {player_choice} and the round is tied"
        rock1 = f"You chose rock and crushed the scissors, Your current score is {player_score + 1}"
        rock2 = f"The computer crushed your scissors with his rock, Computer's current score is {computer_score + 1}"
        paper1 = f"You chose paper and grabbed the stone, Your current score is {player_score + 1}"
        paper2 = f"The computer grabbed your stone, Computer's current score is {computer_score + 1}"
        scissor1 = f"Your scissors cut the paper in half, Your current score is {player_score + 1}"
        scissor2 = f"The computer cut your paper in half with his scissors, Computer's current score is {computer_score + 1}"

        if player_choice == computer_choice:
            print(tie)
        if player_choice == "rock" and computer_choice == "scissors":
            print(rock1)
            player_score += 1
        if player_choice == "paper" and computer_choice == "rock":
            print(paper1)
            player_score += 1
        if player_choice == "scissors" and computer_choice == "paper":
            print(scissor1)
            player_score += 1
        if computer_choice == "rock" and player_choice == "scissors":
            print(rock2)
            computer_score += 1
        if computer_choice == "paper" and player_choice == "rock":
            print(paper2)
            computer_score += 1
        if computer_choice == "scissors" and player_choice == "paper":
            print(scissor2)
            computer_score += 1

    print(f"\nYour final score: {player_score}")
    print(f"Computer's final score: {computer_score}")
     
    if player_score == 3:
        print("You won!")
    else:
        print("Computer won!")
        print("\nGame Over!")

while True:
    play_game()

    replay = input("Do you want to play again? (y/n): ")
    if replay.lower() != 'y':
        break