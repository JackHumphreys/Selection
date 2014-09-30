#Footbal Score

team1 = input("Please enter team one: ")
team2 = input("Please enter team two: ")

score1 = int(input("Please enter {0}'s score:".format(team1)))
score2 = int(input("Please enter {0}'s score:".format(team2)))

if score1>score2:
    print("{0} recieve 3 points and {1} recieve 0 points".format(team1, team2))

elif score1==score2:
    print("{0} recieve 1 point and {1} recieve 1 point".format(team1, team2))

elif score1<score2:
    print("{0} recieve 0 points and {1} recieve 3 points".format(team1, team2))
