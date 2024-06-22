"""
Firstname: Hasini
Lastname: Jayasekara
Username: hjayasekara
StudentID: 165513235
Email: hjayasekara@myseneca.ca
"""

import sys
from random import randint

# 1 Marks
def rolldice():
    """
    function: rolldice prints two random numbers between 1 and 6 simulate two dices rolling. 
    The function should also print output of the numbers generated (Eg: 6 and 6) 
    return: int:total (total of two random numbers) 
    """
    #define the randome numbers
    randdice1=randint(1,6)
    randdice2=randint(1,6)

    #total of the rolling values
    totaldiceval=randdice1+randdice2

    #printing the values
    print(f"{randdice1} and {randdice2}")

    #returning totalvalue
    return totaldiceval

# 1 Marks 
def getplayers(): 
    """
    function:This functions asks user to provide an input of number of players. 
    Based on the number of players asks player names and create a list of player names and return player names
    If user entered invalid input for number of players (eg: string (a)) it throws an error and asks to retry 
    :return list:players (list of playernames entered by user)
    """
  #defines player name list
    player_names=[]
    while True:
      no_of_players= input("Please enter the number of players: ")
      
      #checks if the input is empty 
      if no_of_players == "":
         print("Invalid input please try again")
         break

      #checks if the user input is not a numerical value
      elif not no_of_players.isnumeric():
         print("Invalid input please try again")
      else:
         #convert the input in to a numeric value
         player_count= int(no_of_players)

      # for loop to iterate through the player names and add to the player name list
         for i in range(player_count):
                  player_name = input(f"Please enter player #{i+1} name : ")
                  player_names.append(player_name)
         return player_names

  
# 1 Marks 
def getrounds(): 
    """
    function: This function asks user to enter the number of rounds they going to play 
    Based on the number of rounds entered as long it is valid return the number of rounds otherwise keep asking until a valid number entered. 
    :return int:roundcount (number of rounds)
    """
    # Implement your function here
    while True:
        no_of_rounds = input("Please enter the number of rounds to play: ")

        # Check if the input is empty or not a numerical value
        if no_of_rounds.strip() == "" or not no_of_rounds.isnumeric():
            print("Invalid input, please try again.")
        else:
            round_count = int(no_of_rounds)

            # Check if the round count is a positive number
            if round_count <= 0:
                print("Invalid input, please try again.")
            else:
                return round_count
     

# 4 Marks 
def setgame():
    """
    function: This functions use the getplayers() function and getrounds() function to get player list and round count
    Using the above values setup a two dimensional (2D) list called game. The game list will have lists elements for each round and player 
    Eg: [[score1_1, score1_2, score1_3], [score2_1, score2_2, score2_3], [score3_1, score3_2, score3_3]]
    In this above example score1_1 is player1's score for round 1. Score3_1 is player 3's score for round 1. Score 2_3 is player 2's score for round3 
    Hence each list element in game will represent a player
    Each score (int) element in the nested list element will represent a round for that player
    Finally return a gameset list which has the game list, players list, and number of rounds
    return: list:gameset (Eg gameset returned will be a list [game, players, roundcount]. In the gameset list game is lit, players is list and roundcount is integer)
    """ 
    players = getplayers() # Calling getplayers and getting player list 
    roundcount = getrounds() # Calling getrounds and getting roundcount 
    # Implement your function here 

    #initializing the game array 
    game =[]

     # Adding the scores as a two-dimensional array 
    for i in range(len(players)):
        scores = []
        for j in range(roundcount):
            scores.append(0)
        game.append(scores)

    gameset = [game, players, roundcount]
    return gameset

# 1 Marks 
def asktoroll(player): 
    """
    function: This function takes player name and asks player to hit enter to roll the dice. 
    When user hit enter calls the rolldice function and returns a score 
    :param string:player (player input is string called player name)
    :return int:score (Returns score from roll dice)
    """
    # Implement your function here
    
    input(f"{player}! Hit enter once you are ready to roll your dices!")
    score =rolldice()
    return score

# 2 Marks 
def findwinner(game, players):
    """
    function: This function takes game list (2D list) and the player list as input parameters. Goes through the game and find the player that has the highest score
    Return the winning player name as string. If more than one player winning (eg: same score) return a winner string with all players comma seperated (Eg: John, Kate)
    :param list:game (Game list)
    :param list:players (Players list)
    :return string:winner (Winning players name as string)
    """ 
    # Implement your function here 
    highestscore = 0
    winners = []

    for i in range(len(players)):
        totalscore = sum(game[i])
        if totalscore > highestscore:
            highestscore = totalscore
            winners = [players[i]]
        elif totalscore == highestscore:
            winners.append(players[i])

    # Join the list of winners with ', ' without extra spaces
    return ','.join(winners)
   

# 5 Marks 
def rungame():
    """
    function: This function runs the game 
    It sets the game first using setgame() function. It gets the game, players and roundcount from setgame
    It prints the header and Round 1 begining score card first with inital scores set to 0
    It then asks use to roll dices using asktoroll function for all rounds and players 
    When the game finish it prompts for continuation and if chose to continue run the game again otherwise terminate.
    """
    while True:

      # The next 5 lines are to get you started 
      # Implement the rest of the code 
      gameset = setgame() # Calling the setgame to get game info 
      game = gameset[0] # Getting game list 
      players = gameset[1] # Getting playerlist 
      roundcount = gameset[2] # Getting roundcount 
      printgame(game, players, 0, roundcount) # Calling printgame to print the first score card.
    
    # Playing rounds
      for roundnum in range(1, roundcount + 1):
            print(f"Round {roundnum} starts.")
            for j, player in enumerate(players):
                #print(f"{player},{roundnum}.")
                score = asktoroll(player)
                game[j][roundnum - 1] = score
                printgame(game, players, roundnum, roundcount)
        
      winner = findwinner(game, players)
      print(f"Congratulations {winner}! You are our WINNER!")
        
      choice = input("Would you like to play another game ?\n [1] Yes \n [2] No \n Your choice: ").strip().lower()
      if choice == "2":
            print("Thank you for playing!")
            break

# 5 Marks
def printgame(game, players, roundnum, roundcount): 
    """
    This function takes in game list, players list, round number (aka which round is active), totalround count as input parameters
    The function prints left aligned pretty table of the game with Rounds in columns and players in rows 
    Sample Output:
    ****************** End of Round 3 ******************
            Round 1   Round 2   Round 3   Total     
    Appla     8         7         4         19        
    Applb     11        5         8         24        
    Applc     9         3         5         17        
    Appld     8         8         7         23        
    ****************************************************
    The Stars and the Round title (End of Round) are calculated and aligned as number of rounds changes. 
    This function does not return anything
    """

    round_label_length = len(f"Round {roundcount}")# Calculate the length of the round label 
    title_length = len(f" End of Round {roundnum} ")# Calculate the length of the title

     # Calculate the total length of the table
    total_length = (round_label_length + 2) * roundcount + 12  # +12 for " Total " and spaces
    
    # Print the top border
    print("*" * total_length)

    # Print the title
    print(f"{' ' * ((total_length - title_length) // 2)} End of Round {roundnum} {' ' * ((total_length - title_length) // 2)}")
    
    # Print the header
    header = " " * 8 + "".join([f"Round {r:<{round_label_length}} " for r in range(1, roundcount + 1)]) + "Total"
    print(header)
    
    # Print each player's scores
    for i, player in enumerate(players):
        row = f"{player:<8}"
        total_score = 0
        for j in range(roundcount):
            score = game[i][j] if j < roundnum else 0
            row += f"{score:<{round_label_length + 2}}"
            total_score += score
        row += f"{total_score:<6}"
        print(row)
    
     # Print the bottom border
    print("*" * total_length)
       
    

def game():
    """
    function: Game function to run game 
    """
    rungame() # calling run game 

if __name__ == "__main__":
    """
    Main code block to run the code
    """
    game() # calling game in main block
    