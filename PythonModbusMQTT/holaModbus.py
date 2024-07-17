from pymodbus.client import ModbusTcpClient
import time
cliente = ModbusTcpClient("192.168.5.20")

# Comandos posibles:
# Lectura ---
# cliente.read_coils(direccion,cantidad)
# cliente.read_discrete_inputs(direccion,cantidad)
# cliente.read_input_registers(direccion,cantidad)
# cliente.read_holding_registers(direccion,cantidad)
# Escritura ---
# cliente.write_coil(direccion,valor)
# cliente.write_register(direccion,cantidad)

cliente.connect()
try:
    while True:
        cliente.write_coil(1,True)
        time.sleep(0.5)
        cliente.write_coil(1,False)
        time.sleep(0.5)

except KeyboardInterrupt:
    cliente.close()