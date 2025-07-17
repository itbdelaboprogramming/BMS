import time
import logging
import threading
import struct
import os

from pymodbus.server import StartSerialServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock

# --- Modbus Configuration ---
MODBUS_PORT = 'COM12'
SLAVE_ID = 1

# --- Configure Logging ---
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

# --- Modbus Register Mapping ---
REGISTER_MAP = {
    'charging_status': 1,
    'vbus_voltage': 2,
    'vbus_current': 3,
    'vbus_power': 4,
    'battery_voltage': 5,
    'battery_current': 6,
    'battery_percent': 7,
    'battery_capacity': 8,
    'empty_time': 9,
    'full_time': 10,
    'voltage_V1': 11,
    'voltage_V2': 12,
    'voltage_V3': 13,
    'voltage_V4': 14,
}

def data_display_thread(server_context):
    """
    This function runs in a background thread to continuously read from the
    slave's own datastore and display the values.
    """
    log.info("Display Thread: Starting data display...")
    
    # Get a direct reference to the holding register block for our slave
    holding_register_block = server_context[SLAVE_ID].store['h']

    while True:
        try:
            # --- Read values directly from the datastore ---
            register_values = holding_register_block.values

            # --- Extract and interpret the data ---
            charging_status_raw = register_values[REGISTER_MAP['charging_status']]
            
            # Build the detailed status line based on bits in the status register.
            # NOTE: These bit interpretations are based on common battery ICs.
            # The exact meaning depends on the datasheet for your specific UPS HAT.
            
            # VBUS status (assuming bit 4 indicates VBUS is present)
            vbus_powered_str = "Powered" if charging_status_raw & 0x10 else "Not powered"

            # Charging status
            if charging_status_raw & 0x80: # Charging bit
                charging_str = "Charging"
                detail_str = "Fast Charging" if charging_status_raw & 0x40 else "Standard Charging"
            else:
                charging_str = "Not charging"
                detail_str = "Discharging" if charging_status_raw & 0x20 else "Standby"

            status_line = f"Charging Status: {charging_str} | VBUS: {vbus_powered_str} | Detail: {detail_str}"
            
            # Get all other values
            vbus_voltage = register_values[REGISTER_MAP['vbus_voltage']]
            vbus_current = register_values[REGISTER_MAP['vbus_current']]
            vbus_power = register_values[REGISTER_MAP['vbus_power']]
            battery_voltage = register_values[REGISTER_MAP['battery_voltage']]
            battery_percent = register_values[REGISTER_MAP['battery_percent']]
            battery_capacity = register_values[REGISTER_MAP['battery_capacity']]
            empty_time = register_values[REGISTER_MAP['empty_time']]
            full_time = register_values[REGISTER_MAP['full_time']]
            voltage_v1 = register_values[REGISTER_MAP['voltage_V1']]
            voltage_v2 = register_values[REGISTER_MAP['voltage_V2']]
            voltage_v3 = register_values[REGISTER_MAP['voltage_V3']]
            voltage_v4 = register_values[REGISTER_MAP['voltage_V4']]

            # Interpret the signed value for battery current
            battery_current_raw = register_values[REGISTER_MAP['battery_current']]
            battery_current_signed = battery_current_raw if battery_current_raw <= 0x7FFF else battery_current_raw - 0x10000

            # --- Print a clean, formatted output ---
            # Clear the console for a cleaner refresh
            os.system('cls' if os.name == 'nt' else 'clear') 
            
            print(status_line)
            print(f"VBUS Voltage\t\t: {vbus_voltage} mV")
            print(f"VBUS Current\t\t: {vbus_current} mA")
            print(f"VBUS Power\t\t: {vbus_power} mW")
            print(f"Battery Voltage\t\t: {battery_voltage} mV")
            print(f"Battery Current\t\t: {battery_current_signed} mA")
            print(f"Battery Percent\t\t: {battery_percent} %")
            print(f"Remaining Capacity\t: {battery_capacity} mAh")

            if battery_current_signed < 0:
                print(f"Time to Empty\t\t: {empty_time} min")
            else:
                print(f"Time to Full\t\t: {full_time} min")
            
            print(f"Cell Voltage 1\t\t: {voltage_v1} mV")
            print(f"Cell Voltage 2\t\t: {voltage_v2} mV")
            print(f"Cell Voltage 3\t\t: {voltage_v3} mV")
            print(f"Cell Voltage 4\t\t: {voltage_v4} mV")

        except IndexError:
            # This can happen on the first run before data arrives.
            log.warning("Display Thread: Data not yet available in registers. Waiting...")
        except Exception as e:
            log.error(f"Display Thread: An error occurred: {e}")
            
        # Wait before the next update
        time.sleep(2)


# --- Main Server Execution ---
if __name__ == '__main__':
    # --- 1. Initialize Modbus Data Store ---
    # We create a data store for our slave device.
    store = ModbusSlaveContext(
        hr=ModbusSequentialDataBlock(0, [0] * 100), # Holding Registers
        ir=ModbusSequentialDataBlock(0, [0] * 100), # Input Registers
        co=ModbusSequentialDataBlock(0, [0] * 100), # Coils
        di=ModbusSequentialDataBlock(0, [0] * 100)  # Discrete Inputs
    )
    context = ModbusServerContext(slaves={SLAVE_ID: store}, single=False)

    # --- 2. Create and Start the Data Display Thread ---
    display_thread = threading.Thread(target=data_display_thread, args=(context,))
    display_thread.daemon = True  # Allows the main program to exit
    display_thread.start()

    # --- 3. Start the Modbus Server (This will run forever in the main thread) ---
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'LaptopSlave'
    identity.ProductCode = 'LS'
    identity.ModelName = 'Python Modbus Slave'
    
    log.info(f"Starting Modbus RTU Slave on {MODBUS_PORT} with ID {SLAVE_ID}...")
    try:
        StartSerialServer(context=context,
                          identity=identity,
                          port=MODBUS_PORT,
                          timeout=1,
                          baudrate=9600)
    except Exception as e:
        log.error(f"Failed to start server on {MODBUS_PORT}. Is the port correct and available? Error: {e}")
