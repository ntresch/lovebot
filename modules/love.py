from pymongo import Connection


def note_love(lovebot, input):
	c = Connection()
	db = c.lovers_data
	lovers = db.lovers
	

	s = input.group(1)
	s = s.strip()
	if (s == u'' or s.lower() == u'i'):
		s = input.nick.title()
	else:
		return
	o = input.group(4).strip().lower()
	lover = lovers.find_one({u'nickname':s})
	if lover:
		if not o in lover['lovelist']:
			lover['lovelist'].append(o)
			lovers.save(lover)
	else:
		lover = {u'nickname':s,u'lovelist':[o]}
		lovers.insert(lover)
	msg = '\x01ACTION %s %s\'s love for %s\x01' % ('witnesses',s,o)
	lovebot.say(msg)


note_love.rule = r'^(.*?)(<3)(:?\'s|s)*(.*)$'

def love_wrapper(lovebot,input):
	c = Connection()
	db = c.lovers_data
	lovers = db.lovers
	lover = lovers.find_one({u'nickname':input.nick.title()})
	o = input.group(1).strip().lower()
	if lover:
		if not o in lover['lovelist']:
			lover['lovelist'].append(o)
			lovers.save(lover)
	else:
		lover = {u'nickname':s,u'lovelist':[o]}
		lovers.insert(lover)
	msg = '\x01ACTION %s %s\'s love for %s\x01' % ('witnesses',lover['nickname'],o)
	lovebot.say(msg)


love_wrapper.rule = r'!love (.*)'

def lovers(lovebot, input):
	c = Connection()
	db = c.lovers_data
	lovers = db.lovers
	msg = ''
	for lover in lovers.find():

		msg += 'I have seen %s loving %s things, ' % (lover['nickname'], len(lover['lovelist']))
	
	lovebot.say(msg)

lovers.commands = ['lovers']
lovers.priority = 'medium'

def lover(lovebot,input):
	c = Connection()
	db = c.lovers_data
	lovers = db.lovers
	person = input.group(1)
	lover = lovers.find_one({u'nickname':person.title()})
	if lover:
		msg = 'I have seen %s loving ' % (lover['nickname'])
		for loved in lover['lovelist']:
			msg += '%s, ' %(loved)
		msg += '.'
		lovebot.say(msg)
	else:
		lovebot.say("I've never seen %s loving anything, %s!" % (person, input.nick))		

lover.rule = r'!lover ([^\s]+)'

def loves(lovebot,input):
	c = Connection()
	db = c.lovers_data
	lovers = db.lovers
	obj = input.group(1).strip().lower()
	names = []
	msg = ""
	for lover in lovers.find():
		if obj in lover['lovelist']:
			names.append(lover['nickname'])
	if len(names)>0:
		for name in names:
			msg += "%s, "%(name)
		msg+= " all love %s."%(obj)
	else:
		msg = "no one loves %s, %s"%(obj,input.nick)
	lovebot.say(msg)
loves.rule = r'!loves (.+)'

def witness(lovebot,input):
	lover(lovebot,input)
witness.rule = r'!witness ([^\s]+)'

def editlovelist(lovebot,input):
	c = Connection()
	db = c.lovers_data
	lovers = db.lovers
	lover = lovers.find_one({u'nickname':input.nick.title()})
	if not lover:
		lovebot.say("You dont love anything, %s." % input.nick)
		return
	obj = input.group(1).strip().lower()
	
	if obj in lover['lovelist']:
		lover['lovelist'].remove(obj)
		lovebot.say("I guess you didn't love %s after all, %s!" % (obj,input.nick))
	else:
		lovebot.say("You didn't love %s in the first place, %s!"% (obj,input.nick))
	lovers.save(lover)

editlovelist.rule = r'!unlove (.+)'

import random
def advice(lovebot,input):
	c = Connection()
	db = c.lovers_data
	advice = db.advice
	mRnd = advice.count();
	recordNum = random.randint(1, mRnd)
	a = advice.find_one({'recordNum':recordNum})
	lovebot.say('%s, %s'%(input.nick,a['aText']))

advice.commands = ['advice']