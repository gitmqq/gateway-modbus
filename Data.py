from jsonDb.database import JSONDB
import json

myDb = JSONDB('USER_DB')

def onlineDatahold(rs):
    myDb.insert('msg',rs)
    rc = myDb.find('msg')
    value = json.dumps(rc)
    print value

def TDatahold(Tdata)：
    myDb.insert('Tdata',Tdata)
    

#def sendData():
#    rc = myDb.find('msg',{'id':1})
#    myDb.delete('msg')
#    return rc

def offlineDatahold(data):
    jsObj = json.dumps(data)
    writefile = open('./data.json','a')
    writefile.write(jsObj)
    writefile.write('\n')
    writefile.close()

def sendofflineData():
    file_read = open('data.db','r+')
    while 1:
        line = file_read.readline()
        if not line:
            break
        pub = json.dumps(line)
        client.publish(dConf["TOPIC"],pub,0)
    file_read.truncate() #文件清空函数
    file_read.close()

def jugement(status):
    if status == "online":
        onlineDatahold()
    else :
        offlineDatahold()       
