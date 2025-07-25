"""
Mid-Term Project
Python 1
UCLA Extension
author: Taran Kalle

< Description of the program >

** be sure to RENAME the file <Last><First>_MidTermProject.py
** example: BeemerBill_MidTermProject.py
"""



import random

ISGAMEOVER = False
MAPBASE = [
          # 0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
    # 18  19  20  21  22  23  24  25
          ["#","o","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",
           "#","#","#","#","#","#","#","#"], # 0
          ["#","o","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",
           "#","#","#","#","#","#","#","#"], # 1
          ["#","o","#","#","#","#","#","a","#","#","#","#","#","#","#","#","#","#",
           "#","#","#","#","#","#","#","#"], # 2
          ["#","o","o","e","#","#","#","m","#","#","#","#","#","#","#","#","#","o",
           "o","r","#","#","#","#","#","#"], # 3
          ["#","#","#","o","#","#","#","o","#","#","#","#","o","r","#","#","#","e",
           "#","#","#","#","#","#","#","#"], # 4
          ["#","#","#","o","o","#","#","o","#","#","#","#","o","#","#","#","o","o",
           "#","#","#","#","#","#","#","#"], # 5
          ["#","#","#","#","c","o","o","o","#","#","#","o","o","#","#","#","o","#",
           "#","#","#","#","#","#","#","#"], # 6
          ["#","#","#","#","o","#","#","#","#","#","#","e","#","#","#","#","o","#",
           "#","o","o","o","x","#","#","#"], # 7
          ["#","#","#","o","o","#","#","#","#","#","#","o","#","#","#","#","o","o",
           "m","c","#","#","#","#","#","#"], # 8
          ["#","#","#","o","#","#","#","#","o","o","e","o","o","o","e","o","o","#",
           "#","#","#","#","#","#","#","#"], # 9
          ["#","#","#","e","w","#","#","#","e","#","#","#","#","#","o","#","#","#",
           "#","#","#","#","#","#","#","#"], # 10
          ["#","#","#","o","#","#","#","#","o","#","#","#","#","#","c","#","#","#",
           "#","#","#","#","#","#","#","#"], # 11
          ["#","#","#","o","#","#","o","o","o","#","#","#","#","#","o","#","#","#",
           "#","#","#","#","#","#","#","#"], # 12
          ["#","#","#","o","o","c","o","#","o","#","#","#","#","#","o","m","#","#",
           "#","#","#","#","#","#","#","#"], # 13
          ["#","#","#","#","#","#","#","#","o","#","#","#","#","#","#","o","o","o",
           "#","#","#","#","#","#","#","#"], # 14
          ["#","#","#","#","#","#","#","t","e","o","o","#","#","#","#","o","#","o",
           "t","#","#","#","#","#","#","#"], # 15
          ["#","#","#","#","#","#","#","#","#","#","o","#","#","#","#","l","#","#",
           "#","#","#","#","#","#","#","#"], # 16
          ["#","#","#","#","#","#","#","#","#","#","o","#","#","#","#","#","#","#",
           "#","#","#","#","#","#","#","#"], # 17
          ["#","#","#","#","#","#","#","#","#","o","o","o","o","o","#","#","o","#",
           "#","#","#","#","#","#","#","#"], # 18
          ["#","#","#","#","#","#","o","o","o","m","#","#","#","o","#","#","o","#",
           "o","#","#","#","#","#","#","#"], # 19
          ["#","#","#","#","#","#","o","#","#","#","#","#","#","c","o","o","e","o",
           "m","o","e","#","#","#","#","#"], # 20
          ["#","#","#","#","#","#","o","#","#","#","#","#","#","o","#","#","#","#",
           "o","#","#","#","#","#","#","#"], # 21
          ["#","#","#","#","#","r","o","#","#","#","#","#","#","t","#","#","#","#",
           "p","#","#","#","#","#","#","#"], # 22
          ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",
           "#","#","#","#","#","#","#","#"], # 23
          ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",
           "#","#","#","#","#","#","#","#"], # 24
          ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",
           "#","#","#","#","#","#","#","#"]  # 25
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
        self.curPos = [0,1] # 0,1
        self.lastPos = [0,0]
        self.treasure = 0
        self.moveOptions = [False,False,False,False] # North, East, South, West
        self.level = 1
        self.attackFlavor = [

                            ["You swing your blade in a clean arc, the steel "
                            "singing through the air.","The edge bites true, "
                            "cutting a sharp line through flesh and armor.",
                            "The blade slices only air as your target slips just "
                            "out of reach."]
                            ,

                            ["With a burst of speed, you lunge forward,"
                             " aiming your sword at a vital point.",
                             "The thrust lands solidly, driving steel deep with "
                             "satisfying resistance.",
                             "Your foe twists aside, and your blade skids "
                             "harmlessly past."]
                            ,

                            ["You twist into a tight slash, the edge of your weapon"
                             " flashing in the dim light.","The strike lands "
                             "cleanly, drawing a spray of blood across the stone.",
                             "You overextend, and the blade carves a scar into the "
                             "ground instead."]
                            ,

                            ["Gripping your sword with both hands, you bring it "
                             "down in a crushing overhead strike.",
                             "The blow crashes down with brutal force, "
                             "staggering your opponent.",
                             "The strike slams into the floor, sending sparks and "
                             "stone flying."]
                            ,

                            ["You feint left, then step in and drive your blade "
                             "toward your foe’s guard.","The trick works. The blade"
                             " slips past their defense and strikes deep.",
                             "They don’t fall for it, parrying your thrust with "
                             "ease."]
                            ]

    def attackDamage(self):
        return self.weapon.getDamage()

class RegularEnemy:
    def __init__(self):
        randName = random.choice(["Goblin", "Orc", "Giant Rat", "Zombie", "Mummy",
                                  "Skeleton"])
        self.name = randName
        self.health = 10
        self.attackBonus = 4
        self.armorClass = 12
        self.xpReward = 10
        self.loot = random.randint(10,20)
        self.deathFlavor = ["The goblin lets out a final snarl before crumpling to "
                            "the floor, its dagger clattering beside it.",
                            "With a groan like splitting stone, the orc stumbles "
                            "back, then crashes to the ground in a heap of muscle "
                            "and fury spent.",
                            "The rat jerks once, then collapses with a sickening "
                            "squelch, its twitching limbs finally still.",
                            "The corpse slumps mid-lurch, limbs unraveling as "
                            "whatever foul magic held it together fades into the "
                            "dust.",
                            "The mummy stiffens, then collapses into a brittle"
                            " pile of cloth and bone, ancient curses fading with a "
                            "whisper.",
                            "The skeleton shudders, then its joints give way, "
                            "bones scattering across the stone floor like dry "
                            "leaves in wind."]
        self.attackFlavor = [
                            [
                                ["The goblin slashes wildly, cackling as its blade "
                                 "scrapes for flesh.","The blade grazes your arm, "
                                 "leaving a stinging cut.",
                                 "The swing whistles past as you duck beneath it."],
                                ["It darts in low, aiming a nasty jab at your ribs "
                                 "with surprising speed.","The dagger sinks into "
                                 "your side with a vicious grin.",
                                 "You twist just in time, and its blade "
                                 "strikes only air."],
                                ["With a hiss, it hurls a handful of dirt at your "
                                 "eyes before lunging in.","The distraction works; "
                                 "your vision blurs as its knife bites deep.",
                                 "You shield your eyes and sidestep the feint with "
                                 "ease."]
                            ],
                            [
                                ["The orc roars and swings its axe in a brutal arc "
                                 "meant to cleave.","The axe crashes into your "
                                 "shoulder, knocking you back a step.",
                                 "The heavy swing slams into the wall beside "
                                 "you, spraying stone chips."],
                                ["It charges forward, trying to batter you with "
                                 "sheer force and fury.","You’re slammed against "
                                 "the wall, breath driven from your lungs.",
                                 "You roll aside, and the orc stumbles past with a "
                                 "snarl."],
                                ["The orc feints left, then smashes its fist toward"
                                 " your jaw.","Its knuckles crack against your face"
                                 " with bone-rattling force.",
                                 "You duck under the punch and feel the wind of its"
                                 " fury rush by."]
                            ],
                            [
                                ["The rat lunges, yellowed teeth snapping at your "
                                 "ankle.","Its teeth tear into flesh, and warm "
                                 "blood follows.","You kick it away mid-leap, "
                                 "sending it tumbling."],
                                ["It scurries beneath your guard, trying to bite "
                                 "and claw in a frenzy.","You feel sharp claws rake"
                                 " across your shin.",
                                 "You hop back just in time, its claws scraping the "
                                 "stone."],
                                ["A hiss, a blur of fur, and suddenly it’s clawing "
                                 "up your leg.","It bites deep into your thigh "
                                 "before dropping away.","You shake it off "
                                 "before it can latch on."]
                            ],
                            [
                                ["The zombie swings a rotten arm with clumsy, "
                                 "relentless force.","Its arm slams into your chest"
                                 " with bruising weight.",
                                 "It stumbles past, groaning in frustration."],
                                ["It lurches forward, gnashing teeth aimed at your "
                                 "throat.","Rotten jaws clamp down painfully on "
                                 "your shoulder.",
                                 "You shove its face away just in time, "
                                 "the teeth snapping shut inches from your skin."],
                                ["Slime drips from its grasp as it reaches out to "
                                 "pull you closer.","Its grip tightens around your "
                                 "wrist, dragging you toward decay.",
                                 "You slip free, and it groans as you break contact."]
                            ],
                            [
                                ["Dry hands strike with surprising strength, "
                                 "wrapped fingers aiming to choke.","The grip "
                                 "tightens around your throat, cutting off "
                                 "breath for a heartbeat.",
                                 "You twist free before its grasp can close."],
                                ["The mummy exhales a cursed breath as it lashes "
                                 "out with brittle rage.","A wave of decay strikes "
                                 "your chest, numbing your limbs.",
                                 "You hold your breath and sidestep the "
                                 "blow just in time."],
                                ["It swings an ancient scepter with slow, terrible "
                                 "purpose.","The scepter cracks against your ribs "
                                 "with dreadful weight.","It thuds harmlessly "
                                 "against your shield with a puff of dust."]
                            ],
                            [
                                ["The skeleton lashes out with its blade, "
                                 "bones clacking with each movement.",
                                 "The blade slices a clean line across your "
                                 "forearm.","You parry the strike, and sparks leap "
                                 "from your weapon."],
                                ["It spins suddenly, aiming a strike with inhuman "
                                 "precision.","The tip pierces your side, "
                                 "cold steel kissing bone.",
                                 "You stagger back just in time, and the blade "
                                 "misses by inches."],
                                ["With a hiss of grinding joints, it jabs its "
                                 "weapon toward your chest.","The jab connects, "
                                 "driving the breath from your lungs.",
                                 "You sidestep the thrust, and the skeleton "
                                 "clatters forward, off balance."]
                            ]
                            ]

        # [Enemy][Attack][Hit/Miss]
        # 0 - Goblin, 1 - Orc, 2 - Giant Rat, 3 - Zombie, 4 - Mummy, 5 - Skeleton
        # 0 - Attack, 1 - Hit, 2 - Miss

    @staticmethod
    def attackDamage():
        return random.randint(2, 4)


class MiniBoss:
    def __init__(self):
        randName = random.choice(["Goblin Boss", "Giant Spider", "Giant Skeleton",
                                  "Wizard"])
        self.name = randName
        self.health = 15
        self.attackBonus = 5
        self.armorClass = 14
        self.xpReward = 20
        self.loot = random.randint(20,30)
        self.deathFlavor = ["The Goblin Boss glares with sudden fear, clutching at "
                            "a fresh wound before collapsing with a choked growl, "
                            "ambition leaking into the dirt.",
                            "The spider convulses violently, legs curling inward"
                            " as its body collapses with a wet thud and the "
                            "chittering finally stops.",
                            "Cracks spread through the giant skeleton’s frame "
                            "before it topples, bones splintering on the stone "
                            "floor like brittle timber.",
                            "The wizard gasps, arcane light flickering in his eyes "
                            "one final time before he collapses, robes pooling "
                            "around a body gone limp and cold."]
        self.attackFlavor = [
                            [
                                ["The Goblin Boss bellows and swings a jagged "
                                 "cleaver in a brutal arc.","The cleaver bites "
                                 "deep, leaving a ragged, bleeding wound.",
                                 "You duck under the swing as it crashes into "
                                 "the wall, sparks flying."],
                                ["He feints with a dagger, then lunges low with "
                                 "uncanny speed.","The blade slashes across your "
                                 "thigh before you can retreat.",
                                 "You leap back, and the blade whistles harmlessly "
                                 "past."],
                                ["With a sneer, he hurls a flask of burning oil "
                                 "toward your chest.","The flask shatters on "
                                 "impact, igniting in a burst of searing flame.",
                                 "You dive aside, and fire scorches only the stone "
                                 "behind you."]
                            ],
                            [
                                ["The spider rears up and strikes with dripping "
                                 "fangs aimed at your neck.",
                                 "Its fangs pierce your skin, venom burning like "
                                 "fire.",
                                 "You dodge left, and the fangs snap shut inches "
                                 "from your face."],
                                ["It launches a glob of sticky webbing to pin your "
                                 "limbs.",
                                 "The web entangles your arms, slowing your "
                                 "movements dangerously.",
                                 "You roll clear, and the web splats harmlessly "
                                 "beside you."],
                                ["With eerie silence, it scuttles up the wall and "
                                 "drops toward you from above.",
                                 "The impact knocks you to the ground as its legs "
                                 "dig in.",
                                 "You leap away as it crashes down where you stood "
                                 "seconds ago."]
                            ],
                            [
                                ["The giant skeleton raises a rusted greatsword and"
                                 " brings it down with terrifying force.",
                                 "The sword slams into you, rattling bone and armor"
                                 " alike.",
                                 "You sidestep, and the blade embeds itself deep in"
                                 " the stone floor."],
                                ["It sweeps its massive arm to crush everything in"
                                 " its path.",
                                 "The blow flings you back, pain flaring through"
                                 " your chest.",
                                 "You duck just in time, the wind of the swing "
                                 "whipping past you."],
                                ["It slams its shield forward like a wall of bone "
                                 "and iron.",
                                 "The impact cracks into your ribs and knocks the " 
                                 "breath from your lungs.",
                                 "You roll under the shield as it smashes into the "
                                 "wall with a boom."]
                            ],
                            [
                                ["The wizard chants an incantation, and a bolt of "
                                 "lightning arcs from his fingers.",
                                 "The bolt scorches across your body, muscles "
                                 "spasming from the shock.",
                                 "You dive aside as the lightning scorches a "
                                 "blackened scar into the ground."],
                                ["He thrusts his staff forward, conjuring a wave of"
                                 " force that barrels toward you.",
                                 "The blast sends you flying back, your ears "
                                 "ringing.",
                                 " You brace yourself and stand your ground as the "
                                 "wave rushes past."],
                                ["With a cruel smirk, he flicks a mote of fire that"
                                 " blossoms into a roaring flame.",
                                 "The fireball erupts on your chest, igniting your "
                                 "cloak and searing your skin.",
                                 "You duck behind cover just as the explosion"
                                 " roars overhead."]
                            ]
                            ]
        # [Enemy][Attack][Hit/Miss]
        # 0 - Goblin Boss, 1 - Giant Spider, 2 - Giant Skeleton, 3 - Wizard
        # 0 - Attack, 1 - Hit, 2 - Miss

    @staticmethod
    def attackDamage():
        return random.randint(3, 5)

class Boss:
    def __init__(self):
        self.name = "Vol'qaroth the Fallen"
        self.health = 25
        self.attackBonus = 7
        self.armorClass = 18
        self.loot = random.randint(50,60)
        self.attackFlavor = [[
                                ["Vol'qaroth raises his skeletal hand, "
                                 "and a torrent of shadow lances toward your heart.",
                                 "The darkness pierces you like ice, draining "
                                 "warmth and will alike.",
                                 "You hurl yourself aside, and the beam gouges a "
                                 "smoking trench in the floor."],
                                ["With a guttural incantation, he summons a swarm "
                                 "of spectral hands clawing from the ground.",
                                 "The ghostly claws seize your limbs, raking "
                                 "through flesh and spirit alike.",
                                 "You leap free just before the hands can close "
                                 "around your ankles."],
                                ["He lifts his staff skyward, and the air bends as "
                                 "he calls down a ring of withering flame.",
                                 "The necrotic fire sears your skin and soul, "
                                 "leaving a mark that does not fade.",
                                 "You vault through a gap in the flames, singed"
                                 " but untouched."]
                            ]]

        # [Enemy][Attack][Hit/Miss]
        # 0 - Vol'qaroth
        # 0 - Attack, 1 - Hit, 2 - Miss

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
    print("The dungeon lair of the mad lich Vol'qaroth stands before you. "
          "The empty passage winds into the distance, disappearing in the darkness "
          "and gloom.")

    while not ISGAMEOVER:

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
        if MAPBASE[char.curPos[0]][char.curPos[1]] == "c":
            print("Rest")
        print("Quit")
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
        elif userAction == "quit":
            break
        else:
            print("Invalid command, please try again.")
            continue

        if (MAPBASE[char.curPos[0]][char.curPos[1]] == "e"
                or MAPBASE[char.curPos[0]][char.curPos[1]] == "m" or
                MAPBASE[char.curPos[0]][char.curPos[1]] == "x"):
            combat()
            MAPBASE[char.curPos[0]][char.curPos[1]] = "o"
        elif MAPBASE[char.curPos[0]][char.curPos[1]] == "t":
            print("A treasure chest lies before you, filled with gold "
                  "coins and gems!")
            oldTreasure = char.treasure
            char.treasure += random.randint(50, 60)
            print("Treasure: {0} -> {1}".format(oldTreasure, char.treasure))
            MAPBASE[char.curPos[0]][char.curPos[1]] = "o"
        elif MAPBASE[char.curPos[0]][char.curPos[1]] == "r":
            print("You find a massive pile of treasure, golden crowns and diamonds, "
                  "ruby necklaces and emerald rings, a true hoard.")
            oldTreasure = char.treasure
            char.treasure += random.randint(80, 90)
            print("Treasure: {0} -> {1}".format(oldTreasure, char.treasure))
            MAPBASE[char.curPos[0]][char.curPos[1]] = "o"
        elif MAPBASE[char.curPos[0]][char.curPos[1]] == "a":
            print("A skeleton lies on the floor, a hero of eras past. "
                  "It still wears a set of chainmail.")
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
            MAPBASE[char.curPos[0]][char.curPos[1]] = "o"
        elif MAPBASE[char.curPos[0]][char.curPos[1]] == "p":
            print("A set of shining plate armor stands in an alcove. Just "
                  "sitting there. You uneasily put it on and discover it "
                  "is exactly your size.")
            if char.armorName == "Chainmail":
                oldTreasure = char.treasure
                char.treasure += 40
                print("At least your chainmail will sell for some good money back "
                      "in town.")
                print("Treasure: {0} -> {1}".format(oldTreasure, char.treasure))
            char.armorName = "Plate"
            char.armorClass = 18
            print("Plate armor acquired!")
            MAPBASE[char.curPos[0]][char.curPos[1]] = "o"
        elif MAPBASE[char.curPos[0]][char.curPos[1]] == "w":
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
            MAPBASE[char.curPos[0]][char.curPos[1]] = "o"
        elif MAPBASE[char.curPos[0]][char.curPos[1]] == "l":
            print("A statue stands in the alcove, a "
                  "glittering sword held in its hands.")
            char.weapon = magicalLongsword
            char.weaponName = "Magical Longsword"
            if char.weapon == longsword:
                oldTreasure = char.treasure
                char.treasure += 20
                print("Your longsword will sell for some nice coin in town.")
                print("Treasure: {0} -> {1}".format(oldTreasure, char.treasure))
            print("Magical longsword acquired!")
            MAPBASE[char.curPos[0]][char.curPos[1]] = "o"
        elif MAPBASE[char.curPos[0]][char.curPos[1]] == "o":
            moveFlavor = ["The torches flicker with a breathless whisper, "
                          "as though the walls themselves are exhaling.",
                         "Your footsteps echo too long, as if the corridor "
                         "resents your presence.",
                         "Cracked stone underfoot hints at a battle long forgotten.",
                         "A distant drip reverberates through the gloom, "
                         "steady as a heartbeat.",
                         "The air turns damp and metallic, clinging to your "
                         "skin like a warning.",
                         "Whispers brush your ears, but turn to silence when "
                         "you try to listen.",
                         "Moss creeps between ancient carvings, half erased "
                         "by time and decay.",
                         "The scent of old blood and burnt incense seeps "
                         "from the stone.",
                         "You pass beneath a crumbling arch etched with "
                         "symbols too worn to read.",
                         "A faint breeze brushes your cheek, though "
                         "the air is still.",
                         "Bones crunch faintly beneath your boot, "
                         "brittle as dry leaves.",
                         "Something skitters just out of sight, "
                         "claws tapping stone.",
                         "The walls lean in slightly, like they’re listening.",
                         "You feel watched, though you’re alone... or so you hope."]
            print(random.choice(moveFlavor))
        elif MAPBASE[char.curPos[0]][char.curPos[1]] == "c":
            print("A good place to make camp. Maybe time for a rest.")


def addXP(experience: int):
    char.xp += experience
    if 40 <= char.xp < 80 and char.level != 2:
        print("{0} levels up to 2!".format(char.name))
        oldHealth = char.health
        char.health += 5
        oldMaxHealth = char.maxHealth
        char.maxHealth += 5
        print("Health: {0}/{1} -> {2}/{3}".format(oldHealth, oldMaxHealth,
                                                  char.health, char.maxHealth))
        char.attackBonus += 1
        char.level = 2
    elif 80 <= char.xp < 140 and char.level != 3:
        print("{0} levels up to 3!".format(char.name))
        oldHealth = char.health
        char.health += 5
        oldMaxHealth = char.maxHealth
        char.maxHealth += 5
        print("Health: {0}/{1} -> {2}/{3}".format(oldHealth, oldMaxHealth,
                                                  char.health, char.maxHealth))
        char.attackBonus += 1
        char.level = 3
    elif 140 <= char.xp < 200 and char.level != 4:
        print("{0} levels up to 4!".format(char.name))
        oldHealth = char.health
        char.health += 5
        oldMaxHealth = char.maxHealth
        char.maxHealth += 5
        print("Health: {0}/{1} -> {2}/{3}".format(oldHealth, oldMaxHealth,
                                                  char.health, char.maxHealth))
        char.attackBonus += 1
        char.level = 4
    elif 200 <= char.xp and char.level != 5:
        print("{0} levels up to 5!".format(char.name))
        oldHealth = char.health
        char.health += 5
        oldMaxHealth = char.maxHealth
        char.maxHealth += 5
        print("Health: {0}/{1} -> {2}/{3}".format(oldHealth,oldMaxHealth,
                                                  char.health,char.maxHealth))
        char.attackBonus += 1
        char.level = 5



def combat():
    enemyFlavorIndex = 0
    if MAPBASE[char.curPos[0]][char.curPos[1]] == "e":
        enemy = RegularEnemy()
        if enemy.name == "Goblin":
            print("With a shriek and a flash of rusted steel, a goblin lunges from "
                  "the shadows, eyes gleaming with cruel mischief.")
            enemyFlavorIndex = 0
        elif enemy.name == "Orc":
            print("The ground trembles slightly as an orc rounds the corner, "
                  "muscles taut and tusked jaw clenched in anticipation of blood.")
            enemyFlavorIndex = 1
        elif enemy.name == "Giant Rat":
            print("The stench hits first. Then the wet scurrying. And suddenly a "
                  "rat the size of a dog bursts from a cracked wall.")
            enemyFlavorIndex = 2
        elif enemy.name == "Zombie":
            print("You hear the drag of flesh on stone before you see it—then a "
                  "corpse shambles into view, stitched together by stubborn hatred.")
            enemyFlavorIndex = 3
        elif enemy.name == "Mummy":
            print("Bandages flutter like dry leaves as the mummy emerges, "
                  "its ancient eyes smoldering with forgotten curses.")
            enemyFlavorIndex = 4
        elif enemy.name == "Skeleton":
            print("With a hollow rattle, a skeleton assembles itself from a heap of "
                  "bones, drawing a corroded blade with lifeless precision.")
            enemyFlavorIndex = 5
    elif MAPBASE[char.curPos[0]][char.curPos[1]] == "m":
        enemy = MiniBoss()
        if enemy.name == "Goblin Boss":
            print("From the shadows steps a hulking goblin clad in mismatched "
                  "armor, eyes gleaming with malice as he thumps a notched cleaver "
                  "against his shield.")
            enemyFlavorIndex = 0
        elif enemy.name == "Giant Spider":
            print("The webbed ceiling shudders, then tears, spilling down a "
                  "massive, chittering spider, its eyes glistening like obsidian "
                  "beads as venom drips from its fangs.")
            enemyFlavorIndex =  1
        elif enemy.name == "Giant Skeleton":
            print("The chamber trembles as bones rise from the earth, assembling "
                  "with unnatural speed into a towering warrior of death. Its jaw "
                  "unhinges in a soundless roar as it lifts a blade larger than a "
                  "man.")
            enemyFlavorIndex = 2
        elif enemy.name == "Wizard":
            print("A gust of arcane wind howls through the hall as a robed figure "
                  "floats into view, eyes aglow with bitter wisdom and wrath. His "
                  "fingers trace runes in the air that burn with power.")
            enemyFlavorIndex = 3
    elif MAPBASE[char.curPos[0]][char.curPos[1]] == "x":
        enemy = Boss()
        print("The air grows deathly still as the chamber darkens, torches "
              "extinguishing one by one. Atop a blackened dais, a cloaked figure "
              "rises from a throne of bone and ruin, his skull crowned with a halo "
              "of sickly green flame.\n'I was king when your gods were dust,"
              "' Vol'qaroth intones, his voice echoing from everywhere and "
              "nowhere.\n'Come, let oblivion remember your name… if it must.'")
        enemyFlavorIndex = 0

    global ISGAMEOVER
    isEnemyDead = False

    while not isEnemyDead:
        print("Possible commands:")
        print("Attack")
        print("Run")
        print("Stats")
        combatAction = input("Please select a command:").lower()
        # Player Turn
        if combatAction == "attack":
            charAttackType = random.randint(0,4)
            print(char.attackFlavor[charAttackType][0])
            if random.randint(1,20) + char.attackBonus >= enemy.armorClass:
                print(char.attackFlavor[charAttackType][1])
                enemy.health -= char.attackDamage()
                if enemy.health <= 0:
                    if enemy.name == "Vol'qaroth the Fallen":
                        isEnemyDead = True
                        ISGAMEOVER = True
                        oldTreasure = char.treasure
                        char.treasure += enemy.loot
                        print("As his phylactery shatters and his form begins to "
                              "unravel, Vol'qaroth’s voice fades into a raspy "
                              "whisper:\n'You delay the inevitable. I am the echo "
                              "that eternity does not forget...'")
                        print("Treasure: {0} -> {1}".format(oldTreasure,
                                                            char.treasure))
                        print("\n\n\n")
                        print("--------------------")
                        print("You win!")
                        print("Treasure: {0}".format(char.treasure))
                        print("--------------------")
                        continue
                    else:
                        print(enemy.deathFlavor)
                    isEnemyDead = True
                    addXP(enemy.xpReward)
                    oldTreasure = char.treasure
                    char.treasure += enemy.loot
                    print("Treasure: {0} -> {1}".format(oldTreasure,
                                                        char.treasure))
                    continue
            else:
                print(char.attackFlavor[charAttackType][2])
        elif combatAction == "run":
            char.curPos[0] = char.lastPos[0]
            char.curPos[1] = char.lastPos[1]
            print("One last strike comes at you.")
            enemyAttackType = random.randint(0, 2)
            print(enemy.attackFlavor[enemyFlavorIndex][enemyAttackType][0])
            if random.randint(1, 20) + enemy.attackBonus >= char.armorClass:
                oldHealth = char.health
                char.health -= enemy.attackDamage()
                print(enemy.attackFlavor[enemyFlavorIndex][enemyAttackType][1])
                print("Health: {0}/{1} -> {2}/{1}".format(oldHealth,
                                                          char.maxHealth,
                                                          char.health))
                if char.health <= 0:
                    if enemy.name != "Vol'qaroth the Fallen":
                        print("Despite their prowess, {0} falls in "
                              "battle to a {1}".format(char.name, enemy.name))
                    else:
                        print("The evil lich Vol'qaroth the Fallen claims another "
                              "victim!")
                    print("--------------------")
                    print("You lose!")
                    print("--------------------")
                    ISGAMEOVER = True
                    break
            else:
                print(enemy.attackFlavor[enemyFlavorIndex][enemyAttackType][2])
            print("You manage to get away!")
            break
        elif combatAction == "stats":
            print("Stats:")
            print("Name: {0}".format(char.name))
            print("Level: {0}".format(char.level))
            print("Health: {0}/{1}".format(char.health, char.maxHealth))
            print("Weapon: {0}".format(char.weaponName))
            print("Armor: {0}".format(char.armorName))
        elif combatAction == "quit":
            ISGAMEOVER = True
            break
        else:
            print("Invalid command, please try again.")
            continue
        # Enemy Turn

        enemyAttackType = random.randint(0,2)
        print(enemy.attackFlavor[enemyFlavorIndex][enemyAttackType][0])

        if random.randint(1,20) + enemy.attackBonus >= char.armorClass:
            oldHealth = char.health
            char.health -= enemy.attackDamage()
            print(enemy.attackFlavor[enemyFlavorIndex][enemyAttackType][1])
            print("Health: {0}/{1} -> {2}/{1}".format(oldHealth,
                                                      char.maxHealth,char.health))
            if char.health <= 0:
                if enemy.name != "Vol'qaroth the Fallen":
                    print("Despite their prowess, {0} falls in "
                          "battle to a {1}".format(char.name,enemy.name))
                else:
                    print("The evil lich Vol'qaroth the Fallen claims another "
                          "victim!")
                print("--------------------")
                print("You lose!")
                print("--------------------")
                ISGAMEOVER = True
                break
        else:
            print(enemy.attackFlavor[enemyFlavorIndex][enemyAttackType][2])



def rest():
    oldHealth = char.health
    char.health = char.maxHealth
    print("You takes a nice rest at the campfire.")
    print("Health: {0}/{1} -> {2}/{1}".format(oldHealth,
                                              char.maxHealth,char.health))

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
        if MAPBASE[char.curPos[0]-1][char.curPos[1]] != "#":
            north = True
        else:
            north = False
    else:
        north = False

    if char.curPos[0] != 25:
        if MAPBASE[char.curPos[0]+1][char.curPos[1]] != "#":
            south = True
        else:
            south = False
    else:
        south = False

    if char.curPos[1] != 25:
        if MAPBASE[char.curPos[0]][char.curPos[1]+1] != "#":
            east = True
        else:
            east = False
    else:
        east = False

    if char.curPos[1] != 0:
        if MAPBASE[char.curPos[0]][char.curPos[1]-1] != "#":
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
    char = PlayerCharacter(input("Please enter a name for your character:"),
                           shortsword)
    mainProgram()
