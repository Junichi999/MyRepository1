#!/usr/bin/python

import yaml

def make_yaml_file():
    data = { 'all': 
        { 'children':
          { 'ene_grp_cred_linux':
            { 'children':
              { 'grp_linux':
                { 'hosts': 
                  { 
                    'host001': {'ostype': 'linux', 'ipaddress': '10.1.1.1', 'ansible_ip': '10.1.1.1' },
                    'host002': {'ostype': 'linux', 'ipaddress': '10.1.1.2', 'ansible_ip': '10.1.1.2' },
                  }
                },
                'grp_aix':
                { 'hosts':
                   {
                      'host003': {'ostype': 'aix', 'ipaddress': '10.1.1.3', 'ansible_ip': '10.1.1.3' },
                   }
                }
              }
            }
          }
        }
      }
    with open('hosts.yml', 'wt') as f:
        f.write(yaml.dump(data, default_flow_style=False))

if __name__ == '__main__':
    make_yaml_file()
