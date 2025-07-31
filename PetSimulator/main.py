"""
Step 4: Extensions and Advanced Practice
Goal: Add new features and explore advanced OOP concepts.
Try any or all of these ideas:
Add New Attributes:
Add attributes like energy, health, or age to your Pet class.
Create New Methods:
For example, add a sleep() method that:
Increases happiness and energy
Might increase hunger slightly
Prints the pet's updated stats
Implement a Hunger Timer:
Make hunger increase automatically after every user action or loop iteration to simulate the pet getting hungry over time.
Subclassing (Inheritance): 
Create subclasses that inherit from Pet, like Dog and Cat.
Each subclass can have unique methods:
Dog.bark()
Cat.meow()
And override existing methods for special behavior.
Set Limits and Warnings:
For example, if hunger goes above a certain level, print a warning message.
If happiness drops too low, the pet might “run away” (exit the program or remove the pet).
Multiple Pets Interaction:
Allow pets to interact with each other through methods like play_with(other_pet).
"""


class Pet:
    def __init__(self, name:str, animal_type:str, hunger:int=0, happiness:int=100, energy:int=100):
        self.__name = name
        self.__animal_type = animal_type
        self.__hunger = hunger
        self.__happiness = happiness
        self.__energy = energy
    
    def eat(self):
        print(self.__name + "'s old hunger: " + str(self.__hunger))
        print(self.__name + " has eaten ! Hunger +10")
        self.__hunger += 10
        self.__happiness += 5
        print("New Hunger: " + str(self.__hunger))
        print()
    
    def play(self):
        print(self.__name + " went on a nice walk outside and played at the park! ")
        self.__happiness += 10
        self.__energy -= 10
        # max happiness is 100
        if self.__happiness > 100:
            self.__happiness = 100
        print("Happiness: " + str(self.__happiness))
        print("Energy: " + str(self.__energy))
        print()
    
    def status(self):
        print("--- " + self.__name + "'s Status " + "---")
        print("Hunger : " + str(self.__hunger))
        print("Happiness : " + str(self.__happiness))
        print("Sleep : " + str(self.__energy))
        print()
    
    # getter/setter functions
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_hunger(self):
        return self.__hunger
    
    def get_happiness(self):
        return self.__happiness
    
    def get_energy(self):
        return self.__energy
    
    def set_hunger(self, new_hunger):
        self.__hunger = new_hunger
    
    def set_happiness(self, new_happiness):
        self.__happiness = new_happiness
    
    def set_energy(self, new_energy):
        self.__energy = new_energy
    
    
    


# make the pet objects
pets = {}
num_pets_to_make = int(input("How many pets would you like to make ? "))
for i in range(1, num_pets_to_make+1, 1):
    print("Info for pet #" + str(i))
    animal_type = input("What type of pet would you like to have ? (eg: dog, cat, bunny ...) ").title()
    name = input("What would you like to name your pet? ").title()
    pets[name] = (Pet(name, animal_type))
    print()
print("All pets created ! :)")

#menu to interact w/ pets or leave
while True:
    # choice that the user wants to do
    print("What would you like to do?")
    print("1. Feed a pet")
    print("2. Play with a pet")
    print("3. Check a pet's status")
    print("4. Exit")
    choice_action = int(input(""))
    # check if the user wants to exit before proceeding
    if choice_action == 4:
        print("Thanks for playing ! Come back soon :)")
        break
    print("Great! Which pet would you like to do this with ? Your current pets are.. :")
    # i have to use a for each loop because dictionaries are unordered collections, and I cannot refer to them by index
    for pet in pets:
        print(pets.get(pet).get_name() + " the " + pets.get(pet).get_animal_type())
    choice_pet = input().title()
    if choice_action != 3:
        if choice_action == 1:
            pets.get(choice_pet).eat()
        elif choice_action == 2:
            pets.get(choice_pet).play()
        for pet in pets:
        # set the pet's new hunger to -10 its current hunger
            pets.get(pet).set_hunger(pets.get(pet).get_hunger()-5)
        # set the pet's new energy to -10 its current energy
            pets.get(pet).set_energy(pets.get(pet).get_energy()-5)
        print("A day has passed!")
        print()
    elif choice_action == 3:
        pets.get(choice_pet).status()
