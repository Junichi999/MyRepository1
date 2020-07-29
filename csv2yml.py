#!/usr/bin/python

import csv
import yaml
in_file  = open('servers.csv', "r")
out_file = open('inventory.yml', "w")
items = []
linenum = 0

#def convert_to_yaml(line, counter):
def convert_to_yaml(line):
    item = { 
        'hostname': line[0],
        'ostype': line[1],
        'ipaddress': line[2]
    }
    items.append(item)

def header(line):
    item = 'all:'
    items.append(item)

try:
    reader = csv.reader(in_file)
    #next(reader) # skip headers
    for counter, line in enumerate(reader):
        if counter == 0 :
            header(line)
        else:
        #convert_to_yaml(line, counter)
            convert_to_yaml(line)
        #linenum++
    out_file.write( yaml.dump(items, default_flow_style=False) )

finally:
    in_file.close()
    out_file.close()