from pymodbus.client import ModbusTcpClient
import time

PLC = ModbusTcpClient("127.0.0.1")
PLC.connect()

while True:
    
    print("-----TABLERO DE CONTROL----")
    print("ENCENDER (1)")
    print("APAGAR (0)")
    print("___________________________")
    
    opcion = int(input("Ingrese su opción: "))
    
    if opcion == 1:
        
        registro = PLC.write_coil(0,True,1)
        time.sleep(0.1)         
                
    elif opcion == 0:
        
        registro = PLC.write_coil(0,False,1)
        time.sleep(0.1)
        
    else:
        
        print("Opción incorrecta! Vuelvalo a intentar.")