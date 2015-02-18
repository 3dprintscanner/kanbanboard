import unittest
import uuid

# The program should .... create cards with a name and owner

card ={}
cards = {}
default_list_value = 'todo'
number = 1

def create_new_card(name):
	global number
	card['name'] = name
	card['list'] = default_list_value
	card['owner'] = 'nil'
	card['id'] = number
	cards[card['id']] = card
	number +=1

def assign_card(id,new_owner='default owner'):
	cards[id]['owner'] = new_owner

def move_card_assigned(id,owner,target_list='wip'):
	cards[id]['list']=target_list

def finish_card(id,owner):
	if cards[id]['owner'] == owner:
		cards[id]['list'] = 'done'
	else:
		print('Error, wrong or no owner supplied')

# class MyTest(unittest.TestCase):
# 	def test(self):
#     	assert('name' in cards)
