import tkinter as tk
from tkinter import messagebox
import csv
import os

#######################################################
# All player related functions
##############################################################

class DndCharacter:
    def __init__(self, name, race, character_class, level, abilities, abl_strength,  abl_wisdom, abl_charisma):
        #, abl_dexterity, abl_constitution, abl_intelligence):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.health = self.calculate_health()
        self.abl_strength = abl_strength
        #self.abl_dexterity = abl_dexterity
        #self.abl_constitution = abl_constitution
        #self.abl_intelligence = abl_intelligence
        self.abl_wisdom = abl_wisdom
        self.abl_charisma = abl_charisma
        self.abilities = abilities



    @staticmethod
    def unpack_csv_to_character(name):
        print(f'Current Directory:{os.getcwd()}')
        filename = f"Stats/{name}-stats.csv"
        print(f'Working Directory:{filename}')
        if os.path.exists(filename):
            try:
                with open(filename, 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        name = row['Name']
                        race = row['Race']
                        character_class = row['Class']
                        level = int(row['Level'])
                        abilities = row['Abilities']
                        abl_strength = int(row['Strength'])
                        abl_wisdom = int(row['Wisdom'])
                        abl_charisma = int(row['Charisma'])

                        character = DndCharacter(name, race, character_class, level, abilities, abl_strength, abl_wisdom, abl_charisma)
                        return character
            except Exception as e:
                print(f"Error reading CSV file '{filename}': {e}")
        else:
            print(f"File '{filename}' does not exist.")
        
    def display_character_info(self):
        root = tk.Tk()
        root.title("Character Information")
        if self is None:
            return None
        else:
        
            info_text = (
            f"Name: {self.name}\n"
            f"Race: {self.race}\n"
            f"Class: {self.character_class}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"Strength: {self.abl_strength}\n"
            f"Wisdom: {self.abl_wisdom}\n"
            f"Charisma: {self.abl_charisma}"
        )
        info_label = tk.Label(root, text=info_text)
        info_label.pack()

        root.mainloop()

    def calculate_health(self):
        # This is a simple calculation, you might want to make it more complex
        base_health = 10  # Assuming base health
        health_per_level = 5  # Assuming health increases by 5 per level
        return base_health + (self.level * health_per_level)
    
    def display_health_gui(self):
        root = tk.Tk()
        root.title("DND Character Health")

        label = tk.Label(root, text=f"{self.name}'s Health: {self.health}")
        label.pack()

        root.mainloop()


    def create_csv(self, filename):
        if not filename.endswith('.csv'):
            filename += '.csv'  # Append .csv extension if missing
        
        with open(f'Stats/{filename}', 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Race', 'Class', 'Level', 'Health', 'Strength', 'Wisdom', 'Charisma', 'Abilities']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'Name': self.name,
                             'Race': self.race,
                             'Class': self.character_class,
                             'Level': self.level,
                             'Health': self.health,
                             'Strength': self.abl_strength,
                             'Wisdom': self.abl_wisdom,
                             'Charisma': self.abl_charisma,
                             'Abilities': self.abilities})

    @staticmethod
    def create_character_gui():
        def create_character():
            name = name_entry.get()
            race = race_entry.get()
            character_class = class_entry.get()
            level = int(level_entry.get())

            strength = int(level_entry.get()) 
            #dexterity = int(level_entry.get())
            #constitution = int(level_entry.get())
            #intelligence = int(level_entry.get())
            wisdom = int(level_entry.get())
            charisma = int(level_entry.get())

            abilities = {
            "Strength": strength,
            #"Dexterity": dexterity,
            #"Constitution": constitution,
            #"Intelligence": intelligence,
            "Wisdom": wisdom,
            "Charisma": charisma
                        }
            new_character = DndCharacter(name, race, character_class, level, abilities, strength,  wisdom, charisma)
            #dexterity, constitution, intelligence,
            messagebox.showinfo("Character Created", f"Character {name} created successfully!")
            new_character.create_csv( name + "-stats")
            return new_character

        root = tk.Tk()
        root.title("Create DND Character")

        tk.Label(root, text="Name:").grid(row=0, column=0)
        tk.Label(root, text="Race:").grid(row=1, column=0)
        tk.Label(root, text="Class:").grid(row=2, column=0)
        tk.Label(root, text="Level:").grid(row=3, column=0)
        tk.Label(root, text="Strength:").grid(row=4, column=0)
        tk.Label(root, text="Wisdom:").grid(row=5, column=0)
        tk.Label(root, text="Charisma:").grid(row=6, column=0)

        name_entry = tk.Entry(root)
        race_entry = tk.Entry(root)
        class_entry = tk.Entry(root)
        level_entry = tk.Entry(root)
        strength_entry = tk.Entry(root)
        wisdom_entry = tk.Entry(root)
        charisma_entry = tk.Entry(root)

        name_entry.grid(row=0, column=1)
        race_entry.grid(row=1, column=1)
        class_entry.grid(row=2, column=1)
        level_entry.grid(row=3, column=1)
        strength_entry.grid(row=4, column=1)
        wisdom_entry.grid(row=5, column=1)
        charisma_entry.grid(row=6, column=1)

        create_button = tk.Button(root, text="Create Character", command=create_character)
        create_button.grid(row=7, columnspan=2)

        root.mainloop()



