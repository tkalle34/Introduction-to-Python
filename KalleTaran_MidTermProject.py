"""
Mid-Term Project
Python 1
UCLA Extension
author: Taran Kalle

< Description of the program >

** be sure to RENAME the file <Last><First>_MidTermProject.py
** example: BeemerBill_MidTermProject.py
"""

"""
TODO

Flavor Text
End Game Screen
"""



import random

isGameOver = False
mapBase = [
          # 0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
          ["#","o","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"], # 0
          ["#","o","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"], # 1
          ["#","o","#","#","#","#","#","a","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"], # 2
          ["#","o","o","e","#","#","#","m","#","#","#","#","#","#","#","#","#","o","o","r","#","#","#","#","#","#"], # 3
          ["#","#","#","o","#","#","#","o","#","#","#","#","o","r","#","#","#","e","#","#","#","#","#","#","#","#"], # 4
          ["#","#","#","o","o","#","#","o","#","#","#","#","o","#","#","#","o","o","#","#","#","#","#","#","#","#"], # 5
          ["#","#","#","#","c","o","o","o","#","#","#","o","o","#","#","#","o","#","#","#","#","#","#","#","#","#"], # 6
          ["#","#","#","#","o","#","#","#","#","#","#","e","#","#","#","#","o","#","#","o","o","o","x","#","#","#"], # 7
          ["#","#","#","o","o","#","#","#","#","#","#","o","#","#","#","#","o","o","m","c","#","#","#","#","#","#"], # 8
          ["#","#","#","o","#","#","#","#","o","o","e","o","o","o","e","o","o","#","#","#","#","#","#","#","#","#"], # 9
          ["#","#","#","e","w","#","#","#","e","#","#","#","#","#","o","#","#","#","#","#","#","#","#","#","#","#"], # 10
          ["#","#","#","o","#","#","#","#","o","#","#","#","#","#","c","#","#","#","#","#","#","#","#","#","#","#"], # 11
          ["#","#","#","o","#","#","o","o","o","#","#","#","#","#","o","#","#","#","#","#","#","#","#","#","#","#"], # 12
          ["#","#","#","o","o","c","o","#","o","#","#","#","#","#","o","m","#","#","#","#","#","#","#","#","#","#"], # 13
          ["#","#","#","#","#","#","#","#","o","#","#","#","#","#","#","o","o","o","#","#","#","#","#","#","#","#"], # 14
          ["#","#","#","#","#","#","#","t","e","o","o","#","#","#","#","o","#","o","t","#","#","#","#","#","#","#"], # 15
          ["#","#","#","#","#","#","#","#","#","#","o","#","#","#","#","l","#","#","#","#","#","#","#","#","#","#"], # 16
          ["#","#","#","#","#","#","#","#","#","#","o","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"], # 17
          ["#","#","#","#","#","#","#","#","#","o","o","o","o","o","#","#","o","#","#","#","#","#","#","#","#","#"], # 18
          ["#","#","#","#","#","#","o","o","o","m","#","#","#","o","#","#","o","#","o","#","#","#","#","#","#","#"], # 19
          ["#","#","#","#","#","#","o","#","#","#","#","#","#","c","o","o","e","o","m","o","e","#","#","#","#","#"], # 20
          ["#","#","#","#","#","#","o","#","#","#","#","#","#","o","#","#","#","#","o","#","#","#","#","#","#","#"], # 21
          ["#","#","#","#","#","r","o","#","#","#","#","#","#","t","#","#","#","#","p","#","#","#","#","#","#","#"], # 22
          ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"], # 23
          ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"], # 24
          ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]  # 25
          ]

          # Key
          # "#" - wall
          # "o" - hallway
          # "e" - enemy
          # "c" - campfire
          # "m" - miniboss
          # "a" - chain armor
          # "p" - plate armor
          # "t" - small treasure
          # "r" - big treasure
          # "w" - longsword
          # "l" - magical longsword
          # "x" - boss


class PlayerCharacter:
    def __init__(self, name: str, weapon):
        self.name = name
        self.health = 20
        self.maxHealth = 20
        self.attackBonus = 5
        self.weapon = weapon
        self.weaponName = "Shortsword"
        self.armorName = "Leather Breastplate"
        self.armorClass = 14
        self.xp = 0
        self.curPos = [0,1]
        self.lastPos = [0,0]
        self.treasure = 0
        self.moveOptions = [False,False,False,False] # North, East, South, West
        self.level = 1

    def attackDamage(self):
        return self.weapon.getDamage()

class RegularEnemy:
    def __init__(self):
        randName = random.choice(["Goblin", "Orc", "Giant Rat", "Zombie", "Mummy", "Skeleton"])
        self.name = randName
        self.health = 10
        self.attackBonus = 4
        self.armorClass = 12
        self.xpReward = 10
        self.loot = random.randint(10,20)

    @staticmethod
    def attackDamage():
        return random.randint(2, 4)


class MiniBoss:
    def __init__(self):
        randName = random.choice(["Goblin Boss", "Giant Spider", "Giant Skeleton", "Wizard"])
        self.name = randName
        self.health = 15
        self.attackBonus = 5
        self.armorClass = 14
        self.xpReward = 20
        self.loot = random.randint(20,30)

    @staticmethod
    def attackDamage():
        return random.randint(3, 5)

class Boss:
    def __init__(self):
        self.name = "Vol'qaroth the Fallen"
        self.health = 25
        self.attackBonus = 7
        self.armorClass = 18

    @staticmethod
    def attackDamage():
        return random.randint(5, 8)

class Weapon:
    def __init__(self, minDmg, maxDmg):
        self.minDmg = minDmg
        self.maxDmg = maxDmg
    def getDamage(self):
        return random.randint(self.minDmg, self.maxDmg)



def mainProgram():
    print("The dungeon lair of the mad lich Vol'qaroth stands before you. The empty passage winds into the distance, disappearing in the darkness and gloom.")

    while not isGameOver:

        print("Possible commands:")

        possibleMoves()
        if char.moveOptions[0]:
            print("Move", end=" ")
            print("North")
        if char.moveOptions[1]:
            print("Move", end=" ")
            print("East")
        if char.moveOptions[2]:
            print("Move", end=" ")
            print("South")
        if char.moveOptions[3]:
            print("Move", end=" ")
            print("West")
        if mapBase[char.curPos[0]][char.curPos[1]] == "c":
            print("Rest")

        unsplitAction = input("Please select a command:").lower().split()

        if len(unsplitAction) == 1:
            userAction = unsplitAction[0]
        elif len(unsplitAction) == 2:
            userAction = unsplitAction[0]
            moveDirection = unsplitAction[1]
        else:
            print("Invalid command, please try again.")
            continue

        # Do Actions
        if userAction == "move" and len(unsplitAction) == 2:
            move(moveDirection)
        elif userAction == "rest":
            rest()
        elif userAction == "stats":
            print("Stats:")
            print("Name: {0}".format(char.name))
            print("Level: {0}".format(char.level))
            print("Health: {0}/{1}".format(char.health, char.maxHealth))
            print("Weapon: {0}".format(char.weaponName))
            print("Armor: {0}".format(char.armorName))
        else:
            print("Invalid command, please try again.")
            continue

        if mapBase[char.curPos[0]][char.curPos[1]] == ("e" or "m" or "x"):
            combat()
            mapBase[char.curPos[0]][char.curPos[1]] = "o"
        elif mapBase[char.curPos[0]][char.curPos[1]] == "t":
            print("A treasure chest lies before you, filled with gold coins and gems!")
            oldTreasure = char.treasure
            char.treasure += random.randint(50, 60)
            print("Treasure: {0} -> {1}".format(oldTreasure, char.treasure))
            mapBase[char.curPos[0]][char.curPos[1]] = "o"
        elif mapBase[char.curPos[0]][char.curPos[1]] == "r":
            print("You find a massive pile of treasure, golden crowns and diamonds, ruby necklaces and emerald rings, a true hoard.")
            oldTreasure = char.treasure
            char.treasure += random.randint(80, 90)
            print("Treasure: {0} -> {1}".format(oldTreasure, char.treasure))
            mapBase[char.curPos[0]][char.curPos[1]] = "o"
        elif mapBase[char.curPos[0]][char.curPos[1]] == "a":
            print("A skeleton lies on the floor, a hero of eras past. It still wears a set of chainmail.")
            if char.armorName != "Plate":
                char.armorName = "Chainmail"
                char.armorClass = 16
                print("Chainmail acquired!")
            else:
                print("You stuff it in your pack, your plate is far superior.")
                oldTreasure = char.treasure
                char.treasure += 40
                print("Chainmail acquired!")
                print("Treasure: {0} -> {1}".format(oldTreasure, char.treasure))
            mapBase[char.curPos[0]][char.curPos[1]] = "o"
        elif mapBase[char.curPos[0]][char.curPos[1]] == "p":
            print("A set of shining plate armor stands in an alcove. Just sitting there. You uneasily put it on and discover it is exactly your size.")
            if char.armorName == "Chainmail":
                oldTreasure = char.treasure
                char.treasure += 40
                print("At least your chainmail will sell for some good money back in town.")
                print("Treasure: {0} -> {1}".format(oldTreasure, char.treasure))
            char.armorName = "Plate"
            char.armorClass = 18
            print("Plate armor acquired!")
            mapBase[char.curPos[0]][char.curPos[1]] = "o"
        elif mapBase[char.curPos[0]][char.curPos[1]] == "w":
            print("A longsword leans against the wall. It seems in good condition.")
            if char.weapon != magicalLongsword:
                char.weapon = longsword
                char.weaponName = "Longsword"
                print("Longsword acquired!")
            else:
                oldTreasure = char.treasure
                char.treasure += 20
                print("At least it will sell for some nice coin in town.")
                print("Treasure: {0} -> {1}".format(oldTreasure, char.treasure))
            mapBase[char.curPos[0]][char.curPos[1]] = "o"
        elif mapBase[char.curPos[0]][char.curPos[1]] == "l":
            print("A statue stands in the alcove, a glittering sword held in its hands.")
            char.weapon = magicalLongsword
            char.weaponName = "Magical Longsword"
            if char.weapon == longsword:
                oldTreasure = char.treasure
                char.treasure += 20
                print("Your longsword will sell for some nice coin in town.")
                print("Treasure: {0} -> {1}".format(oldTreasure, char.treasure))
            print("Magical longsword acquired!")
            mapBase[char.curPos[0]][char.curPos[1]] = "o"
        elif mapBase[char.curPos[0]][char.curPos[1]] == "o":
            moveFlavor = ["The torches flicker with a breathless whisper, as though the walls themselves are exhaling.",
                         "Your footsteps echo too long, as if the corridor resents your presence.",
                         "Cracked stone underfoot hints at a battle long forgotten.",
                         "A distant drip reverberates through the gloom, steady as a heartbeat.",
                         "The air turns damp and metallic, clinging to your skin like a warning.",
                         "Whispers brush your ears, but turn to silence when you try to listen.",
                         "Moss creeps between ancient carvings, half erased by time and decay.",
                         "The scent of old blood and burnt incense seeps from the stone.",
                         "You pass beneath a crumbling arch etched with symbols too worn to read.",
                         "A faint breeze brushes your cheek, though the air is still.",
                         "Bones crunch faintly beneath your boot, brittle as dry leaves.",
                         "Something skitters just out of sight, claws tapping stone.",
                         "The walls lean in slightly, like they’re listening.",
                         "You feel watched, though you’re alone... or so you hope."]
            print(random.choice(moveFlavor))

def addXP(experience: int):
    char.xp += experience
    if 40 <= char.xp < 80 and char.level != 2:
        print("{0} levels up to 2!".format(char.name))
        oldHealth = char.health
        char.health += 5
        oldMaxHealth = char.maxHealth
        char.maxHealth += 5
        print("Health: {0}/{1} -> {2}/{3}".format(oldHealth, oldMaxHealth, char.health, char.maxHealth))
        char.attackBonus += 1
    elif 80 <= char.xp < 140 and char.level != 3:
        print("{0} levels up to 3!".format(char.name))
        oldHealth = char.health
        char.health += 5
        oldMaxHealth = char.maxHealth
        char.maxHealth += 5
        print("Health: {0}/{1} -> {2}/{3}".format(oldHealth, oldMaxHealth, char.health, char.maxHealth))
        char.attackBonus += 1
    elif 140 <= char.xp < 200 and char.level != 4:
        print("{0} levels up to 4!".format(char.name))
        oldHealth = char.health
        char.health += 5
        oldMaxHealth = char.maxHealth
        char.maxHealth += 5
        print("Health: {0}/{1} -> {2}/{3}".format(oldHealth, oldMaxHealth, char.health, char.maxHealth))
        char.attackBonus += 1
    elif 200 <= char.xp and char.level != 5:
        print("{0} levels up to 5!".format(char.name))
        oldHealth = char.health
        char.health += 5
        oldMaxHealth = char.maxHealth
        char.maxHealth += 5
        print("Health: {0}/{1} -> {2}/{3}".format(oldHealth,oldMaxHealth,char.health,char.maxHealth))
        char.attackBonus += 1




def combat():
    if mapBase[char.curPos[0]][char.curPos[1]] == "e":
        enemy = RegularEnemy()
    elif mapBase[char.curPos[0]][char.curPos[1]] == "m":
        enemy = MiniBoss()
    elif mapBase[char.curPos[0]][char.curPos[1]] == "x":
        enemy = Boss()


    global isGameOver
    isEnemyDead = False

    while not isEnemyDead:
        print("Possible commands:")
        print("Attack")
        print("Run")
        print("Stats")
        combatAction = input("Please select a command:").lower()
        # Player Turn
        if combatAction == "attack":
            if random.randint(1,20) + char.attackBonus >= enemy.armorClass:
                enemy.health -= char.attackDamage()
                if enemy.health <= 0:
                    isEnemyDead = True
                    addXP(enemy.xpReward)
                    char.treasure += enemy.loot
                    continue
            else:
                pass # MISS
        elif combatAction == "run":
            char.curPos[0] = char.lastPos[0]
            char.curPos[1] = char.lastPos[1]
            if random.randint(1, 20) + enemy.attackBonus >= char.armorClass:
                char.health -= enemy.attackDamage()
                if char.health <= 0:
                    # ADD GAME OVER MESSAGE
                    isGameOver = True
                    break
        elif combatAction == "stats":
            print("Stats:")
            print("Name: {0}".format(char.name))
            print("Level: {0}".format(char.level))
            print("Health: {0}/{1}".format(char.health, char.maxHealth))
            print("Weapon: {0}".format(char.weaponName))
            print("Armor: {0}".format(char.armorName))
        else:
            print("Invalid command, please try again.")
            continue
        # Enemy Turn
        if random.randint(1,20) + enemy.attackBonus >= char.armorClass:
            char.health -= enemy.attackDamage()
            if char.health <= 0:
                # ADD GAME OVER MESSAGE
                isGameOver = True
                break
    if enemy.name == "Vol'qaro the Fallen":
        pass # END GAME


def rest():
    oldHealth = char.health
    char.health = char.maxHealth
    print("{0} takes a nice rest at the campfire.".format(char.name))
    print("Health: {0}/{1} -> {2}/{1}".format(oldHealth,char.maxHealth,char.health))

def move(direction):
    if direction == "north" and char.moveOptions[0]:
        char.lastPos[0] = char.curPos[0]
        char.lastPos[1] = char.curPos[1]
        char.curPos[0] = char.curPos[0] - 1
    elif direction == "east" and char.moveOptions[1]:
        char.lastPos[0] = char.curPos[0]
        char.lastPos[1] = char.curPos[1]
        char.curPos[1] = char.curPos[1] + 1
    elif direction == "south" and char.moveOptions[2]:
        char.lastPos[0] = char.curPos[0]
        char.lastPos[1] = char.curPos[1]
        char.curPos[0] = char.curPos[0] + 1
    elif direction == "west" and char.moveOptions[3]:
        char.lastPos[0] = char.curPos[0]
        char.lastPos[1] = char.curPos[1]
        char.curPos[1] = char.curPos[1] - 1
    else:
        print("That is not a valid direction")

    # print("Current position is: {0}".format(char.curPos))

def possibleMoves():
    if char.curPos[0] != 0:
        if mapBase[char.curPos[0]-1][char.curPos[1]] != "#":
            north = True
        else:
            north = False
    else:
        north = False

    if char.curPos[0] != 25:
        if mapBase[char.curPos[0]+1][char.curPos[1]] != "#":
            south = True
        else:
            south = False
    else:
        south = False

    if char.curPos[1] != 25:
        if mapBase[char.curPos[0]][char.curPos[1]+1] != "#":
            east = True
        else:
            east = False
    else:
        east = False

    if char.curPos[1] != 0:
        if mapBase[char.curPos[0]][char.curPos[1]-1] != "#":
            west = True
        else:
            west = False
    else:
        west = False

    char.moveOptions = [north, east, south, west]




if __name__ == "__main__":
    shortsword = Weapon(4, 6)
    longsword = Weapon(5, 7)
    magicalLongsword = Weapon(6, 8)
    char = PlayerCharacter(input("Please enter a name for your character:"),shortsword)


    mainProgram()
