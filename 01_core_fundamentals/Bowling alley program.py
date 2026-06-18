#bowling alley program
player_list = []
playernames = input("Enter a player name: ")
while playernames.lower() != "done":
    player_list.append(playernames.title())
    playernames = input("Enter a player name or type done to finish: ")
print(f"There are {len(player_list)} players")
print(f"Here is the list of players: {', '.join(player_list)}")
