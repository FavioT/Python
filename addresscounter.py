#!/usr/bin/python
# -*- coding: utf-8 -*-

# by Favio.

import csv
import re
import string

# Parsing Log
def cutAdmin(adm):
    substr = adm.split("@")[1]
    res = substr.split(".")[0]
    return res

i = 0
# Opening pmta delivered log
with open('delivered.csv.0','rb') as f:
#with open('head','rb') as f:
    next(f)	
    reader = csv.reader(f)	
    acct, onlyadr, onlyadm = [], [], []

    for row in reader:		
        admin = row[3]	
        res = cutAdmin(admin)		
        address = row[4]									
		
        # DON'T USE FOR NOW		 	
        # Creating dictionary	
        #dicc[i] = {address, res}	

        # Removing duplicates values
        acct.append([address, res])		
        #acc = [list(t) for t in set(tuple(element) for element in acct)]	
										
        i += 1
f.close()

# Asing address and admin in separate lists.
for index in range(len(acct)):
    onlyadr.append(acct[index][0])
    #onlyadm.append(acc[index][1])

# Address counter
contadr = {i:onlyadr.count(i) for i in onlyadr}
#contadm = {i:onlyadm.count(i) for i in onlyadm}

# Creating file output
fo = open('adr_data.out','w')
print >> fo, '\tCuenta:', '\t\t', 'Count:'
print >> fo, '\t----------------------------'
for i,j in contadr.iteritems():
    if j > 5:
        print >> fo,"\t", i, '\t', j        
f.close()

    

        
