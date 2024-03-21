from characters import DndCharacter
#######################################################
# All interactions and stat updates
##############################################################


class Actions:
    #def __init__(self):
        #self.character = character

    def attack(self, attacker: DndCharacter, target: DndCharacter, damage: int):
        print(f"{attacker.name} attacks {target.name} with {damage} damage!")

    def cast_spell(self, spell_name):
        print(f"{self.character.name} casts {spell_name}!")