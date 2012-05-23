
#--------------------------------------------------------------------
# Pinky's exclamations.

exclamations = \
["Narf!",
 "Zort!",
 "Nogg!",
 "Poit!",
 "Oooo!",
 "Ooooh, a button!",
 "God damn it!",
 "Fuck!",
 "Shit, piss, hell, fuck, cocksucker, motherfucker!",
 "Nobody messes with the Jesus!",
 "It ain't gonna suck itself, bitch!",
 "It ain't gonna lick itself, bitch!"]


def exclaim(lovebot,input):
	import random
	mRnd = len(exclamations)-1
	recordNum = random.randint(0, mRnd)
	lovebot.say(exclamations[recordNum])
exclaim.rule = r'^!excited'
