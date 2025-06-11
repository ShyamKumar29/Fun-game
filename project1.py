import random
#rolling a random value
def rollrand():
    max_no = 6
    min_no = 1
    roll = random.randint(min_no,max_no)
    return roll
#getting the player count
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("Invalid number of players")
    else:
        print("Give a proper input")
#checking the score and keeping a limit
max_score = 30
player_scores = [0 for i in range(players)]

#game intro
while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "'s turn 🎲")
        print("Current total score:", player_scores[player_idx])
        
    #game start
        current_score = 0

        while True:
            action = input("Type 'r' to Roll or 'h' to Hold: ").lower()
            
            if action == 'h':
                player_scores[player_idx] += current_score
                print("You held your score.")
                print("Your total score is:", player_scores[player_idx])

                break

            elif action == 'r':
                value = rollrand()
                if value == 1:
                    print("OOPS! You rolled a 1, your turn is over and you get 0 this round ")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print("You rolled a", value)
                    print("Your current turn score is:", current_score)

            else:
                print("Invalid input. Please type 'r' or 'h'.")

            
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,"is the winner with a score of:", max_score)

