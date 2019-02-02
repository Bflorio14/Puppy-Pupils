def o_good(narrator, stat):
    if stat == 1:
        narrator("(GOOD) Your dogs obedience level is 1")
    elif stat == 2:
        narrator("(GOOD) Your dogs obedience level is 2")
    else:
        narrator("(GOOD)Your dogs obedience level is maxed out")
def o_bad(narrator, stat):
    if stat == 1:
        narrator("(BAD) Your dogs obedience level is 1")
    elif stat == 2:
        narrator("(BAD) Your dogs obedience level is 2")
    else:
        narrator("(BAD) Your dogs obedience level is maxed out")
