# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define teacher = Character("Mrs. C")
define narrator = Character(" ")
define m = Character("Madigan")
define temp = Character("???")

init python:
    training = None
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

    #makes dog object
    def make_dog(name, gender, agility, obedience, intelligence):
        dog = Dog(name, gender, agility, obedience, intelligence)
        return dog

    akita = make_dog("Jun", False, 2, 3, 1)
    beagle = make_dog("Mehira", True, 3, 1, 2)
    lab = make_dog("Kanchi", True, 1, 2, 3)

    #returns if the dog can successfully complete training
    def canPass(stat, compStat):
        return compStat > stat

    import dialogue

    # returns the label of where the dialogue is located
    def passDialogue(stat, compStat):
        if canPass(stat, compStat):
            if training == "o":
                dialogue.o_good(narrator, stat)
            elif training == "i":
                dialogue.i_good(narrator, stat)
            elif training == "a":
                dialogue.a_good(narrator, stat)
            else:
                narrator("Error: No Choice Selected")
            return True
        else:
            if training == "o":
                dialogue.o_bad(narrator, stat)
            elif training == "i":
                dialogue.i_bad(narrator, stat)
            elif training == "a":
                dialogue.a_bad(narrator, stat)
            else:
                narrator("Error: No Choice Selected")
            return False

## renpy.set_return_stack(

# The game starts here.

label start:
    stop music fadeout 1.0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    "Today is the day."

    "You pick at your fingernails haphazardly while your car is stopped."

    "To say your nervous is an understatement of the century."

    "After almost a year of waiting (8 months, 2 weeks and 4 days to be exact, but who's counting?) you were finally called by the local Guide Dog Training School."

    "You remember how excited you were to receive that phone call, and how hard it was to keep your cool."

    "Right now, you're on your way to the training school to take an examination."

    "As you pull up to the school, all of your emotions being to heighten."

    "Nervous? Excited? Terrified? Why pick one?"

    "You almost forgot to grab your backpack as you hastily, and almost clumsily, stumble out of your car door."

    "You quickly grab it, some pens fly out of it, and you rush into the school."

    "Without looking, you almost run someone over."

    m "OH! Oh no! I’m so sorry! I didn’t see you coming!"

    temp "It’s definitely my bad! I’m so sorry! I was so excited for the exam, I just was gunning for it!"

    temp "(I need to be more careful!)"

    temp "Are you hurt?"

    m "No, no! Not at all! You caught me off guard is all!"

    temp "(I’m so lucky I didn’t hurt anyone. I shouldn’t of ran off like that. How unprofessional!)"

    m "What an ice breaker, am I right?"

    narrator "She looks down at her watch."

    m "Oh no! I’m going to be late!"

    m "I heard you say you’re taking an exam? Well if it’s the guide dog trainer examination, then I wouldn’t loose footing now!"

    narrator "You look down at your phone."

    narrator "She was right! It's 9:00am on the dot!"

    temp "Lets book it!"

    ## Change background to school

    narrator "You and your new friend book it into the school."

    narrator "Thankfully, there were signs posted around the building that helped you find the examination room quickly."

    narrator "On entering, there is a small woman standing in front of the room, with a desk full of neatly organized papers."

    narrator "She looks at you both."

    teacher "Would you two kindly please take your seats? I will discuss the examination once you all are settled."

    m "Y-yes! Of course!"

    narrator "You both fall into your seats, both slightly trembling from the crash of adrenaline and embarrassment."

    narrator "You take out your pencils from out of your backpack and wait patiently for the woman to start talking."

    teacher "Good morning everyone! My name is Mrs. Clawson, but you can call me Mrs. C for short!"

    teacher "You all are here today for a reason. There were a handful of applications that were selected from the large amount of submissions."

    teacher "These handful of applications stood out. Whether it was from their experiences, their skills, or their knowledge…"

    teacher "Their traits stood out the most."

    teacher "You are those handful of applications! You can give yourself a nice pat on the back."

    teacher "This examination will contain questions to test your knowledge about guide dog training."

    teacher "However, there is a short section on the front page that will not be graded."

    teacher "Its for our understanding on what type of person you are. To admit your weaknesses show character."

    teacher "Please be as honest as you possibly can be. We want to know what training style best suits you!"

    teacher "With that being said, I wish you all the best of luck! If you have any questions, please do not hesitate to ask!"

    narrator "She hands a smaller stack of papers row by row, instructing everyone to pass them back."

    narrator "You feel a sudden tap on your shoulder."

    m "Good luck, okay? (She gives a slight smile)"

    temp "Yeah!"

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # Test begins here

    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
            povname = "Jesse"

    define pov = Character("[povname]")

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
                dog = Character(lab.name)
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
        if dogObj == beagle:
            mdogObj = lab
            mdog = Character(mdogObj.name)
        elif dogObj == akita:
            mdogObj = beagle
            mdog = Character(mdogObj.name)
        else:
            mdogObj = akita
            mdog = Character(mdogObj.name)

    $ pov("My dog's name is " + dogObj.name)
    $ m(m.name + "'s dog is " + mdogObj.name)

    label dailyChoice:
        menu:
            "How will you train your dog?"

            "Obedience Training":
                python:
                    training = "o"
                    passed = passDialogue(dogObj.obedience, dogObj.agility)
                    training = "None"
                    if passed and dogObj.obedience < 3:
                        dogObj.obedience+=1
                    narrator("Your dogs obedience level is now " + str(dogObj.obedience))
            "Intelligence Training":
                python:
                    training = "i"
                    passed = passDialogue(dogObj.intelligence, dogObj.obedience)
                    training = "None"
                    if passed and dogObj.intelligence < 3:
                        dogObj.intelligence+=1
                    narrator("Your dogs intelligence level is now " + str(dogObj.intelligence))
            "Agility Training":
                python:
                    training = "a"
                    passed = passDialogue(dogObj.agility, dogObj.intelligence)
                    training = "None"
                    if passed and dogObj.agility < 3:
                        dogObj.agility+=1
                    narrator("Your dogs agility level is now " + str(dogObj.agility))

    ## Enter code here for connecting sprites to dog ##

    return
