class Pokemon:
    def __init__(self, name, level, type, max_health, current_health, knocked_out):
        self.name=name
        self.level=level
        self.type=type
        self.max_health=max_health
        self.current_health=current_health
        self.knocked_out=knocked_out
    
    def __repr__(self):
        return "Your {} is at level {} and has {}/{} HP.".format(self.name,self.level, self.current_health, self.max_health)


    def lose_health(self,  health_lost):
        self.current_health= self.current_health - health_lost
        if self.current_health <= 0:
            self.knocked_out = "Yes"
            return ("{} has no HP left and is knocked out").format(self.name)
        else:
            return ("{} now has {} HP").format(self.name, self.current_health)
    
    def gain_health(self,  health_gained):
        self.current_health = min( (self.current_health + health_gained), self.max_health)
        return ("{} now has {} HP").format(self.name, self.current_health)
    

    
    #for question 3, create variables for knocking out Pokemon and reviving pokemons



    def attack (self, other_pokemon):
        fire_dictionary={'type':'fire', 'weakness':'water', 'strength':'grass'}
        water_dictionary={'type':'water', 'weakness':'grass', 'strength':'fire'}
        grass_dictionary={'type':'grass', 'weakness':'fire', 'strength':'water'}
        type_list= [fire_dictionary, water_dictionary, grass_dictionary]

        for dictionary in type_list:
            dictionary_type = dictionary.get("type")
            if self.type.lower() == dictionary_type:
                strength = dictionary.get("strength")
                weakness = dictionary.get("weakness")
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
            return ("{} has been attacked by {} and lost {} HP! {} HP remains. {}").format(other_pokemon.name, self.name, damage, other_pokemon.current_health)

    #before continuing, test out the above functions with some examples and debug if needed

#example test:
Squirtle = Pokemon("Squirtle",21,"water",100,54,"No")
Charmander = Pokemon("Charmander", 24, "fire", 123, 43, "No")

print(Squirtle)
print(Charmander)

#battle between Squirtle and Charmander
#Squirtle to attack first
print(Squirtle.attack(Charmander))



