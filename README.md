<div align = "center">
  
# Mystery Island Game
</div>

## Game story
You wake up on Mystery Island after a storm. The lighthouse is dark, the bridge is locked, and a rescue boat will arrive only if you restore the beacon. 
Build a text-based adventure in which the player explores locations, collects objects, solves simple puzzles and either escapes or runs out of energy.

### Problem statement
I need to build a command-line, turn-based text game where a player navigate a connected map of locations to complate two sequential goals, that's unlocking
a bridge and restoring a lighthouse beacon before their energy counter turns zero, their energy level start at 5. The system must track the player's current
location, inventory items and remaining energy, while validating text commands and preventing progress past locked obstacles untill the required items are used.
The game ends cleanly when the player triggers the win condition, lost when the energy reaches zero or when the player quits
