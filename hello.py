#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"a test hello modle"

__author__="honeybee"

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print("hello world")
	elif len(args) == 2:
		print("fuck you, %s!" % args[1])
	else:
		print("ass ♂ we can ~~")

if __name__ == '__main__':
	test()