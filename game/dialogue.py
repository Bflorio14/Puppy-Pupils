def o_good(narrator, stat):
    if stat == 1:
        narrator("(GOOD) Your dogs obedience level is 1")
        return True
    elif stat == 2:
        narrator("(GOOD) Your dogs obedience level is 2")
        return True
    else:
        narrator("Your dogs obedience level is maxed out")
        return False
def o_bad(narrator, stat):
    if stat == 1:
        narrator("(BAD) Your dogs obedience level is 1")
    elif stat == 2:
        narrator("(BAD) Your dogs obedience level is 2")
    else:
        narrator("Your dogs obedience level is maxed out")
    return False
def i_good(narrator, stat):
    if stat == 1:
        narrator("(GOOD) Your dogs intelligence level is 1")
        return True
    elif stat == 2:
        narrator("(GOOD) Your dogs intelligence level is 2")
        return True
    else:
        narrator("Your dogs intelligence level is maxed out")
        return False
def i_bad(narrator, stat):
    if stat == 1:
        narrator("(BAD) Your dogs intelligence level is 1")
    elif stat == 2:
        narrator("(BAD) Your dogs intelligence level is 2")
    else:
        narrator("Your dogs intelligence level is maxed out")
    return False
def a_good(narrator, stat):
    if stat == 1:
        narrator("(GOOD) Your dogs agility level is 1")
        return True
    elif stat == 2:
        narrator("(GOOD) Your dogs agility level is 2")
        return True
    else:
        narrator("Your dogs agility level is maxed out")
        return False
def a_bad(narrator, stat):
    if stat == 1:
        narrator("(BAD) Your dogs agility level is 1")
    elif stat == 2:
        narrator("(BAD) Your dogs agility level is 2")
    else:
        narrator("Your dogs agility level is maxed out")
    return False
def night0(narrator, pov, dog): #dog paramater is a Dog object
    if dog.name == "Jun":
        narrator("You pat down on the blanket. " + dog.name + " comes forward immediately, trying their best to please you.")
        narrator("However, he does not really understand what you're asking for him to do.")
        narrator("He picks up the blanket in his mouth, and gives it right back to you.")
        pov("No, " + dog.name + "! This is your bed. You lay down in it to sleep!")
        narrator("There is a flush of disappointment in [dog]'s eyes. You can tell he is trying his best to follow your commands, but he does not understand.")
        pov("You sit down on your bed out of frustration")
        narrator(dog.name + "picks up blanket once again in his mouth, and brings it over to the foot of your bed. He seems to want to stay close to you!")
        pov("(He seems to be very obedient... I just wish he understood what I was saying!)")
        pov("(Maybe I shouldn't focus on training him in obedience this week...)")
        pov("(His weakness seems to be his intelligence. Maybe I should focus on that!)")
        pov(dog.name + ", lay down!")
        narrator(dog.name + " seems to have got the hint and laid down.")
        narrator("Unfortunately, he did not lay on the blanket, but under it.")
        narrator("You can't help but grin at his determination to please you.")
        narrator("He passes out, and you can hear snoring from under the blanket.")
    elif dog.name == "Mehira":
        narrator("You bend over and pat in the middle of the blanket, but " + dog.name + " seems completely distracted!")
        narrator("After calling a couple times to lay down in the bed, " + dog.name +" seems like they don't want to listen to you.")
        pov("(She seems as if her strongest weakness is obedience...)")
        narrator("Right now, you decide that she will eventually have to fall asleep, so you lay down in your own bed, getting ready to doze off.")
        narrator("After what seems like hours of her having \"zoomies\", biting on anything that is humanly possible, and limitless tail chases...")
        narrator("She passes out. Not *quite* on the bed. Only the tip of her foot is touching the blanket.")
        narrator("The rest of her body is sprawled out from exhaustion.")
        pov("(She seems to have a lot of energy. She must be very agile!)")
        pov("(Guess that means I should NOT focus on training her in agility these three days.)")
    elif dog.name == "Kanchi":
        narrator(dog.name + "  seems to understand everything that you are saying!")
        narrator("Without you having to make a gesture, she comes over to the blanket you laid out for her.")
        pov("(She seems like a very intelligent dog!)")
        pov("(Guess that means I shouldn't focus on training her intelligence these three days.)")
        narrator("Once " + dog.name + " steps onto the blanket, she stumbles and falls!")
        narrator("She cries and sporadically tries to get away from the blanket.")
        narrator("However, she keeps getting caught on the blanket.")
        narrator("You step in to try to help her get unstuck, and once she is released, she cowers in sight of the blanket.")
        pov("(She seems like her worst weakness is her clumsiness... maybe she's not very agile?)")
        narrator("After a long battle of you trying to slowly reintroduce the blanket to [dog], she finally feels safe enough to lay on the blanket once more.")
        narrator("This time she is successful, and curls up into a small ball.")
    narrator("You eventually pass out as well, hopeful for the next day.")
def night1(narrator, pov, dog,success): #dog paramater is a Dog object
    if dog.name == "Jun": #akita
        narrator(dog.name + "tilts their head at you...")
        if success:
            narrator("...and they plop right down on the bed!")
            narrator("Good think you trained them in intelligence today!")
        else:
            narrator("...and they pick up the bed in their mouth!")
            narrator("You tell him to drop it, but he doesn’t seem to understand!")
            narrator("He drops the bed eventually, and it’s now flipped over.")
            narrator(dog.name + " plops right down on top of it, and looks at you with a smile!")
            narrator("You’re starting to wish you trained him in agility today instead.")

    elif dog.name == "Mehira": #beagle
        narrator(dog.name + " lays down on the bed, and starts to rip it apart!")
        pov("Hey! Stop that!")
        if success:
            narrator(dog.name + " stops, looks at you, and wags their tail!")
            narrator("Good thing you trained them in obedience today! They seem to be learning!")
        else:
            narrator(dog.name + " pauses, and doesn’t care to listen!")
            narrator("She starts chewing out the stuffing out of the bed!")
            narrator("You pick her up, and throw the bed out of the room. You put back the blanket for now.")
            narrator("You’re starting to wish you trained in her in obedience today instead.")

    elif dog.name == "Kanchi":
        narrator(dog.name + " starts to circle around the bed...")
        if success:
            narrator("He plops and sits right down!")
            narrator("Good thing you trained them in agility! She seem to be less clumsy tonight.")
        else:
            narrator("And trip on her own two feet!")
            narrator("She get scared again and refuse to lay back on the bed.")
            narrator("She grabs the blanket out of the laundry basket and rolls up into it like a burrito.")
            narrator("You’re starting to wish you trained her in agility today instead.")
    narrator("You turn it in for the night, and eventually fall asleep.")
