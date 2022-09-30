import random

class player(object):
    # Pokemon's basic informations
    def __init__(self, pokemonName, pokemonTypeOne, pokemonTypeTwo, pokemonLevel,
                 pokemonHP, pokemonAttack, pokemonDefense, pokemonSpecialAttack, pokemonSpecialDefense, pokemonSpeed, pokemonSum):
        self.name = pokemonName
        self.typeOne = pokemonTypeOne
        self.typeTwo = pokemonTypeTwo
        self.level = pokemonLevel
        
        # Pokemon's species status
        self.HP = pokemonHP
        self.attack = pokemonAttack
        self.defense = pokemonDefense
        self.specialAttack = pokemonSpecialAttack
        self.specialDefense = pokemonSpecialDefense
        self.speed = pokemonSpeed
        self.sum = pokemonSum
        
        self.damage = 0
        
        # Pokemon's individual values
        # Random IV generator
        a= random.randint(0, 31)
        b= random.randint(0, 31)
        c= random.randint(0, 31)
        d= random.randint(0, 31)
        e= random.randint(0, 31)
        f= random.randint(0, 31)
        self.ivHP = a
        self.ivAttack = b
        self.ivDefense = c
        self.ivSpecialAttack = d
        self.ivSpecialDefense = e
        self.ivSpeed = f
        
        # Calculate stats
        # HP
        g = (self.HP * 2) + (1 / 4) + self.ivHP
        h = ((g * 50) / 100)
        self.realHP = round(h + 10 + 50)
        # Attack
        g = (self.attack * 2) + self.ivAttack + (1 / 4)
        self.realAttack = round(((g * 50) / 100) + 5)
        # Defense
        g = (self.defense * 2) + self.ivDefense + (1 / 4)
        self.realDefense = round(((g * 50) / 100) + 5)
        # Special attack
        g = (self.specialAttack * 2) + self.ivSpecialAttack + (1 / 4)
        self.realSpecialAttack = round(((g * 50) / 100) + 5)
        # Special defense
        g = (self.specialDefense * 2) + self.ivSpecialAttack + (1 / 4)
        self.realSpecialDefense = round(((g * 50) / 100) + 5)
        # Speed
        g = (self.speed * 2) + self.ivSpeed + (1 / 4)
        self.realSpeed = round(((g * 50) / 100) + 5)
        
    # Print this pokemon's status
    def printStat(self):
        print(self.name)
        print("%s + %s" % (self.typeOne, self.typeTwo))
        print("Level: %i" % self.level)
        print("HP: %i" % self.realHP)
        print("Attack: %i" % self.realAttack)
        print("Defense: %i" % self.realDefense)
        print("Special Attack: %i" % self.realSpecialAttack)
        print("Speicla Defense: %i" % self.realSpecialDefense)
        print("Speed: %i" % self.realSpeed)
        
    def battle(self):
        moveType = input("Move's type: ")
        moveDamage = input("Move's damage: ")

        i = (2 * self.level + 10) / 250
        j = i * (self.realAttack / self.realDefense)
        k = (j * 120) + 2
        l = random.randint(85, 100)
        m = (l / 100)
        
        if moveType == self.typeOne or moveType == self.typeTwo:
            n = 1.5
        else:
            n = 1
            
        addOn = n * (1 / 2) * m
        self.damage = round(k * addOn)
        

class opponent(object):
    # Opponent pokemon's basic informations
    def __init__(self, pokemonName, pokemonTypeOne, pokemonTypeTwo, pokemonLevel,
                 pokemonHP, pokemonAttack, pokemonDefense, pokemonSpecialAttack, pokemonSpecialDefense, pokemonSpeed, pokemonSum):
        self.name = pokemonName
        self.typeOne = pokemonTypeOne
        self.typeTwo = pokemonTypeTwo
        self.level = pokemonLevel
        
        # Pokemon's species status
        self.HP = pokemonHP
        self.attack = pokemonAttack
        self.defense = pokemonDefense
        self.specialAttack = pokemonSpecialAttack
        self.specialDefense = pokemonSpecialDefense
        self.speed = pokemonSpeed
        self.sum = pokemonSum
        
        # Pokemon's individual values
        # Random IV generator
        a= random.randint(0, 31)
        b= random.randint(0, 31)
        c= random.randint(0, 31)
        d= random.randint(0, 31)
        e= random.randint(0, 31)
        f= random.randint(0, 31)
        self.ivHP = a
        self.ivAttack = b
        self.ivDefense = c
        self.ivSpecialAttack = d
        self.ivSpecialDefense = e
        self.ivSpeed = f
        
        # Calculate stats
        # HP
        g = (self.HP * 2) + (1 / 4) + self.ivHP
        h = ((g * 50) / 100)
        self.realHP = round(h + 10 + 50)
        # Attack
        g = (self.attack * 2) + self.ivAttack + (1 / 4)
        self.realAttack = round(((g * 50) / 100) + 5)
        # Defense
        g = (self.defense * 2) + self.ivDefense + (1 / 4)
        self.realDefense = round(((g * 50) / 100) + 5)
        # Special attack
        g = (self.specialAttack * 2) + self.ivSpecialAttack + (1 / 4)
        self.realSpecialAttack = round(((g * 50) / 100) + 5)
        # Special defense
        g = (self.specialDefense * 2) + self.ivSpecialAttack + (1 / 4)
        self.realSpecialDefense = round(((g * 50) / 100) + 5)
        # Speed
        g = (self.speed * 2) + self.ivSpeed + (1 / 4)
        self.realSpeed = round(((g * 50) / 100) + 5)
        
    # Print this pokemon's status
    def printStat(self):
        print(self.name)
        print("%s + %s" % (self.typeOne, self.typeTwo))
        print("Level: %i" % self.level)
        print("HP: %i" % self.realHP)
        print("Attack: %i" % self.realAttack)
        print("Defense: %i" % self.realDefense)
        print("Special Attack: %i" % self.realSpecialAttack)
        print("Speicla Defense: %i" % self.realSpecialDefense)
        print("Speed: %i" % self.realSpeed)