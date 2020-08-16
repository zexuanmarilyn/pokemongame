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
        print(("{} now has {} health").format(self.name, self.current_health))
    
    def gain_health(self, current_health, health_gained, max_health):
        self.current_health = max( (current_health + health_gained), max_health)
        print(("{} now has {} health").format(self.name, self.current_health))
    
    fire_dictionary={'type':'fire', 'weakness':'water', 'strength':'grass'}
    water_dictionary={'type':'water', 'weakness':'grass', 'strength':'fire'}
    grass_dictionary={'type':'grass', 'weakness':'fire', 'strength':'water'}
    type_list= [fire_dictionary, water_dictionary, grass_dictionary]

    def attack (self, other_pokemon, damage):
        for dictionary in type_list:
            if self.type == dictionary.get(type):
                self.strength = dictionary.get(strength)
                self.weakness = dictionary.get(weakness)
        if self.strength == other_pokemon.type:
            damage = 


