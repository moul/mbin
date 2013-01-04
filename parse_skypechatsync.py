#!/usr/bin/python
# from: https://raw.github.com/bitexploder/Misc/master/parse_skypechatsync.py

import sys

f = open(sys.argv[1], "r")

skype = f.read()

idx = 0
while True:
	start = skype.find("\x01\x03\x02", idx)
	end = skype.find("\x00", start)
	if start == -1 or end == -1:
		break
	print skype[start+3:end]
	idx = end
