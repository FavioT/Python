#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import chain, islice

def chunks(iterable, n):
   "chunks(ABCDE,2) => AB CD E"
   iterable = iter(iterable)
   while True:
       # store one line in memory,
       # chain it to an iterator on the rest of the chunk
       yield chain([next(iterable)], islice(iterable, n-1))

def main():
    l = 10*10**5
    file_large = 'delivered.csv'
    with open(file_large) as bigfile:
        for i, lines in enumerate(chunks(bigfile, l)):
            file_split = '{}.{}'.format(file_large, i)
            with open(file_split, 'w') as f:
                f.writelines(lines)

main()


