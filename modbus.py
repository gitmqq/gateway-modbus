#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Pymodbus Synchronous Client Examples
--------------------------------------------------------------------------

The following is an example of how to use the synchronous modbus client
implementation from pymodbus.

It should be noted that the client can also be used with
the guard construct that is available in python 2.5 and up::

    with ModbusClient('192.168.0.107') as client:
        result = client.read_coils(1,10)
        print result
 '''

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)
#client = ModbusClient('192.168.0.107',port=502)
client = ModbusClient('192.168.0.105',retries=5,retry_on_empty=True)
import Data as data
import time
import json


client.connect()

def Write_holding_registers():
    print "---------------------------------------------------------------------------"
    log.debug("write to a holding register")
    print "---------------------------------------------------------------------------"
    #wc = client.write_coil(0,True,unit=1)
    addr = 40001
    for i in range(1,20):
        print "---------------------------------------------------------------------------"
        log.debug("write to a holding register")
        print "---------------------------------------------------------------------------"
        wh = client.write_register(addr,1)
        addr =addr + 1
        time.sleep(1)

def read_holding_registers(status):    
    print "---------------------------------------------------------------------------"
    log.debug("Reading holding register")
    print "---------------------------------------------------------------------------"

            #rr = client.read_coils(1,1,unit=0x01)
            #addr = 40001
    dConf = readConf("mqtt_data_conf.json")
    id = dConf[0]['ID']
    addr = dConf[0]['SAVEADDR']
    reg = dConf[0]['REG_QTY']
    t = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    print t
    dataobj = {
       'REG_VAL':{
            },
        'status':'1',
        'TIME':'0',
        'PHONE':'18049040679',
        'Flag':'Z',
        'ID':'0',
        }
    dataobj['TIME'] = t
    dataobj['ID'] = id
    start = 0
    for i in range(1,reg):
        print "---------------------------------------------------------------------------"
        log.debug("Reading holding register")
        print "---------------------------------------------------------------------------"
        rh = client.read_holding_registers(start,1,unit=1)
        print rh.registers[0]
        dataobj['REG_VAL'][360000+addr] = rh.registers[0]
        addr = addr + 1
        start = start + 1
    if status == 1:
        data.onlineDatahold([dataobj])
    else:
        dataobj['Flag'] = 'D'
        data.offlineDatahold(dataobj)

#dConf = readConf("mqtt_data_conf.json")
def Tdata(usersenddata):
    id = usersenddata[0]['ID']
    addr = usersenddata[0]['SAVEADDR']
    reg = usersenddata[0]['REG_QTY']
    t = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    dataobj = {
       'REG_VAL':{
            },
        'status':'1',
        'TIME':'0',
        'PHONE':'18049040679',
        'Flag':'T',
        'ID':'0',
        }
    dataobj['TIME'] = t
    dataobj['ID'] = id
    start = 0
    for i in range(1,reg):
        print "---------------------------------------------------------------------------"
        log.debug("Reading holding register")
        print "---------------------------------------------------------------------------"
        rh = client.read_holding_registers(start,1,unit=1)
        print rh.registers[0]
        dataobj['REG_VAL'][360000+addr] = rh.registers[0]
        addr = addr + 1
        start = start + 1

def  readConf(filepath):    
    fo = open(filepath, "r")
    line = fo.readline()
    conf = json.loads(line)
    print conf
    fo.close()
    return conf
