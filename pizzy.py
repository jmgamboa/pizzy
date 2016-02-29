from time import sleep
import random

def prRed(prt): print "\033[91m {}\033[00m" .format(prt)
def prGreen(prt): print "\033[92m {}\033[00m" .format(prt)
def prYellow(prt): print "\033[93m {}\033[00m" .format(prt)
def prLightPurple(prt): print "\033[94m {}\033[00m" .format(prt)
def prPurple(prt): print "\033[95m {}\033[00m" .format(prt)
def prCyan(prt): print "\033[96m {}\033[00m" .format(prt)
def prLightGray(prt): print "\033[97m {}\033[00m" .format(prt)
def prBlack(prt): print "\033[98m {}\033[00m" .format(prt)

line = ''
switch = 0
counter_line = 0
final_line = ''

for i in xrange(600000):
	len_line = len(line)
	if counter_line < 175 and switch == 0:
		counter_line += 1
		final_line = counter_line * '@'
	elif counter_line > 0:
		switch = 1
		counter_line -= 1
		final_line = counter_line * '@'
	else:
		switch = 0
	randint = random.randint(1, 5)
	sleep(.02)
	if randint == 1:
		prYellow(final_line)
	elif randint == 2:
		prGreen(final_line)
	elif randint == 3:
		prRed(final_line)
	elif randint == 4:
		prLightPurple(final_line)
	elif randint == 5:
		prCyan(final_line)