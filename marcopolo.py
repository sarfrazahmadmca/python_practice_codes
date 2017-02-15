"""
Marco Polo Instructions
In the old city of Venice it was important for children to be good at math so they could grow up to be great merchants. One way for the children of Venice to practice their math skills was to play a game called Marco Polo, named after the great explorer from Venice.
The game is simple.
The children sit around in a circle and count the numbers from 1 to 100. However, every time the number that a child is supposed to say is divisible by 4, the child says 'marco' instead of the number. Every time the number is divisible by 7, the child says 'polo' instead of the number. If the number is divisible by both 4 and 7, the child will say 'marcopolo'.

Goal

Your task is to write a small program that will print out all the correct answers for this game from 1 to 100 in a single string, so that children may use a cheat sheet to follow along.

Expected Output

When executed, your function should print a single string of all answers from 1 to 100.

You may use the following output as the expected result for numbers 1 to 30 for your unit test.

1,2,3,marco,5,6,polo,marco,9,10,11,marco,13,polo,15,marco,17,18,19,marco,polo,22,23,marco,25,26,27,marcopolo,29,30
"""


def marcopolo(n):
	for i in range(1, n+1):
		if i% 4 == 0 and i %7 ==0:
			print "marcopolo",
		elif i % 4 ==0:
			print "marco",
		elif i % 7 ==0:
			print "polo",
		else:
			print i,

marcopolo(100)
