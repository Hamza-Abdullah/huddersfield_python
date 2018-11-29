team = input("Please enter your team name: ")
wins = 0
draws = 0
losses = 0

for count in range(5):
    while True:
        try:
            scored = int(input("Goals scored in football match #" + str(count + 1) + ": "))
            against = int(input("Goals against in football match #" + str(count + 1) + ": "))
            break
        except ValueError:
            print("Please enter a valid input.")

    result = scored - against
    if result > 0:
        wins += 1
    elif result < 0:
        losses += 1
    else:
        draws += 1

points = wins * 3 + draws
print(team)
print("Wins: " + str(wins))
print("Draws: " + str(draws))
print("Losses: " + str(losses))
print("Points: " + str(points))
