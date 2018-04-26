#csv library
import csv

# execute only if run as a script
if __name__ == "__main__":
    with open('soccer_players.csv', newline='') as csvfile:
        # read csv file as a list of dictionaries
        # Each value seperated by a comma in the first row is set as key a key value
        leagereader = csv.DictReader(csvfile)
        rows = list(leagereader)
        #Create the teams
        team1 = ['Dragons']
        team2 = ['Sharks']
        team3 = ['Raptors']
        #Two dictionaries to sort players into two groups
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
    #Counter for the for loop
    count = 0
    #Assign experienced_players to each team equally
    for player in experienced_players:
        if count<experienced_players_each_team:
            team1.append(player)
        elif count<experienced_players_each_team*2:
            team2.append(player)
        else:
            team3.append(player)
        count += 1
    #Set counter to 0 again
    count = 0
    #Assign inexperienced_players to each team equally
    for player in inexperienced_players:
        if count<inexperienced_players_each_team:
            team1.append(player)
        elif count<inexperienced_players_each_team*2:
            team2.append(player)
        else:
            team3.append(player)
        count += 1
    #Create the teams.txt file
    with open("teams.txt", "a") as file:
        #Create function that takes a team as parameter and writes it to the text file
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
