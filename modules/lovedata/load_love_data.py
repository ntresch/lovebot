from pymongo import Connection
from pymongo import DESCENDING as D

def load(text):
	c = Connection()
	db = c.lovers_data
	advice = db.advice

	lastNum = advice.find_one(sort=[('recordNum',D)])
	if lastNum:
		thisNum = lastNum['recordNum'] + 1
	else:
		thisNum = 1
	toLoad = {'aText':text,'recordNum':thisNum}
	advice.save(toLoad)
