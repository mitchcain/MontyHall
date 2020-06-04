from random import randint
import pandas as pd

# This program assumes knowledge of the Monty Hall Problem.
# This program simulates the problem when the player plays the strategy of always switching doors.

games = input('How many games? ')  # input how many simulations are needed.
filepath = input('File Path: ')  # input file path for new csv to store results.
plays = 0  # counter for how many simulations are done.
goats = 0  # counter for how many goats won.
cars = 0  # counter for how many cars won.
result = []  # result list stores the prize as a string for each simulation.
door = []  # door list stores the door number that contained the car for ech simulation.

while plays < int(games):
    car_door = randint(1, 3)  # door with the car is randomly assigned each time.
    player_door = randint(1, 3)  # player door is randomly chosen each time.
    if car_door == 1:
        if player_door == 1:  # if the player initially chooses the door with the car ...
            goats += 1        # ... they lose as they will always switch doors.
            plays += 1        # therefore, they win a goat.
            result.append('goat')
            door.append(1)
        elif player_door == 2 or player_door == 3:  # if the player initially chooses a door ...
            cars += 1                               # ... with a goat, they win the car when ...
            plays += 1                              # ... they switch doors.
            result.append('car')
            door.append(1)
    elif car_door == 2:  # the same applies as above when the car is behind doors 2 or 3.
        if player_door == 2:
            goats += 1
            plays += 1
            result.append('goat')
            door.append(2)
        elif player_door == 1 or player_door == 3:
            cars += 1
            plays += 1
            result.append('car')
            door.append(2)
    elif car_door == 3:
        if player_door == 3:
            goats += 1
            plays += 1
            result.append('goat')
            door.append(3)
        elif player_door == 1 or player_door == 2:
            cars += 1
            plays += 1
            result.append('car')
            door.append(3)

data = {'Outcome': result, 'Door Number': door}
results = pd.DataFrame(data, columns=['Outcome', 'Door Number'])  # create a data frame to hold results.

for char in filepath:  # replace any single '\' in file path with a double (escape character).
    if char == '\\':
        filepath.replace('\\', '\\\\')
    else:
        continue

results.to_csv(filepath)  # write the results from the games to a csv file for further analysis.
