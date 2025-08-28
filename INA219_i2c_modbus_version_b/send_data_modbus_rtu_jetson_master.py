import smbus
import time
import os
import logging
import threading

# Import the Modbus CLIENT
from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException

# --- I2C Configuration ---
I2C_ADDR = 0x2d
LOW_VOL_SHUTDOWN = 3150  # mV

# --- Modbus Configuration ---
MODBUS_PORT = "/dev/serial0"  # Use the Pi's hardware serial port (TX/RX pins)
# This is the ID of the SLAVE device we want to write data TO.
TARGET_SLAVE_ID = 1

# --- Configure Logging (Good for debugging) ---
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

# --- Modbus Register Mapping ---
# We will write the I2C variables TO these holding register addresses on the slave.
# IMPORTANT: This map defines the order of data in the list we send.
REGISTER_MAP = {
    'charging_status': 0,
    'vbus_voltage': 1,
    'vbus_current': 2,
    'vbus_power': 3,
    'battery_voltage': 4,
    'battery_current': 5,
    'battery_percent': 6,
    'battery_capacity': 7,
    'empty_time': 8,
    'full_time': 9,
    'voltage_V1': 10,
    'voltage_V2': 11,
    'voltage_V3': 12,
    'voltage_V4': 13,
}
# The starting address for our block write will be the lowest value in the map.
START_ADDRESS = min(REGISTER_MAP.values())
# The number of registers we will write in a single block.
NUM_REGISTERS = len(REGISTER_MAP)


def main():
    """
    Main function to run the I2C reader and Modbus master loop.
    """
    log.info("Starting I2C to Modbus Master application...")
    bus = smbus.SMBus(1)
    low_voltage_counter = 0

    # --- Initialize Modbus Client ---
    # We create the client once and reuse the connection.
    client = ModbusSerialClient(
        port=MODBUS_PORT,
        baudrate=9600,
        timeout=1
    )

    while True:
        try:
            # --- 1. Read all data from the I2C sensor ---
            log.info("Reading new data from I2C sensor...")
            
            data = bus.read_i2c_block_data(I2C_ADDR, 0x02, 1)
            charging_status = data[0]

            data = bus.read_i2c_block_data(I2C_ADDR, 0x10, 6)
            vbus_voltage = data[0] | data[1] << 8
            vbus_current = data[2] | data[3] << 8
            vbus_power = data[4] | data[5] << 8

            data = bus.read_i2c_block_data(I2C_ADDR, 0x20, 12)
            battery_voltage = data[0] | data[1] << 8
            battery_current_raw = data[2] | data[3] << 8
            battery_percent = data[4] | data[5] << 8
            battery_capacity = data[6] | data[7] << 8
            empty_time = data[8] | data[9] << 8
            full_time = data[10] | data[11] << 8

            data = bus.read_i2c_block_data(I2C_ADDR, 0x30, 8)
            voltage_V1 = data[0] | data[1] << 8
            voltage_V2 = data[2] | data[3] << 8
            voltage_V3 = data[4] | data[5] << 8
            voltage_V4 = data[6] | data[7] << 8
            
            log.info(f"I2C Read successful: Battery at {battery_percent}%, Voltage: {battery_voltage}mV.")

            # --- 2. Assemble the data into a list for Modbus ---
            # The order MUST match the register map from START_ADDRESS upwards.
            values_to_write = [
                charging_status,
                vbus_voltage,
                vbus_current,
                vbus_power,
                battery_voltage,
                battery_current_raw, # Send the raw 16-bit value (two's complement)
                battery_percent,
                battery_capacity,
                empty_time,
                full_time,
                voltage_V1,
                voltage_V2,
                voltage_V3,
                voltage_V4
            ]

            # --- 3. Connect and write data to the Modbus Slave ---
            if not client.is_socket_open():
                log.info("Modbus client not connected. Attempting to connect...")
                client.connect()

            if client.is_socket_open():
                log.info(f"Writing {len(values_to_write)} registers to Slave ID {TARGET_SLAVE_ID} starting at address {START_ADDRESS}...")
                # Use function 16 (0x10) to write multiple registers
                response = client.write_registers(START_ADDRESS, values_to_write, slave=TARGET_SLAVE_ID)
                
                if response.isError():
                    log.error(f"Modbus Error writing registers: {response}")
                else:
                    log.info("Modbus write successful.")
            else:
                log.error("Failed to connect to Modbus serial port.")

            # --- Low Voltage Shutdown Logic ---
            battery_current_signed = battery_current_raw if battery_current_raw <= 0x7FFF else battery_current_raw - 0x10000
            is_low_voltage = (voltage_V1 < LOW_VOL_SHUTDOWN or voltage_V2 < LOW_VOL_SHUTDOWN or
                              voltage_V3 < LOW_VOL_SHUTDOWN or voltage_V4 < LOW_VOL_SHUTDOWN)

            if is_low_voltage and battery_current_signed < 50:
                low_voltage_counter += 1
                if low_voltage_counter >= 30:
                    log.warning("Critical low voltage. Shutting down now.")
                    # os.system("sudo poweroff")
                    break
                else:
                    log.warning(f"Low voltage detected! Shutdown in {60 - 2 * low_voltage_counter}s.")
            else:
                low_voltage_counter = 0

        except IOError as e:
            log.error(f"I/O Error communicating with I2C sensor at 0x{I2C_ADDR:02x}. Check connection. Error: {e}")
        except ModbusException as e:
            log.error(f"Modbus communication error: {e}")
            client.close() # Close connection on error
        except Exception as e:
            log.error(f"An unexpected error occurred: {e}")

        # Wait before the next cycle
        time.sleep(1)

    client.close()
    log.info("Application has stopped.")


# --- Main Execution ---
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log.info("Shutdown requested by user.")