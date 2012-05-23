
#--------------------------------------------------------------------
# Pinky's exclamations.

exclamations = \
["Narf!",
 "Zort!",
 "Nogg!",
 "Poit!",
 "Oooo!"]


def exclaim(lovebot,input):
	import random
	mRnd = len(exclamations)-1
	recordNum = random.randint(0, mRnd)
	lovebot.say(exclamations[recordNum])
exclaim.rule = r'^!excited'
