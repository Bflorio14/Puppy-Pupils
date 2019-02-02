# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define teacher = Character("Mrs. C")

init python:
    class Dog(object):
        name = ""
        isFemale = None
        agility = 0
        obedience = 0
        intelligence = 0

        def __init__(self, name, gender, agility, obedience, intelligence):
            self.name = name
            self.isFemale = gender
            self.agility = agility
            self.obedience = obedience
            self.intelligence = intelligence

    def make_dog(name, gender, agility, obedience, intelligence):
        dog = Dog(name, gender, agility, obedience, intelligence)
        return dog

    akita = make_dog("Jun", False, 2, 1, 3)
    beagle = make_dog("Mehira", True, 3, 2, 1)
    lab = make_dog("Kanchi", True, 1, 3, 2)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    # Test begins here
    define pov = Character("[povname]")

    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
            povname = "Jesse"

    menu:
        "What is your gender?"

        "Male":
            $ tempgen = False

        "Female":
            $ tempgen = True

    python:
        povObj = make_dog(povname, tempgen, 0, 0, 0)
        if tempgen == False:
            povgender = "Male"
        else:
            povgender = "Female"
        pov("My name is "+povObj.name + ", and my gender is "+ povgender)

    menu:
        "When learning a new skill, you:"

        "Understand it almost immediately and do not need further practice":
            $ povObj.intelligence += 6
        "Feel comfortable enough with the skill after practicing a couple more times":
            $ povObj.intelligence += 4
        "Need to repeat and practice a bunch more times for it to stick":
            $ povObj.intelligence += 2

    menu:
        "If you are given a difficult task to complete, you:"

        "Like a challenge, and complete it wholeheartedly!":
            $ povObj.obedience += 3

        "Force yourself to overcome the difficulties at hand.":
            $ povObj.obedience += 2

        "Get frustrated, and come back to it at a later time":
            $ povObj.obedience += 1

    menu:
        "Would you consider yourself to be accident prone?"

        "More than the average person":
            $ povObj.agility += 2

        "As much as the average person":
            $ povObj.agility += 4

        "Less than the average person":
            $ povObj.agility += 6

    menu:
        "What grades do/did you generally recieve in a passing course?"

        "Mostly A's (100-85)":
            $ povObj.intelligence += 3

        "Mostly B's (84-75)":
            $ povObj.intelligence += 2

        "Mostly C's (74-65)":
            $ povObj.intelligence += 1

    menu:
        "Out of these three sports, which would you prefer to partake in?"

        "Track/Cross Country":
            $ povObj.agility += 3

        "Basketball":
            $ povObj.agility += 2

        "Sleepathon":
            $ povObj.agility += 1

    menu:
        "When told by a superior to complete a task, you traditionally:"

        "Get started and finish as quickly as possible!":
            $ povObj.obedience += 6

        "Start and finish at your own pace":
            $ povObj.obedience += 4

        "Procrastinate until the last minute":
            $ povObj.obedience += 2

    $ pov("My test results are:\n Intelligence: "+str(povObj.intelligence)+"\nObedience: "+ str(povObj.obedience)+"\nAgility: "+str(povObj.agility))

    python:
        if povObj.intelligence > povObj.obedience and povObj.intelligence > povObj.agility:
            dogObj = lab
            dog = Character(lab.name)

        elif povObj.obedience > povObj.intelligence and povObj.obedience > povObj.agility:
            dogObj = akita
            dog = Character(akita.name)

        elif povObj.agility > povObj.intelligence and povObj.agility > povObj.obedience:
            dogObj = beagle
            dog = Character(beagle.name)

        elif povObj.intelligence == povObj.obedience and povObj.intelligence == povObj.agility:
            from random import randint
            randomVar = randint(1, 3)
            if randomVar == 1:
                dogObj = lab
                dog = Character(lab.name)
            if randomVar == 2:
                dogObj = beagle
                dog = Character(beagle.name)
            if randomVar == 3:
                dogObj = akita
                dog = Character(akita.name)
        elif povObj.intelligence == povObj.obedience or povObj.intelligence == povObj.agility:
            if povObj.intelligence > povObj.obedience:
                dogObj = beagle
                dog = Character(beagle.name)
            elif povObj.intelligence > povObj.agility:
                dogObj = lab
                dog = Character(dog.name)
            elif povObj.intelligence < povObj.obedience:
                dogObj = akita
                dog = Character(akita.name)
            else:
                dogObj = beagle
                dog = Character(beagle.name)
        else:
            if povObj.agility > povObj.intelligence:
                dogObj = akita
                dog = Character(akita.name)
            else:
                dogObj = lab
                dog = Character(lab.name)

    $ pov("My dog's name is " + dogObj.name)
    return
