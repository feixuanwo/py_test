#!/usr/bin/env python

from random import randint, choice
from string import lowercase
from sys import maxint
from time import ctime

doms = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randint(5, 10)):
	#dtint = randint(0, (maxint -1)/100)
	dtint = 111111111
	print dtint
	dtstr = ctime(111111111)
	print 'dtstr:%s' % dtstr
	shorter = randint(4, 7)
	print 'shorter: %d' % shorter
	em = ''
	for j in range(shorter):
		em += choice(lowercase)
	print 'em:%s' % em
	longer = randint(shorter, 12)
	dn = ''
	for j in range(longer):
		dn += choice(lowercase)
	print 'dn:%s' % dn
	
	print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms), dtint, shorter, longer)
