
def movement():
    current_location = "beach"
    
    inventory = {"has_key": False, "rope": False}
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
        # Cave movement
        elif current_location == "Cave":
            print(f"Your current location is {current_location}")
            print("It's dark, dump and echoes with dripping water")
            choice = input("You can go 'Wast' to Jungle, 'North' to Old Bridg, what do you want to do? ").lower().strip()
            if choice == "west":
                current_location = "Jungle"
            elif choice == "north":
                current_location = "Old bridge"
                if current_location == "Old bridge":
                    while True:
                        key = input("take key: ").lower().strip()
                        rope = input("take rope: ").lower().strip()
                        if rope == "take rope":
                            inventory["rope"] = True
                            break
                        else:
                            print("no rope")
                        if key == "take key":
                            inventory["has_key"] = True
                            print(inventory)
                            break
                        else:
                            print("no key")
            elif choice == "quit":
                print("Quit")
                break
            else:
                print("You can't go that way")
        # Old Bridge
        elif current_location == "Old bridge":
            print(f"Your current location is {current_location}")
            print("A wooden bridge sways over a deep canyon.")
            choice = input("You can go east to 'Cave', 'south' to the Old bridge'. what do you want to do? ").lower().strip()
            if choice == "east":
                current_location = "Cave"
            elif choice == "south":
                current_location == "Old bridge"
                if inventory["rope"] == True:
                    print("repair bridge")
                else:
                    print("rope can't be found")
            elif choice == "quit":
                print("Quit")
                break
            else:
                print("You can't go that way")
    return current_location
