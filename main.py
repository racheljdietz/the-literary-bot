import config
import random
import sys

from twython import Twython

api = Twython(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_KEY, config.ACCESS_SECRET)

# return random noun
def getNoun(type):
    if type == 1:
        return random.choice([line.rstrip('\n') for line in open('nouns/1syllablenouns.txt')])
    elif type == 2:
        return random.choice([line.rstrip('\n') for line in open('nouns/2syllablenouns.txt')])
    else:
        return random.choice([line.rstrip('\n') for line in open('nouns/abstractnouns.txt')])

# return random verb
def getVerb(type):
    if type == 1:
        return random.choice([line.rstrip('\n') for line in open('verbs/1syllableverbs.txt')])
    elif type == 2:
        return random.choice([line.rstrip('\n') for line in open('verbs/2syllableverbs.txt')])

# return random adjective
def getAdj(type):
    if type == 1:
        return random.choice([line.rstrip('\n') for line in open('adjectives/1syllableadjectives.txt')])
    elif type == 2:
        return random.choice([line.rstrip('\n') for line in open('adjectives/2syllableadjectives.txt')])

# return random adverb 
def getAdv():
    return random.choice([line.rstrip('\n') for line in open('adverbs/2syllableadverbs.txt')])

# vowels
vowel = 'aeiou'

# return true if first character is vowel
def firstVowel(string):
    if string[0].lower() in vowel:
        return True
    else:
        return False

# return the correct article ("a" or "an")
def getArticle(string):
    if firstVowel(string):
        return "an"
    else:
        return "a"

adj = getAdj(2)

post = getAdj(3).capitalize() + " " + getNoun(2) + ",\n"
post += getVerb(2) + " towards " + getNoun(0) + " and " + "\n"
post += getAdv() + " " + getVerb(1) + " away."

api.update_status(status=post)
