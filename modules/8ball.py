
"""An IRC bot to respond with 8ball prognostications.
"""

prognostications = [\
"It is certain",
"It is decidedly so",
"Without a doubt",
"Yes definitely",
"You may rely on it",
"As I see it yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful"]

def EightBall(lovebot,input):
	import random
	mRnd = len(prognostications)-1
	rnd = random.randint(0, mRnd)
	lovebot.say("%s, %s" % (prognostications[rnd],input.nick) )

EightBall.rule = (r'!8ball.*')
