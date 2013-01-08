import random

x=0

inputskill=raw_input("please provide what skill bonus you have: ")
intskill=float(inputskill)
inputchallenge=raw_input("Please provide the opposing challenge level: ")
intchallenge=float(inputchallenge)
inputcontests=raw_input("Please provide the number of rolls: ")
intcontests=float(inputcontests)

def tempotest(skill,challenge):
    rolls=0
    global wins
    wins=0
    global losses
    losses=0
    while(rolls<intcontests):
        dice1=random.randrange(0,7)
        dice2=random.randrange(0,7)
        dice3=random.randrange(0,7)
        if dice1+dice2+dice3 + skill < challenge:
            print "Loss :("
            losses=losses +1
            rolls=rolls+1
        
        else:
            print "Win :D"
            wins=wins+1
            rolls=rolls+1
           
            
tempotest(intskill,intchallenge)

percentile=wins / intcontests

print "Total wins  are %s" %wins
print "Total losses are %s" %losses
print "Percentage of wins was %d" %percentile
