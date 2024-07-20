from pymodbus.client import ModbusTcpClient
import time

# Crear una instancia del cliente Modbus TCP
PLC = ModbusTcpClient("192.168.1.17")

# Conectar al PLC
PLC.connect()

# Bucle infinito
while True:
 
    # Leer el estado del sensor en el input 0
    result = PLC.read_discrete_inputs(0,1,1)

    # Asignar a la variable el estado del sensor
    sensor_state = result.bits[0]
    print(f"Estado del sensor: {sensor_state}")

    # Mostrar menú de ENCENDIDO Y PARADA de la cinta
    print("-----TABLERO DE CONTROL----")
    print("ENCENDER (1)")
    print("APAGAR (0)")
    print("---------------------------")
    
    # Leer la opción del usuario
    opcion = input("Ingrese su opción: ")
    
    # Ejecutar la opción del usuario
    if opcion == "1" and sensor_state == True:
        
        PLC.write_coil(0, True, 1)
        print("¡Cinta en funcionamiento!")
    
    elif opcion == "1" and sensor_state == False:
        
        PLC.write_coil(0, False, 1)
        print("¡Cinta parada - Caja al final de línea!")
    
    elif opcion == "0":
        
        PLC.write_coil(0, False, 1)
        print("¡Cinta parada!")
    
    else:
        print("Opción incorrecta! Vuelva a intentarlo.")
    
    # Esperar un momento antes de la siguiente iteración
    time.sleep(0.1)
    
# Desconectar del PLC
PLC.close()