
"""An IRC bot to respond as 'Pinky'.

This is an example bot that uses the SingleServerIRCBot class from
ircbot.py.  The bot enters a channel and listens for commands in
private messages and channel traffic.  Commands in channel messages
are given by prefixing the text by the bot name followed by a colon.

"""



#--------------------------------------------------------------------
# Pinky's exclamations.

exclamations = \
["Narf!",
 "Zort!",
 "Nogg!",
 "Poit!",
 "Oooo!"]


#--------------------------------------------------------------------
# Pinky's ponderings.

ponderings = \
["I think so, Brain, but where are we going to find a duck and a hose at this hour?",
"I think so, but where will we find an open tattoo parlor at this time of night?",
"Wuh, I think so, Brain, but if we didn't have ears, we'd look like weasels.",
"Uh... yeah, Brain, but where are we going to find rubber pants our size?",
"Uh, I think so, Brain, but balancing a family and a career ... ooh, it's all too much for me.",
"Wuh, I think so, Brain, but isn't Regis Philbin already married?",
"Wuh, I think so, Brain, but burlap chafes me so.",
"Sure, Brain, but how are we going to find chaps our size?",
"Uh, I think so, Brain, but we'll never get a monkey to use dental floss.",
"Uh, I think so Brain, but this time, you wear the tutu.",
"I think so, Brain, but culottes have a tendency to ride up so.",
"I think so, Brain, but if they called them 'Sad Meals', kids wouldn't buy them!",
"I think so, Brain, but me and Pippi Longstocking -- I mean, what would the children look like?",
"I think so, Brain, but this time *you* put the trousers on the chimp.",
"Well, I think so, Brain, but I can't memorize a whole opera in Yiddish.",
"I think so, Brain, but there's still a bug stuck in here from last time.",
"Uh, I think so, Brain, but I get all clammy inside the tent.",
"I think so, Brain, but I don't think Kay Ballard's in the union.",
"Yes, I am!",
"I think so, Brain, but, the Rockettes? I mean, it's mostly girls, isn't it?",
"I think so, Brain, but pants with horizontal stripes make me look chubby.",
"Well, I think so -POIT- but *where* do you stick the feather and call it macaroni?",
"Well, I think so, Brain, but pantyhose are so uncomfortable in the summertime.",
"Well, I think so, Brain, but it's a miracle that this one grew back.",
"Well, I think so, Brain, but first you'd have to take that whole bridge apart, wouldn't you?",
"Well, I think so, Brain, but 'apply North Pole' to what?",
"I think so, Brain, but 'Snowball for Windows'?",
"Well, I think so, Brain, but *snort* no, no, it's too stupid!",
"Umm, I think so, Don Cerebro, but, umm, why would Sophia Loren do a musical?",
"Umm, I think so, Brain, but what if the chicken won't wear the nylons?",
"I think so, Brain, but isn't that why they invented tube socks?",
"Well, I think so Brain, but what if we stick to the seat covers?",
"I think so Brain, but if you replace the 'P' with an 'O', my name would be Oinky, wouldn't it?",
"Oooh, I think so Brain, but I think I'd rather eat the Macarana.",
"Well, I think so *hiccup*, but Kevin Costner with an English accent?",
"I think so, Brain, but don't you need a swimming pool to play Marco Polo?",
"Well, I think so, Brain, but do I really need two tongues?",
"I think so, Brain, but we're already naked.",
"We eat the box?",
"Well, I think so, Brain, but if Jimmy cracks corn, and no one cares, why does he keep doing it?",
"I think so, Brain *NARF*, but don't camels spit a lot?",
"I think so, Brain, but how will we get a pair of Abe Vigoda's pants?",
"I think so, Brain, but Pete Rose? I mean, can we trust him?",
"I think so, Brain, but why would Peter Bogdanovich?",
"I think so, Brain, but isn't a cucumber that small called a gherkin?",
"I think so, Brain, but if we get Sam Spade, we'll never have any puppies.",
"I think so, Larry, and um, Brain, but how can we get seven dwarves to shave their legs?",
"I think so, Brain, but calling it pu-pu platter? Huh, what were they thinking?",
"I think so, Brain, but how will we get the Spice Girls into the paella?",
"I think so, Brain, but if we give peas a chance, won't the lima beans feel left out?",
"I think so, Brain, but if we had a snowmobile, wouldn't it melt before summer?",
"I think so, Brain, but what kind of rides do they have in Fabioland?",
"I think so, Brain, but can the Gummi Worms really live in peace with the Marshmallow Chicks?",
"Wuh, I think so, Brain, but wouldn't anything lose it's flavor on the bedpost overnight?",
"I think so, Brain, but three round meals a day wouldn't be as hard to swallow.",
"I think so, Brain, but if the plural of mouse is mice, wouldn't the plural of spouse be spice?",
"Umm, I think so, Brain, but three men in a tub? Ooh, that's unsanitary!",
"Yes, but why does the chicken cross the road, huh, if not for love?  (sigh)  I do not know.",
"Wuh, I think so, Brain, but I prefer Space Jelly.",
"Yes Brain, but if our knees bent the other way, how would we ride a bicycle?",
"Wuh, I think so, Brain, but how will we get three pink flamingos into one pair of Capri pants?",
"Oh Brain, I certainly hope so.",
"I think so, Brain, but Tuesday Weld isn't a complete sentence.",
"I think so, Brain, but why would anyone want to see Snow White and the Seven Samurai?",
"I think so, Brain, but then my name would be Thumby.",
"I think so, Brain, but I find scratching just makes it worse.",
"I think so, Brain, but shouldn't the bat boy be wearing a cape?",
"I think so, Brain, but why would anyone want a depressed tongue?",
"Um, I think so, Brainie, but why would anyone want to Pierce Brosnan?",
"Methinks so, Brain, verily, but dost thou think Pete Rose by any other name would still smell as sweaty?",
"I think so, Brain, but wouldn't his movies be more suitable for children if he was named Jean-Claude van Darn?",
"Wuh, I think so, Brain, but will they let the Cranberry Dutchess stay in the Lincoln Bedroom?",
"I think so, Brain, but why does a forklift have to be so big if all it does is lift forks?",
"I think so, Brain, but if it was only supposed to be a three hour tour, why did the Howells bring all their money?",
"I think so, Brain, but Zero Mostel times anything will still give you Zero Mostel.",
"I think so, Brain, but if we have nothing to fear but fear itself, why does Elanore Roosevelt wear that spooky mask?",
"I think so, Brain, but what if the hippopotamus won't wear the beach thong?",
]

def takeOverTheWorld(lovebot, input):
	import random
	mRnd = len(ponderings)-1;
	recordNum = random.randint(0, mRnd)
	lovebot.say(ponderings[recordNum])

takeOverTheWorld.rule = r'.*are you (:?thinking|pondering) what I\'m thinking\?.*'

def exclaim(lovebot,input):
	import random
	mRnd = len(exclamations)-1
	recordNum = random.randint(0, mRnd)
	lovebot.say(exclamations[recordNum])
exclaim.rule = r'^.+\!.*$'
