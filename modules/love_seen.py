#!/usr/bin/env python
"""
seen.py - Phenny Seen Module
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import time
from pymongo import Connection
from datetime import datetime

def lovebot_seen(lovebot, input): 
   """.seen <nick> - Reports when <nick> was last seen."""
   c = Connection()
   db = c.lovers_data
   lovers = db.seen
   nick = input.group(1)
   if nick != "":
      nick = nick.lower()
      lover = lovers.find_one({'nickname':nick})
      if lover:
         time = datetime.fromtimestamp(lover['time']+28800)
         msg = "I last saw %s at %s GMT on %s" % (lover['nickname'], time, lover['channel'])
      else:
         msg = "I haven't seen %s, %s."%(nick,input.nick)
   else:
      lovuhs = lovers.find()
      msg = "I have seen "
      for lover in lovahs:
         msg += "%s, "%(lover['nickname'])
      msg += " %s, try !seen (nick) for more information."%(input.nick)

   
   lovebot.say(msg)
   
lovebot_seen.rule = (r'!seen ([^\s]*)')


def lovebot_note(lovebot, input):
   c = Connection()
   db = c.lovers_data
   lovers = db.seen
   nick = input.nick.lower()
   lover = lovers.find_one({'nickname':nick})
   if lover:
      lover['time'] = time.time()
      lover['channel'] = input.sender
   else:
      lover = {'nickname':nick,'channel':input.sender, 'time':time.time()}
   lovers.save(lover)


lovebot_note.rule = r'(.*)'
lovebot_note.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
