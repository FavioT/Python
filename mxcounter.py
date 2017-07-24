#!/usr/bin/python
# -*- coding: utf-8 -*-

#import break_file
import csv
import os

#break_file.main()

# Parsing Log
def cutMX(mx):
    substr = mx.split(" ")[0]
    return substr	

# Working the csv
with open('delivered.csv.0') as f:
#with open('head') as f:
    next(f)
    reader = csv.reader(f)
    mx = []
    
    for row in reader:
        extract = row[9]
        extract = cutMX(extract)
        
        mx.append(extract)
        
f.close()

# MX counter
contmx = {i:mx.count(i) for i in mx}

#print contmx

# Creating file output
fo = open('mx_data.out','w')
print >> fo, '\tMX:', '\t\t', 'Count:'
print >> fo, '\t----------------------------'
for i,j in contmx.iteritems():
    if j > 5:
        print >> fo,"\t", i, '\t', j        
f.close()
