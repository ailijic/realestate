# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 08:16:34 2015

@author: ailij_000

TODO:
- Find file to import
- switch csv to tab delimited
- read in headers
- put data into dictionary
- create sqllite db
- check sql db
- read from sql db
- write to sql db
- import data
"""

import csv as csv
import sqlite3 as sql

def open_file():
    # NEXT: count number of items in each row, 
        # make sure each row has correct number of columns
    with open('mls_dataset_brdentown.txt', 'r') as f:
        #reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        reader = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        import itertools
        '''        
        for row in itertools.islice(reader, 2):
            print(row)
        '''
        for row in reader:#itertools.islice(reader, 1):
             print(row['first_name'], row['last_name'])
        
    return True
open_file()    
