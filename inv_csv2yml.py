#!/usr/bin/python
# <STDIN> utf-8.csv : ostype,hostname,ipaddress,tier (no BOM/ascii only)
#  ostype = { aix, linux, windows }
#  tier = { production, maint, dev, dr }
# <STDOUT> inventory yaml
#
import sys
import yaml
import csv

aix_list = {}
linux_list = {}
windows_list ={}
grp_aix = {}
grp_linux = {}
grp_windows = {}
reader = csv.DictReader(sys.stdin)
tier = 'prod' 
for row in reader:
    if row['tier'] != 'production':
        row['hostname'] = row['hostname']+'.'+row['tier']
    vars = { 'ipaddress':row['ipaddress'], 'ansible_host': row['ipaddress']}
    if row['ostype'] == 'aix':
        aix_list[row['hostname']] = vars 
        tier = row['tier']
    elif row['ostype'] == 'linux':
        linux_list[row['hostname']] = vars 
        tier = row['tier']
    elif row['ostype'] == 'windows':
        windows_list[row['hostname']] = vars 
        tier = row['tier']

grp_aix['vars'] = {'ostype': 'aix'} 
grp_aix['hosts'] = aix_list
grp_linux['vars'] = {'ostype': 'linux'} 
grp_linux['hosts'] = linux_list
grp_windows['vars'] = {'ostype': 'windows'} 
grp_windows['hosts'] = windows_list
groups = {'grp_aix': grp_aix, 'grp_linux': grp_linux, 'grp_windows': grp_windows}
childrens = {'children':groups}
childrens['vars'] = {'tier': tier}
all = {'all':childrens}
sys.stdout.write( yaml.dump(all, default_flow_style=False) )
