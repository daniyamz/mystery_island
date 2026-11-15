def display():
    print(" MYSTERY GAME ".center(30, "="))
    instruction = """
1. Enter player's name.
"""
    print(instruction)
    while True:
        player_name = input("Enter player name: ").strip()
        if player_name == "":
            print("Player name cannot be empty. Re-enter")
            continue
        else:
            break
    print(f"\n{player_name}, Welcome to the Game.")
display()
