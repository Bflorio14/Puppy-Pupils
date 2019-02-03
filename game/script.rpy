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

    "The rest of the exam you blasted through. You felt confident submitting your test."

    "Later, you meet up with your new friend outside."

    m "Hey, this is kind of awkward, but I never happened to catch your name."

    pov "[pov], and you?"

    m "My name is Madigan! Nice to meet you properly!"
    "She smiles."
    m "How’d you think of the test?"

    menu:
        "It was challenging!":
            m "I thought it was pretty thought-provoking too…"
            $hardTest=True
        "It was easy!":
            m "I’m glad you think so!"
            $hardTest=False
    m "I hope you did well! Maybe we’ll see each other tomorrow too?"

    pov "Yeah, sure!"

    m "It’s nice to have already made a friend!"
    m "Anyways, I will catch you tomorrow!"

    "You part ways and drive back to your home"
    #goes home
    "After a long day, you throw yourself onto the bed simultaneously as your backpack hits the floor."
    "For the first time all day, you feel relaxed. You remind yourself that the hardest part was taking the test, and the rest should come easy…"
    "At least you thought."
    "From the whirlwind of emotions today, you pass out almost immediately afterward with a soft grin written on your face."
    #next day at training school.
    "You woke up that morning feeling refreshed. You took no time at all to get to the school this morning."
    "You met up with Madigan, both feeling the same rollercoaster of emotions as yesterday."
    "Small chatters fill the field with a sense of curiosity."
    if hardTest:
        "You cannot contain your nerves. Feeling like the test was hard makes you even more nervous!"
    else:
        "You cannot contain your nerves. Feeling like the test was easy doesn’t make you feel any less nervous."

    "Distinctive chatter fills the room when Mrs. Clawson stands up."

    teacher "Okay everyone! Please settle down!."
    teacher "I have an announcement to make…"
    "The room slowly shifts to an anticipated silence"
    teacher "Through bizarre, and unpredictable conditions…"
    teacher "Everyone passed the examination with flying colors!"
    "Chatter begins to fill the air once more"
    teacher "Please settle down! I’m not quite finished!"
    teacher "As much as we would love to have all you talented individuals here, we unfortunately don’t have enough room to keep you all…"
    teacher "Our team has come up with a new test."
    m "(Whispering Softly) A new test? I don’t think I’m ready…"
    teacher "Before you start chattering again, please let me finish explaining."
    teacher "Traditionally, this would be your first step in your training."
    teacher "But because of the circumstances, We believe that giving you the opportunity to train here will give you an advantage at more foundations like ours."
    teacher "That being said, we will only take the best of the group here."
    m "(In whispers) I’m getting more nervous…"
    teacher "We will be giving you temporary partners to have hands on experience!"
    teacher "Partners, of course, meaning your own dog!"
    m "D-dog?!"
    teacher "That’s right, you heard me fine!"
    teacher "We have already randomly assigned your dog to you!"
    teacher "But first let me go through a briefing on what we do here…"
    label repeat:
        teacher "You will have three days to complete this assignment."
        teacher "On receiving your dog, you will have to learn it’s traits."
        teacher "Meaning both their strengths and their weaknesses."
        teacher "In this assignment, we ask of you to strengthen their weaknesses."
        teacher "However, don’t be fooled, there are challenges that come with training a dog in each trait."
        teacher "It’s like playing a game of rock, paper, scissors..."
        teacher "But it is more like obedience, intelligence, agility!"
        teacher "You cannot train a dog properly in one area if a specific stat is insufficient. For example..."
        label exampleRepeat:
            teacher "You cannot train a disobedient dog in intelligence. It will refuse to listen to you!"
            teacher "You also cannot train a dog in agility if they lack intelligence! Obstacle courses are difficult to master with even the most brilliant dog!"
            teacher "Lastly, you cannot train a dog in obedience if they lack agility. Less coordinated dogs may stumble while following through commands!"
        teacher "Do you need me to repeat the assignment?"
        menu:
            "Do you need me to repeat the assignment?"

            "Yes please!":
                jump repeat
            "Uhh, what were the examples again?":
                jump exampleRepeat
            "No thank you!":
                pass

    teacher "Let’s take a trip to our onsite training locations!"
    #goto agility location
    teacher "The great outdoors is the best way to train your dog in agility!"
    teacher "Try to get exercise in with your dog! Take them for a walk around the field, the building, or even the block!"
    teacher "Get them more associated with the world surrounding them! They will be leaders in the world after all!"
    teacher "I think that’s relatively straight forward, let’s move on to the next location!"
    #goto obedience site
    teacher "This is our classroom for our PUPil’s."
    "No one laughed at the joke"
    teacher "Ahem… I will be your boss here at this sight, and I have a soft spot for people who share the same sense of humor as me!"
    "A mumbled, force laughter fills the teacher’s ears"
    teacher "You’re getting it! Right, about the training course…"
    teacher "“We will be teaching your partners here on simple commands, such as fetch, sit, stay"
    teacher "And later on more difficult commands, such as pushing a button, or going to get help!"
    teacher "These commands are important for a guide dog in training!"
    teacher "Come along now, everyone!"
    #goto intelligence site
    teacher "This is our gymnasium where you will work with your dog to recognize certain items, like a water bottle, or a phone!"
    teacher "We will ask them to retrieve these items for us."
    teacher "The main concept here is to expand their knowledge of items that their owner may need on a daily basis."
    teacher "Thank you for being patient, I know you’ve all been waiting to see who your partner may be!"
    teacher "As you may notice, there are a group of trainers sitting on the bleachers with dogs in bandanas!"
    teacher "These will be your future partners. We will be assigning them to you right now."
    "Mrs.C pulls out a clipboard with a pen dangling by a string. She starts to read down the list of people."
    "Each person is introduced to their dog, and is given their leash."
    "Only about a minute passes before your name is addressed."
    $ teacher("[pov], will be partnered up with... ")
    $ teacher(dogObj.name + "!")
    if dogObj.name==lab.name:
        "An adorable Lab follows the walking pattern of previous dogs to a tee, but stumbles before your feet. They look up at you, a little disappointed in itself."
    if dogObj.name==akita.name:
        "An Akita approaches, seemingly unaware about the amount of drool hanging from their mouth."
    if dogObj.name==beagle.name:
        "A excited Beagle bascially drags it's handler to you. They are ecstatic to meet you!"

    "Mrs. C goes through a couple more names before announcing Madigan’s dog."
    $ teacher(m.name + ", you are partnered up with…")
    $ teacher(mdogObj.name + "!")
    if mdogObj.name==akita.name:
        "The trainer brings up to Madigan an akita, with a certain glimmer in its eye."
    elif mdogObj.name==beagle.name:
        "The trainer brings up to Madigan a beagle, with a certain glimmer in its eye."
    else:
        "The trainer brings up to Madigan a chocolate lab, with a certain glimmer in its eye."

    "Unlike the others, Madigan bends down and reaches out her hand as a peace offering."
    "[mdog] gently sniffs her hand. Madigan smiles."

    m "I’m excited to be working with you!"
    "After all other names are paired off with their partners, Mrs. C speaks up."

    teacher "We’ve reached the end of our partner pairings! You all will be spending a lot of time with your partners."
    teacher "It is crucial that you familiarize yourselves with one another."
    "She glances over to Madigan with a look of reassurance"
    teacher "Of course, I forgot to mention that these pup’s will be coming home with you!"
    "There is a sudden chatter filling the room of mixed emotions."
    teacher "However, we acknowledge that this was sprung on you last minute. We do understand if you must leave your partner here overnight at our kennel."
    teacher "But, as I mentioned before, it is crucial for you and your partner to familiarize each other with one another. You need to learn their traits and skill set in order to train them."
    teacher "Just as a gentle reminder, you only need to focus on your dog’s weaknesses throughout the three day course."
    teacher "You should not try to strengthen their best qualities, but train your dog in other areas to be on par with their strongest trait."
    teacher "How you train your partner is up to you!"
    teacher "You are all dismissed for the day. I will see you all tomorrow!"

    #goes home
    "After a long day of utter surprises, you bring your new partner to your apartment."
    "Being caught completely off guard, you have not arranged a bed for them to sleep in."
    "Instead, you bring a large blanket and put it on the floor on the other side of the room."

    pov "[dog], this is your bed for now! I’m sorry I wasn’t expecting company so soon."
    pov "Let’s call it in for a night, okay?"
    $ dialogue.night0(narrator, pov, dogObj)

    #next day at school
    "You and [dog] both seemed to have a restful night, despite the challenges you both faced."
    "You see Madigan and her partner, [mdog], coming up to meet you!"
    m "Hey [pov] and [dog]! Are you guys ready for the day?"
    mdog "Woof!"
    pov "Yes! Me and [dog] are both excited for today!"
    m "That's great! I think [mdog] and I have to figure out where we are training today..."
    m "Mrs. C mentioned yesterday how we should focus on our dogs weaknesses..."
    m "I had a great night with [mdog] last night, but I had trouble figuring out what their weaknesses are! They seem like such a well rounded dog!"
    mdog "Woof!"
    "Madigan giggles"
    m "So I have no idea where I’m starting today. I hope you at least have some idea where you’re going!"
    m "Maybe I’ll catch up with you later after training?"
    pov "Yeah, sure! Good luck on your first day!"
    m "(She gives you a bright smile) You too!"

    #training options
    call dailyChoice

    m "Hey [pov], [dog]! How was training?"
    if passed:
        pov "It was great! [dog] did a great job out there today!"
        m "Glad to hear it!"
    else:
        pov "It wasn’t great... but me and [dog] will get the hang of this soon!"
        m "That's the spirit!"
    m "Hey, what do you say if we grab a coffee on the way home tonight? Would you and [dog] be interested?"

    menu:
        "Yes, let's go!":
            #goto coffee shop

            "You and Madigan walked to a local coffee shop."
            "On entering, you smell strong flavors such as cinnamon, peppermint..."
            "You grab your favorite coffee drink, and get a pupachino for [dog]."
            "Madigan and you make your way towards a 2-seater table in the corner of the shop."
            "You tilt your pupacino towards [dog], and they happily shove their nose right in the whip cream!"
            m "Hey, [pov]..."
            pov "Yeah?"
            m "What made you want to be a guide dog trainer"
            "You pause to think about what you’re going to say."
            pov "My dad was a dog trainer. Not for guide dogs, but more for obedience."
            pov "I loved seeing the bond between him and his clients, and how determined he was."
            pov "I always grew up around dogs too, and eventually my dad taught me some tricks too!"
            pov "I started training with him, and eventually I became confident on my own, and started my own local business!"
            pov "I think it’s amazing what dogs are capable of if you just guide them."
            "You look down at [dog] and give them a pet on the head. They lean into your hand."
            m "I agree with you completely. I think guide dogs in particular are amazing."
            m "I haven’t had as much experience in hands on training. Actually none at all."
            m "My uncle was actually blind and he had a guide dog."
            m "To him, his dog, Iris, was more than just his service dog. She was his best friend. They went everywhere together."
            m "Even when Iris got too old, he kept her because they had such a great bond. Iris definitely returned the feeling."
            m "He went through a couple more guide dogs, and eventually my Uncle passed away from old age."
            m "I know it should be sad, but it fills me with bitter happiness because my uncle got to fill his life to the fullest."
            m "It was all thanks to his companions over the years. They made it possible."
            m "I want to let more people have that opportunity to live their life to their fullest, and to experience the same bond that my uncle and Iris had."
            m "That’s why I want to do this."
            pov "(Wow. Madigan’s story puts things in a whole new perspective.)"
            pov "(I always loved dogs, but she’s right. Guide dogs are very special.)"
            m "Anyway, thanks for coming out with me! It was nice to get to know you more!"
            pov "Yeah, you too!"
            $coffee=True

        "Maybe another time":
            $coffee=False
            pov "I think it’s getting a little late. [dog] and I are going to call it in for the night. I’ll catch you tomorrow?"
            m "Yeah, of course! See you tomorrow!"
    "On the way home, you stopped at the local pet store to pick up an appropriate bed for [dog]."
    "You pick up the blanket and throw it in the laundry basket. Where the blanket used to be, you place the bed."
    pov "C’mere [dog]!"
    "You pat down on the bed."
    $ dialogue.night1(narrator, pov, dogObj, passed)


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
        return
    ## Enter code here for connecting sprites to dog ##

    return
