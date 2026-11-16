
def movement():
    current_location = "beach"
    while True:
        # Beach movement
        if current_location == "beach":
            print(f"Your current location is {current_location}\n")
            print("Warm sand stretches along the shore. Waves crash nearby.")
            choice = input("You can go 'North' to the Jungle. ").lower().strip()
            if choice == "north":
                current_location = "jungle"
            elif choice == "quit":
                print("Quit")
                break
            else:
                print("You can't go thet way.")

        # Jungle movement
        elif current_location == "jungle":
            print(f"Your current location is {current_location}")
            print("Thick vines and tall trees block out most of the sunlight.")
            choice = input("You can go 'South' to the Beach or you can go 'East' to Cave. what do you do? ").lower().strip()
            if choice == "south":
                current_location = "Beach"
                print(f"Your current location {current_location}")
                continue
            elif choice == "east":
                current_location = "Cave"
            elif choice == "quit":
                print("Quit")
                break
            else:
                print("you can't that way.")

movement()