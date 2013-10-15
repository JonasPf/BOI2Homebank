"""
Copyright (c) 2013, Jonas Pfannschmidt
Licensed under the MIT license http://www.opensource.org/licenses/mit-license.php
"""

import csv
import sys
import datetime
import os.path

expected_header = ['Date', 'Details', 'Debit', 'Credit', 'Balance']

if len(sys.argv) == 1:
    print "USAGE: python boi2hb.py [FILENAME]"
    exit()

inputpath = sys.argv[1]
name, ext = os.path.splitext(inputpath)
outputpath = name + '_converted' + ext

assert not os.path.exists(outputpath), outputpath + ' already exists'

with open(outputpath, 'wb') as outputfile:
	with open(inputpath, 'r') as inputfile:
		csvreader = csv.reader(inputfile, delimiter=',')
		csvwriter = csv.writer(outputfile, delimiter=';')

		header = csvreader.next()
		assert expected_header == header, 'Invalid header'

		csvwriter.writerow(['Date','Paymode','Info','Payee','Memo','Amount','Category','Tags'])

		for inputrow in csvreader:
			date = datetime.datetime.strptime(inputrow[0], '%d/%m/%Y')
			memo = inputrow[1]

			if inputrow[2]:
				amount = '-' + inputrow[2]
			else:
				amount = inputrow[3]

			csvwriter.writerow([date.strftime('%m-%d-%y'), '', '', '', memo, amount, '', 'BOI'])