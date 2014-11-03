#! /usr/bin/python

import re
import string
import os

burn_1 = 'make telosb install.'
burn_2 = ' bsl,/dev/ttyUSB'

for i in range(0, 4):
	NODEid = str(i)
	USBid = str(i)
	burn = burn_1 + NODEid + burn_2 + USBid
	os.system(burn)
	print '-----------------------\n' + 'NODE %d '%(i) + 'burned!!\n' + '----------------------'
