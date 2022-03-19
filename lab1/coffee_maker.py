"""
A command-line controlled coffee maker.
"""

import sys
import math

"""
Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

Requirements:
    - use functions
    - use __main__ code block
    - access and modify dicts and/or lists
    - use at least once some string formatting (e.g. functions such as strip(), lower(),
    format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
    - BONUS: read the coffee recipes from a file, put the file-handling code in another module
    and import it (see the recipes/ folder)

There's a section in the lab with syntax and examples for each requirement.

Feel free to define more commands, other coffee types, more resources if you'd like and have time.
"""

"""
Tips:
*  Start by showing a message to the user to enter a command, remove our initial messages
*  Keep types of available coffees in a data structure such as a list or dict
e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
as value
"""

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  #!!! when making coffee you must first check that you have enough resources!
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"

# Coffee maker's resources - the values represent the fill percents
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}

"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""
def exitf():
	sys.exit()

def resources():
	print(RESOURCES)

def refill(s):
	if s=="all\n":
		RESOURCES[WATER]=100
		RESOURCES[COFFEE]=100
		RESOURCES[MILK]=100
	if s=="water\n":
		RESOURCES[WATER]=100
	if s=="coffee\n":
		RESOURCES[COFFEE]=100

	if s=="milk\n":
		RESOURCES[MILK]=100


if __name__ == "__main__":

	print("I'm a simple coffee maker")
	
	while True:
		print("commands pls")

		r=sys.stdin.readline()

		if r=="exit\n":
			exitf()


		if r=="resources\n":
			resources()

		if r=="help\n":
			print(commands)

		if r=="list\n":
			print(ESPRESSO)
			print(AMERICANO)
			print(CAPPUCCINO)

		if r=="make\n":
			print("which cofee")
			s=sys.stdin.readline()
			if s=="espresso\n":
					RESOURCES[WATER]=RESOURCES[WATER] - 10
					RESOURCES[COFFEE]=RESOURCES[COFFEE] - 10
					resources()

			if s=="americano\n":
					RESOURCES[WATER]=RESOURCES[WATER] - 10
					RESOURCES[MILK]=RESOURCES[MILK] - 10
					resources()
					
			if s=="cappuccino\n":
					RESOURCES[MILK]=RESOURCES[MILK] - 10
					RESOURCES[COFFEE]=RESOURCES[COFFEE] - 10
					resources()

		if r=="lower\n":
			for i in commands:
				print(i.lower())

		if r=="upper\n":
			for i in commands:
				print(i.upper())

		if r=="pi\n":
			pi=math.pi
			print("The value of pi is approximately %s"% format(pi, '.14f'))

		if r=="refill\n":
			print("which one or all")
			s=sys.stdin.readline()
			refill(s)

	
	print("ok")
