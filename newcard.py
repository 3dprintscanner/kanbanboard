#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Coding dojo task:

# Your team needs a digital Kanban board urgently.

# So create a board with columns for To Do, In Progress, Review and
# Done.

# New tasks are set in the column To Do and are moved to the next
# right column, if there is not already reached the WIP limit.

# Tasks has to be token by team members in the moment they move it to
# In Progress.

# Visualize the board as you like.

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

## Tests

# class MyTest(unittest.TestCase):
#       def test(self):
#       assert('name' in cards)

def name_exists_test():
    assert 'name' in cards[1]
    # if 'name' in cards[1]:
    # print("Erfolg")
    # else:
    # print("Fehler")

def wrong_positiv_test():
    assert not 'foo' in cards[1], "foo should not be a valid sybmol of cards[1]"

print('newcard.py')

# run tests only if not imported
if __name__ == '__main__' :
    create_new_card('firstcase')
    wrong_positiv_test()
    print("__name__ == '__main__'")
    print(cards)
    name_exists_test()
