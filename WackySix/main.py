from PlayerClass import Player
import time


def displayOptions(players):
    choice = input("Options: \n\t1. Enter Scores\n\t2. Adjust Score\n\t3. Display Current Scores\n\t4. End Game\n\t::")
    match(choice):
            case "1":
                for i in range(0,len(players)):
                    score = int(input(f"{players[i].name}'s Score for Round {players[i].round}: "))
                    players[i].round += 1
                    players[i].addScores(score)
            case "2":
                player = input("Which players score needs to be adjusted? ")
                index = int(input("Which round was it? "))
                adjustment = int(input("How much needs to be subtracted (enter negative #) or added (enter positive number)? "))
                for i in range(0,len(players)):
                    if players[i].name.lower() == player.lower():
                        players[i].editScore(adjustment,index)
                        print("Updated!")
                        break
                    elif i == len(players)-1:
                        print(f"Error:\n\tName '{player}' was not found or doesn't exist. Check your spelling")
                        displayOptions(players)
            case "3":
                #print player names &
                #print player scores
                print("Name:          ", end="", flush=True)
                for i in range(len(players[0].roundScores)):
                    print(f"Round {i+1}:    ", end="",flush=True)
                print("Total:  ")
                for player in players:
                    for index in range(0,len(player.roundScores)):
                        if index == 0:
                            print(f"{player.name}:            ", end="",flush=True)
                        print(f"{player.roundScores[index]}          ", end="", flush=True)
                        if index == len(player.roundScores)-1:
                            print(f"{player.totalScore}",end="",flush=True)
                    print('\n')
            case "4":
                print("\n")
                print("Totaling", end="", flush=True)
                for i in range(3):
                    time.sleep(1)
                    print(".",end="",flush=True)
                print("\n")
                time.sleep(1)
                displayWinner(players)
                exit()
            case _:
                print("Invalid choice. Please try again.")
                displayOptions(players)
                    
                
                

def displayWinner(players):
    players.sort(key=lambda x: x.totalScore)
    print(f"######################################\n\n\t1st Place: {players[0].name}\n\t    Score: {players[0].totalScore}\n\t2nd Place: {players[1].name}\n\t    Score: {players[1].totalScore}\n\t3rd Place: {players[0].name}\n\t    Score: {players[0].totalScore}\n\t \n######################################")

def playGame(players):
    #create player array
    objs = []
    objs.sort
    for obj in range(players):
        name = input("Enter players name (For easier to read scores, keep names 4-5 characters): ")
        obj = Player(name)
        objs.append(obj)
    # Provide options for score keeping
    while(True):
        displayOptions(objs)
        
        

if __name__ == "__main__":
    print("\n\n")
    print("########################################")
    print("#      Wacky Six Score Calculator      #")
    print("########################################\n\n")

    players = int(input("How many people are playing? "))
    playGame(players)
