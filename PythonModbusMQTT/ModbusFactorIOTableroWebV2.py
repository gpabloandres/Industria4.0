import streamlit as st
from pymodbus.client import ModbusTcpClient
import time

# Crear una instancia del cliente Modbus TCP
PLC = ModbusTcpClient("127.0.0.1")

# Conectar al PLC
if not PLC.connect():
    st.error("Error al conectar con el PLC.")
    st.stop()

# Configurar la interfaz de Streamlit
st.set_page_config(page_title="Tablero de Control del PLC", layout="centered")
st.title("Tablero de Control del PLC")
st.markdown("---")

# Leer el estado del sensor en el input 0
result = PLC.read_discrete_inputs(0, 1, 1)

if result.isError():
    st.error("Error al leer el estado del sensor.")
    st.stop()

# Asignar a la variable el estado del sensor
sensor_state = result.bits[0]

# Mostrar el estado del sensor con colores indicativos
if sensor_state:
    st.success(f"Estado del sensor: ACTIVO")
else:
    st.error(f"Estado del sensor: INACTIVO")

st.markdown("---")

# Crear columnas para los botones de control
col1, col2 = st.columns(2)

# Botón ENCENDER
with col1:
    if st.button("ENCENDER", key="encender"):
        if sensor_state:
            PLC.write_coil(0, True, 1)
            st.success("¡Cinta en funcionamiento!")
        else:
            PLC.write_coil(0, False, 1)
            st.warning("¡Cinta parada - Caja al final de línea!")

# Botón APAGAR
with col2:
    if st.button("APAGAR", key="apagar"):
        PLC.write_coil(0, False, 1)
        st.success("¡Cinta parada!")

st.markdown("---")

# Información adicional o logs
with st.expander("Ver detalles del sistema"):
    st.write("Aquí puedes incluir información adicional, logs o cualquier otro detalle relevante.")

# Desconectar del PLC (este punto se alcanzará si hay un error)
PLC.close()
