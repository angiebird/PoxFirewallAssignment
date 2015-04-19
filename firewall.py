'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 4 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from pox.lib.addresses import IPAddr
from collections import namedtuple
import os
''' Add your imports here ... '''



log = core.getLogger()
policyFile = "%s/pox/firewall-policies.csv" % os.environ[ 'HOME' ]  

''' Add your global variables here ... '''
#read policy file and save it as a dictionary
blockLs = []
fp = open(policyFile)
line = fp.readline() #ignore first line
line = fp.readline()
while line:
    item = line.split(',')
    item[0] = int(item[0])
    item[2] = item[2].strip() #remove white space
    blockLs.append(item)
    print item[0], item[1], item[2]
    line = fp.readline()
fp.close()



class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):    
        ''' Add your logic here ... '''
        #get mac of current host
        connection = event.connection
        for item in blockLs:
            print item[1]
            print item[2]
            connection.send( of.ofp_flow_mod(  match=of.ofp_match( dl_src=EthAddr(item[1]), dl_dst=EthAddr(item[2])))) 
            connection.send( of.ofp_flow_mod(  match=of.ofp_match( dl_src=EthAddr(item[2]), dl_dst=EthAddr(item[1])))) 
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)
