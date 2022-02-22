#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author Vitorrio Brooks - Ahead
import collections
import datetime
import logging
import sys, time
import os
import requests, json

logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class TWBootStrap(object):
    def __init__(self):
        pass

    

    
    def add_tower_host(self, hostname, ansible_domain, ansible_token, inventory_id):
        headers = {'Authorization': 'Bearer ' + ansible_token, 'Content-Type': 'application/json'}
        url = 'https://' + ansible_domain + '/api/v2/inventories/' + inventory_id + '/hosts/'
        new_host = {"description":"TFE Server","name":hostname,"enabled":"True"}

       
        try:
            r = requests.post(url, headers=headers, data=json.dumps(new_host), verify=False)
        except StandardError as e:
            logging.error('Could not add new host to inventory for the following reason: ${0} '.format(e))
        return r
        

def main():
    #Pull tower domain, host name/IP and tower token from cmd options
    ansible_domain = sys.argv[1]
    hostname = sys.argv[2]
    ansible_token = sys.argv[3]
    inventory_id = sys.argv[4]
   
    boot_strapper = TWBootStrap()
    #Add hot to the configured inventory
    add_host_response = boot_strapper.add_tower_host(hostname, ansible_domain, ansible_token, inventory_id)
    print(add_host_response)

if __name__ == '__main__':
    main()

