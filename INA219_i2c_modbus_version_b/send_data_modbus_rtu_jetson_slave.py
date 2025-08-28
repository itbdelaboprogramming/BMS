import smbus
import time
import os
import logging
import threading

from pymodbus.server import StartSerialServer
from pymodbus.datastore import ModbusDeviceContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock

# --- I2C Configuration ---
I2C_ADDR = 0x2D
LOW_VOL_SHUTDOWN = 3150  # mV

# --- Modbus Configuration ---
MODBUS_PORT = "/dev/ttyTHS1"
MY_SLAVE_ID = 1

# --- Configure Logging (Good for debugging) ---
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

def i2c_data_updater(server_context):
    """
    This function runs in a separate thread. It continuously reads data
    from the I2C sensor and updates the Modbus datastore.
    The 'server_context' is the main ModbusServerContext object.
    """
    log.info("I2C Updater: Starting background thread...")
    bus = smbus.SMBus(7)
    low_voltage_counter = 0

    # Get a direct reference to the holding register block for our slave
    holding_register_block = server_context[MY_SLAVE_ID].store['h']

    while True:
        try:
            log.info("I2C Updater: Reading new data from sensor...")
            
            # --- Read Charging Status ---
            data = bus.read_i2c_block_data(I2C_ADDR, 0x02, 1)
            charging_status = data[0]
            # CORRECTED: Assign value directly to the .values list at the correct index
            holding_register_block.values[REGISTER_MAP['charging_status']] = charging_status

            # --- Read VBUS Data ---
            data = bus.read_i2c_block_data(I2C_ADDR, 0x10, 6)
            vbus_voltage = data[0] | data[1] << 8
            vbus_current = data[2] | data[3] << 8
            vbus_power = data[4] | data[5] << 8
            holding_register_block.values[REGISTER_MAP['vbus_voltage']] = vbus_voltage
            holding_register_block.values[REGISTER_MAP['vbus_current']] = vbus_current
            holding_register_block.values[REGISTER_MAP['vbus_power']] = vbus_power

            # --- Read Battery Data ---
            data = bus.read_i2c_block_data(I2C_ADDR, 0x20, 12)
            battery_voltage = data[0] | data[1] << 8
            battery_current = data[2] | data[3] << 8
            
            battery_percent = data[4] | data[5] << 8
            battery_capacity = data[6] | data[7] << 8
            empty_time = data[8] | data[9] << 8
            full_time = data[10] | data[11] << 8
            holding_register_block.values[REGISTER_MAP['battery_voltage']] = battery_voltage
            holding_register_block.values[REGISTER_MAP['battery_current']] = battery_current
            holding_register_block.values[REGISTER_MAP['battery_percent']] = battery_percent
            holding_register_block.values[REGISTER_MAP['battery_capacity']] = battery_capacity
            holding_register_block.values[REGISTER_MAP['empty_time']] = empty_time
            holding_register_block.values[REGISTER_MAP['full_time']] = full_time

            # --- Read Cell Voltages ---
            data = bus.read_i2c_block_data(I2C_ADDR, 0x30, 8)
            voltage_V1 = data[0] | data[1] << 8
            voltage_V2 = data[2] | data[3] << 8
            voltage_V3 = data[4] | data[5] << 8
            voltage_V4 = data[6] | data[7] << 8
            holding_register_block.values[REGISTER_MAP['voltage_V1']] = voltage_V1
            holding_register_block.values[REGISTER_MAP['voltage_V2']] = voltage_V2
            holding_register_block.values[REGISTER_MAP['voltage_V3']] = voltage_V3
            holding_register_block.values[REGISTER_MAP['voltage_V4']] = voltage_V4

            log.info(f"I2C Updater: Battery at {battery_percent}%, Voltage: {battery_voltage}mV. Modbus registers updated.")

            # --- Low Voltage Shutdown Logic ---
            is_low_voltage = (voltage_V1 < LOW_VOL_SHUTDOWN or voltage_V2 < LOW_VOL_SHUTDOWN or
                              voltage_V3 < LOW_VOL_SHUTDOWN or voltage_V4 < LOW_VOL_SHUTDOWN)

            if is_low_voltage and battery_current < 50:
                low_voltage_counter += 1
                if low_voltage_counter >= 30:
                    log.warning("I2C Updater: Critical low voltage. Shutting down now.")
                    # os.system("sudo poweroff")
                    break # Exit the loop to stop the thread
                else:
                    log.warning(f"I2C Updater: Low voltage detected! Shutdown in {60 - 2 * low_voltage_counter}s.")
            else:
                low_voltage_counter = 0

        except IOError as e:
            log.error(f"I2C Updater: I/O Error communicating with sensor at 0x{I2C_ADDR:02x}. Check connection. Error: {e}")
        except Exception as e:
            log.error(f"I2C Updater: An unexpected error occurred: {e}")

        # Wait before the next update cycle
        time.sleep(1)

    log.info("I2C Updater: Background thread has stopped.")

# --- Main Server Execution ---
if __name__ == '__main__':
    # --- 1. Initialize Modbus Data Store ---
    store = ModbusDeviceContext(
        hr=ModbusSequentialDataBlock(0, [0] * 100), # Holding Registers
        ir=ModbusSequentialDataBlock(0, [0] * 100), # Input Registers
        co=ModbusSequentialDataBlock(0, [0] * 100), # Coils
        di=ModbusSequentialDataBlock(0, [0] * 100)  # Discrete Inputs
    )
    context = ModbusServerContext(device_ids={MY_SLAVE_ID: store}, single=False)

    # --- 2. Create and Start the I2C Updater Thread ---
    updater_thread = threading.Thread(target=i2c_data_updater, args=(context,))
    updater_thread.daemon = True
    updater_thread.start()

    # --- 3. Start the Modbus Server (This will run forever) ---
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'RaspberryPi'
    identity.ProductCode = 'I2C-BMS-Bridge'
    identity.ModelName = 'Modbus RTU Slave'
    
    log.info(f"Modbus Server: Starting RTU Slave on {MODBUS_PORT} with ID {MY_SLAVE_ID}...")
    StartSerialServer(context=context,
                      identity=identity,
                      port=MODBUS_PORT,
                      timeout=1,
                      baudrate=9600)

