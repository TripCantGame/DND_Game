from characters import DndCharacter
from actions import Actions
#######################################################
#Main loop
##############################################################

if __name__ == "__main__":

    ###creates a window to create character
    #character = DndCharacter.create_character_gui()
    
    ##displays info on a character
    #Bob = DndCharacter.unpack_csv_to_character("Bob")
    #DndCharacter.display_character_info(Bob)

    ##displays a characters health
    Bob = DndCharacter.unpack_csv_to_character("Bob")
    Joe = DndCharacter.unpack_csv_to_character("Joe")
    #DndCharacter.display_character_info(Bob)
    #DndCharacter.calculate_health(Bob)
    #DndCharacter.display_health_gui(Bob)

    DndCharacter.calculate_health(Joe)
    DndCharacter.display_health_gui(Joe)

    CallAction = Actions() 
    CallAction.attack(Bob, Joe, 5)  

    DndCharacter.calculate_health(Joe)
    DndCharacter.display_health_gui(Joe)
    