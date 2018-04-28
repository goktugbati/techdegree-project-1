#csv library
import csv

# execute only if run as a script
if __name__ == "__main__":
    with open('soccer_players.csv', newline='') as csvfile:
        # read csv file as a list of dictionaries
        # Each value seperated by a comma in the first row is set as a key value
        leagereader = csv.DictReader(csvfile)
        rows = list(leagereader)
        #Create the teams
        team1 = ['Dragons']
        team2 = ['Sharks']
        team3 = ['Raptors']
        #Two lists to sort players into two groups
        experienced_players = []
        inexperienced_players = []
        #Iterates over the list and
        for row in rows:
            #If the player is experienced add it to the experienced_players list
            if row['Soccer Experience'] == 'YES':
                experienced_players.append(row['Name'] + ',' +
                                           row['Height (inches)'] + ',' +
                                           row['Soccer Experience']+ ',' +
                                           row['Guardian Name(s)']
                                           )
            #Otherwise add it to the inexperienced_players list
            elif row['Soccer Experience'] == 'NO':
                inexperienced_players.append(row['Name'] + ',' +
                                           row['Height (inches)'] + ',' +
                                           row['Soccer Experience']+ ',' +
                                           row['Guardian Name(s)']
                                           )
    #Find number of experienced and inexperienced players players to assign each team
    experienced_players_each_team = len(experienced_players) / 3
    inexperienced_players_each_team = len(inexperienced_players) / 3
    #Create a function that takes a list and a number as parameters and iterates over the list
    def add_players(player_list, number_of_players):
        #Counter for the for loop
        count = 0
        for player in player_list:
            if count<number_of_players:
                team1.append(player)
            elif count<number_of_players*2:
                team2.append(player)
            else:
                team3.append(player)
            count += 1
    #Assign experienced_players to each team equally
    add_players(experienced_players, experienced_players_each_team)

    #Assign inexperienced_players to each team equally
    add_players(inexperienced_players, inexperienced_players_each_team)

    #Create the teams.txt file
    with open("teams.txt", "a") as file:
        #Create a function that takes a team as parameter and writes it to the text file
        def add_team(team):
            for player in team:
                file.write(player + "\n")
            file.write("\n")
        #Add first team
        add_team(team1)
        #Add second team
        add_team(team2)
        #Add third team
        add_team(team3)
