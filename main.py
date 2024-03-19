from characters import DndCharacter
from actions import Actions
#######################################################
#Main loop
##############################################################
"""
if __name__ == "__main__":
    # Assuming DndCharacter class is already defined
    character1 = DndCharacter("Gandalf", "Human", "Wizard", 10)
    character2 = DndCharacter("Enemy", "Orc", "Barbarian", 8)

    actions = Actions(character1)
    actions.attack(character2, 10)
    actions.cast_spell("Fireball")
"""
if __name__ == "__main__":

    ###creates a window to create character
    #character = DndCharacter.create_character_gui()
    
    ##displays info on a character
    #Bob = DndCharacter.unpack_csv_to_character("Bob")
    #DndCharacter.display_character_info(Bob)

    ##displays a characters health
    Bob = DndCharacter.unpack_csv_to_character("Bob")
    DndCharacter.calculate_health(Bob)
    DndCharacter.display_health_gui(Bob)
    