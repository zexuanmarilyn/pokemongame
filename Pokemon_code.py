class Pokemon:
    def __init__(self, name, level, type, max_health, current_health):
        self.name=name
        self.level=level
        self.type=type
        self.max_health=max_health
        self.current_health=current_health
        if current_health == 0:
            self.knocked_out="Yes"
        else:
            self.knocked_out="No"
    
    def __repr__(self):
        return "Your {} is at level {} and has {}/{} HP.".format(self.name,self.level, self.current_health, self.max_health)

    # method for pokemon who is injured in battle
    def lose_health(self,  health_lost):
        self.current_health= self.current_health - health_lost
        if self.current_health <= 0:
            self.knocked_out = "Yes"
            return ("{} has no HP left and is knocked out").format(self.name)
        else:
            return ("{} now has {} HP").format(self.name, self.current_health)
        
    # method for pokemon who gains health (through potion consumption)
    def gain_health(self,  health_gained):
        self.current_health = min( (self.current_health + health_gained), self.max_health)
        return ("{} now has {} HP").format(self.name, self.current_health)
    

    
  # create variables for knocking out Pokemon and reviving pokemons

    # method for pokemon to attack opponent in battle
    def attack (self, other_pokemon):
        fire_dictionary={'type':'fire', 'weakness':'water', 'strength':'grass'}
        water_dictionary={'type':'water', 'weakness':'grass', 'strength':'fire'}
        grass_dictionary={'type':'grass', 'weakness':'fire', 'strength':'water'}
        type_list= [fire_dictionary, water_dictionary, grass_dictionary]
        if self.knocked_out == "Yes":
            return "{} has already fainted and cannot fight!".format(self.name)
        for dictionary in type_list:
            dictionary_type = dictionary.get("type")
            if self.type.lower() == dictionary_type:
                strength = dictionary.get("strength")
                weakness = dictionary.get("weakness")
            else:
                strength =""
                weakness = ""
        if strength == other_pokemon.type:
            damage = other_pokemon.level*2
        elif weakness == other_pokemon.type:
            damage = other_pokemon.level*.5
        else:
            damage = other_pokemon.level
        other_pokemon.lose_health(damage)
        if other_pokemon.knocked_out =="Yes":
            return ("{} has been attacked by {} and lost {} HP! {} has fainted.").format(other_pokemon.name, self.name, damage, other_pokemon.name)
        else:
            return ("{} has been attacked by {} and lost {} HP! {} HP remains.").format(other_pokemon.name, self.name, damage, other_pokemon.current_health)


class Trainer:

    def __init__(self, name, pokemon_list, no_of_potions, active_pokemon):
        self.name=name
        self.pokemon_list=pokemon_list
        self.no_of_potions=no_of_potions
        self.active_pokemon=active_pokemon
          
    def __repr__(self):
        return "You are {}. You currently have {} and {} potions in your bag. {} is ready to fight.".format(self.name, self.pokemon_list, self.no_of_potions, self.active_pokemon)
 
    # method for consumption of potion
    def potion(self):
        self.no_of_potions-=1
        self.pokemon_list[self.active_pokemon].gain_health(20)
        return "{} gained 20 HP and now has {} HP. You have {} potions left.".format(self.pokemon_list[self.active_pokemon].name, self.pokemon_list[self.active_pokemon].current_health, self.no_of_potions)

    # method for starting trainer battle
    def trainer_battle(self, other_trainer):
        return self.pokemon_list[self.active_pokemon].attack(other_trainer.pokemon_list[other_trainer.active_pokemon])
    
    # method for changing active pokemon
    def switch_active_pokemon(self, new_active_pokemon):
        if self.pokemon_list[new_active_pokemon].knocked_out == "Yes":
            return "{} has fainted and cannot be the lead pokemon.".format(self.pokemon_list[new_active_pokemon].name)
        self.active_pokemon = new_active_pokemon
        return "{} is now the lead pokemon.".format(self.pokemon_list[self.active_pokemon].name)

    




# example of pokemon game logic:

# setting up individual pokemon stats:
Squirtle = Pokemon("Squirtle",21,"water",100,54)
Charmander = Pokemon("Charmander", 24, "fire", 123, 43)
Bulbasaur  = Pokemon("Bulbasaur", 20, "grass", 87, 87)
Pikachu  = Pokemon("Pikachu", 25, "electric", 100, 80)
Torchic = Pokemon("Torchic", 30, "fire", 100, 0) 

print(Squirtle)
print(Charmander)
print(Bulbasaur)
print(Torchic)

# example pokemon battle
#battle between Squirtle and Charmander
#Squirtle to attack first
print(Squirtle.attack(Charmander))

#example trainer class
Ash = Trainer("Ash", [Squirtle, Pikachu, Torchic], 10, 1)
Misty = Trainer("Misty", [Bulbasaur, Charmander], 5, 0)

print(Ash.potion())
print(Ash.switch_active_pokemon(2))
print(Ash.trainer_battle(Misty))





