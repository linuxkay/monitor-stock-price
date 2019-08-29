#!/usr/biin/pyrhon2.7
import urllib
import re

symbolfile = open("symbols.txt")

symbolslist = symbolfile.read()


newsymbolslist = symbolslist.split("\n")

i=0
while i<len(newsymbolslist):
	url = "http://finance.yahoo.com/q?s=" +newsymbolslist[i] + ""
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	print "the price of",newsymbolslist[i]," is " ,price
	i+=1
