from setting import *

# Ferrothorn test
ferrothorn = player("Ferrothorn", "Grass", "Iron", 50,
                     74, 94, 131, 54, 116, 20, 489)
ferrothorn.printStat()

print()

# Chandelure test
chandelure = opponent("Chandelure", "Ghost", "Fire", 50,
                     60, 55, 90, 145, 90, 80, 520)
chandelure.printStat()

ferrothorn.battle()

print()
print("Ferrothorn uses Power Whip!")
print("The damage is %i" % ferrothorn.damage)
chandelure.realHP -= ferrothorn.damage
chandelure.realHP = 0 if chandelure.realHP < 0 else chandelure.realHP
print("Chandelure's HP: %i" % chandelure.realHP)