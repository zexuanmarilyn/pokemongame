class Pokemon:
    def __init__(self, name, level, type, max_health, current_health, knocked_out):
        self.name=name
        self.level=level
        self.type=type
        self.max_health=max_health
        self.current_health=current_health
        self.knocked_out=knocked_out
    
    def lose_health(self, current_health, health_lost):
        self.current_health=current_health - health_lost
        return print(("{} now has {} health").format(self.name, self.current_health))
    
    def gain_health(self, current_health, health_gained, max_health):
        self.current_health = max( (current_health + health_gained), max_health)
        return print(("{} now has {} health").format(self.name, self.current_health))
    
    #for question 3, create variables for knocking out Pokemon and reviving pokemons



    def attack (self, other_pokemon, damage):
        fire_dictionary={'type':'fire', 'weakness':'water', 'strength':'grass'}
        water_dictionary={'type':'water', 'weakness':'grass', 'strength':'fire'}
        grass_dictionary={'type':'grass', 'weakness':'fire', 'strength':'water'}
        type_list= [fire_dictionary, water_dictionary, grass_dictionary]
        for dictionary in type_list:
            if self.type == dictionary.get(type):
                self.strength = dictionary.get("strength")
                self.weakness = dictionary.get("weakness")
        if self.strength == other_pokemon.type:
            damage = other_pokemon.level*2
        elif self.weakness == other_pokemon.type:
            damage = other_pokemon.level*.5
        else:
            damage = other_pokemon.level
        other_pokemon.lose_health(damage)
        return print(("Your pokemon has been attacked and lost {} health").format(damage))

    #before continuing, test out the above functions with some examples and debug if needed

    


