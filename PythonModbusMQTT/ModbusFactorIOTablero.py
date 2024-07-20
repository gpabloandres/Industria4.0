from pymodbus.client import ModbusTcpClient
import time

# Crear una instancia del cliente Modbus TCP
PLC = ModbusTcpClient("192.168.1.17")

# Conectar al PLC
PLC.connect()

# Bucle infinito
while True:
    
    # Leer el estado del botón de arranque en el input 0
    start_button = PLC.read_discrete_inputs(0,1,1)
    
    # Leer el estado del botón de parada en el input 1
    stop_button = PLC.read_discrete_inputs(1,1,1)
    
    # Leer el estado del sensor de fin de cinta en el input 2
    sensor = PLC.read_discrete_inputs(2,1,1)
   
    # Asignar a una variable el estado del botón de arranque e imprimir
    start_button_state = start_button.bits[0]
    
    # Asignar a una variable el estado del botón de parada e imprimir
    stop_button_state = stop_button.bits[0]
    
    # Asignar a una variable al estado del sensor de fin de cinta e imprimir
    sensor_state = sensor.bits[0]
    
    if start_button_state == True and sensor_state == True:
        
        PLC.write_coil(0,True,1)
        print(f"¡Botón de arranque activado {start_button_state} - Cinta en funcionamiento!")
        time.sleep(0.5)         
                
    if stop_button_state == True or sensor_state == False:
        
        PLC.write_coil(0,False,1)
        PLC.write_coil(1,True,1)
        print(f"¡Estado de botón de parada/sensor de parada: {stop_button_state}/{sensor_state} - Cinta se detuvo!")
        time.sleep(0.5)