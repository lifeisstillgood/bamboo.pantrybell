#!/usr/local/bin/python

"""
Simple, manual based process to rebuild rackspace non-nova (non
OpenStack) servers from images stored online

Basically Rackspace offer an API set of calls, and I am using them -
but I have laready imaged my servers (Ubuntu 12.04 LTS, with ssh keys
added in)

Patching

weekly: apt-get update && apt-get upgrade
Then re-image...


1. get_auth - retrieves the current token for use in all calls
2. 


"""


import requests
import sys
import json 
from rhaptos2.common import conf
confd = conf.get_config("pantrybell")

APIURL='https://lon.auth.api.rackspacecloud.com/v1.0'

class RackspaceMgmtError(Exception):
    pass

def get_auth():

    hdrs = {"X-Auth-Key": confd['pantrybell_rackspace_api_key'],
            "X-Auth-User": 'pbrian'
           }

    r = requests.get(APIURL, headers=hdrs)
    results = []
    if r.status_code == 401: raise RackspaceMgmtError("Failed AUthorisation")
    l = ['x-server-management-url', 'x-auth-token']
    for k in l:
        results.append(r.headers[k])
    return results




proxy_dict = None

def discover_images():

    r = requests.get(mgmtURL + "/servers", headers=hdrs)
    j = json.loads(r.text)
    for svr in j['servers']:
        print svr['id'], svr['name']

    r = requests.get(mgmtURL + "/images", headers=hdrs)
    j = json.loads(r.text)
    for svr in j['images']:
        print svr['id'], svr['name']


def rebuild_server(imageid, serverid, authtoken, mgmtURL, hdrs):


    hdrs = {"X-Auth-Token": authtoken,
            "Content-Type": "application/json"
            }


    json = """{
              "rebuild" : {
              "imageId" : %s
              }
              }""" % imageid

    payload = json
    r = requests.post(mgmtURL + "/servers/%s/action" % serverid, 
                      data=payload, 
                      proxies=proxy_dict, 
                      headers=hdrs)    
    print r
    print r.headers
    print r.text


# from novaclient.v1_1 import client
# nt = client.Client('pbrian', 
#                    confd[''], 
#                    '10017816', 
#                    'https://lon.identity.api.rackspacecloud.com/v2.0', 
#                     service_type="compute")
# print nt.servers.list()


def reimage_server(servername):
    """ """

    mgmtURL, authtoken =  get_auth()
    hdrs = {"X-Auth-Token": authtoken}

    #discover_images()    
    #sys.exit() 
    detail= { #name:(imageid,serverid)
    "bare-server-jenkins": ("11251010","10158867"),
    "www-baseserver": ("11313960","10148905"),
    "bare-server-log":("11318780","10158866") 
    }

    if servername not in detail.keys():
        raise RackspaceMgmtError("Unknown server ref (%s) passed in to reimage" % servername)

    imageid, serverid = detail[servername]
    print rebuild_server(imageid, serverid, authtoken, mgmtURL, hdrs)
    


if __name__ == '__main__':
    mgmtURL, authtoken =  get_auth()
    hdrs = {"X-Auth-Token": authtoken}
    r = discover_images()

