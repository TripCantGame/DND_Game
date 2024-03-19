
#######################################################
# All interactions and stat updates
##############################################################


class Actions:
    def __init__(self, character):
        self.character = character

    def attack(self, target, damage):
        print(f"{self.character.name} attacks {target.name} with {damage} damage!")

    def cast_spell(self, spell_name):
        print(f"{self.character.name} casts {spell_name}!")