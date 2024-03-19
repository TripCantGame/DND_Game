import random

#######################################################
# Controls the overall values being returned during actions
##############################################################

##rolls a D20 dice
def random_roll_20():
    roll = random.randint(1, 20)
    return roll