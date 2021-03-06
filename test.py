#!/usr/bin/python3
from lib.Element import *
from lib.Page import *
from lib.Site import *
import random
import shutil
import pprint

random.seed()

def makeChoice():
	print( '\nSelect a lib to check: ' )
	print( '   (1) Element.py' )
	print( '   (2) Page.py' )
	print( '   (3) Site.py' )
	print( '   (e) Exit test.py' )
	choice = input()
	return choice

def makeDummyEle():
	test_element = Element( 'text')
	test_element.content = str( random.getrandbits( 32))
	test_element.location = str( random.getrandbits( 8))
	return test_element

def makeDummyPage( site):
	name = random.getrandbits( 16)
	print( 'Page name will be ' + str( name))
	test_page = Page( site + str( name))
	return test_page

def checkElement_py():
	print( 'Testing instantiation...')
	try:
		test_element = Element( 'text')
	except ElementError as why:
		print( why.reason)
	try:
		test_element = Element( 'image')
	except ElementError as why:
		print( why.reason)
	try:
		test_element = Element( str( random.getrandbits( 32)))
		print( 'Instantiation of unspecified Element type succeeded...FAILURE.')
	except:
		pass
	print( 'Instantiation OK.')

	print( 'Testing render()...')
	try:
		pprint.pprint( makeDummyEle().render())
	except ElementError as why:
		print( why.reason)
	print( 'render() OK.')

	print( 'Testing load()...')
	try:
		test_element.load( makeDummyEle().render())
	except ElementError as why:
		print( why.reason)
	print( 'load() OK.')

def checkPage_py():
	print( 'Testing instantiation...')
	try:
		test_page = makeDummyPage( '')
	except PageError as why:
		print( why.reason)
	print( 'Instantiation OK.')
	
	print( 'Testing add()...')
	try:
		test_element = makeDummyEle()
		print( 'Adding element id ' + test_element.id)
		test_page.add( test_element)
	except PageError as why:
		print( why.reason)
	print( 'add() OK.')

	print( 'Testing retrieve()...')
	try:
		print( test_page.retrieve( test_element.id))
	except PageError as why:
		print( why.reason)
	print( 'retrieve() OK.')


	print( 'Testing render()...')
	try:
		pprint.pprint( test_page.render())
	except PageError as why:
		print( why.reason)
	print( 'render() OK.')

	print( 'Testing remove()...')
	try:
		test_page.remove( test_element.id)
	except PageError as why:
		print( why.reason)
	print( 'remove() OK.')
	shutil.rmtree( test_page.name)
	
def checkSite_py():
	print( 'Testing instantiation...')
	try:
		test_site = Site( "test_site")
	except SiteError as why:
		print( why.reason)
	print( 'Instantiation OK.')

	print( 'Testing add()...')
	test_page = makeDummyPage( test_site.name + '/')
	test_page.add( makeDummyEle())
	test_site.add( test_page)
	print( 'add() OK.')

	print( 'Testing render()...')
	test_site.render()
#	for page in test_site.render():
#		pprint.pprint( test_site.render()[page].render())
	print( 'render() OK.')
	
	print( 'Testing remove()...')
	try:
		test_site.remove( test_page.name)
	except SiteError as why:
		print( why.reason)
	print( 'remove() OK.')

checking = True
while checking == True:
	choice = makeChoice()
	if choice == '1':
		checkElement_py()
	elif choice == '2':
		checkPage_py()
	elif choice == '3':
		checkSite_py()
	elif choice == 'e':
		checking = False
	else:
		print( 'ERROR: Given option invalid' )
