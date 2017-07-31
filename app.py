import modbus
#import mqtt_run
import threading

#threads = []
#t1 = threading.Thread(target=modbus.Writehdrg)
#threads.append(t1)
#t2 = threading.Thread(target=modbus.Readhdrg)
#threads.append(t2)

#if __name__ == "__main__":

    #for t in threads:
    #    t.setDaemon(True)
    #    t.start()
    
    #t.join()
if __name__ == "__main__":
    #1:mqttonline,else numble mqttoffline
    modbus.read_holding_registers(1)
    #modbus.Writehdrg()
