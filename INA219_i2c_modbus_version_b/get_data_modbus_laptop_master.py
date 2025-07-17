import time
import logging
import os

# Import the Modbus CLIENT
from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException

# --- Modbus Configuration ---
# !!! IMPORTANT: CHANGE THIS TO YOUR LAPTOP'S COM PORT !!!
MODBUS_PORT = 'COM12'  # For Windows. On Linux/macOS, it might be '/dev/ttyUSB0'
# This is the ID of the SLAVE device (your Raspberry Pi) we want to read from.
SLAVE_ID_TO_READ = 1

# --- Configure Logging ---
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

# --- Modbus Register Mapping ---
# This MUST match the map in the Raspberry Pi slave script.
# It defines how we will interpret the list of registers we receive.
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

# We will read one large block starting from the lowest address.
START_ADDRESS = min(REGISTER_MAP.values())
NUM_REGISTERS = len(REGISTER_MAP)

def main():
    """
    Main function to run the Modbus master polling loop.
    """
    log.info("Starting Modbus Master application...")

    # --- Initialize Modbus Client ---
    client = ModbusSerialClient(
        port=MODBUS_PORT,
        baudrate=9600,
        timeout=1
    )

    while True:
        try:
            # --- 1. Connect to the serial port ---
            if not client.is_socket_open():
                log.info(f"Connecting to {MODBUS_PORT}...")
                client.connect()

            if not client.is_socket_open():
                log.error("Failed to connect to serial port. Retrying in 5 seconds...")
                time.sleep(5)
                continue

            # --- 2. Read a block of registers from the slave ---
            log.info(f"Reading {NUM_REGISTERS} registers from Slave {SLAVE_ID_TO_READ} starting at address {START_ADDRESS}...")
            
            response = client.read_holding_registers(
                address=START_ADDRESS,
                count=NUM_REGISTERS,
                slave=SLAVE_ID_TO_READ
            )

            if response.isError():
                log.error(f"Modbus Error reading registers: {response}")
            elif not response.registers:
                log.warning("No data received in response.")
            else:
                # --- 3. Parse and display the received data ---
                register_values = response.registers
                
                # The received list is 0-indexed, but our map starts at 1.
                # We adjust by subtracting the START_ADDRESS.
                charging_status_raw = register_values[REGISTER_MAP['charging_status'] - START_ADDRESS]
                
                vbus_powered_str = "Powered" if charging_status_raw & 0x10 else "Not powered"
                if charging_status_raw & 0x80:
                    charging_str = "Charging"
                    detail_str = "Fast Charging" if charging_status_raw & 0x40 else "Standard Charging"
                else:
                    charging_str = "Not charging"
                    detail_str = "Discharging" if charging_status_raw & 0x20 else "Standby"
                
                status_line = f"Charging Status: {charging_str} | VBUS: {vbus_powered_str} | Detail: {detail_str}"
                
                vbus_voltage = register_values[REGISTER_MAP['vbus_voltage'] - START_ADDRESS]
                vbus_current = register_values[REGISTER_MAP['vbus_current'] - START_ADDRESS]
                vbus_power = register_values[REGISTER_MAP['vbus_power'] - START_ADDRESS]
                battery_voltage = register_values[REGISTER_MAP['battery_voltage'] - START_ADDRESS]
                battery_percent = register_values[REGISTER_MAP['battery_percent'] - START_ADDRESS]
                battery_capacity = register_values[REGISTER_MAP['battery_capacity'] - START_ADDRESS]
                empty_time = register_values[REGISTER_MAP['empty_time'] - START_ADDRESS]
                full_time = register_values[REGISTER_MAP['full_time'] - START_ADDRESS]
                voltage_v1 = register_values[REGISTER_MAP['voltage_V1'] - START_ADDRESS]
                voltage_v2 = register_values[REGISTER_MAP['voltage_V2'] - START_ADDRESS]
                voltage_v3 = register_values[REGISTER_MAP['voltage_V3'] - START_ADDRESS]
                voltage_v4 = register_values[REGISTER_MAP['voltage_V4'] - START_ADDRESS]

                battery_current_raw = register_values[REGISTER_MAP['battery_current'] - START_ADDRESS]
                battery_current_signed = battery_current_raw if battery_current_raw <= 0x7FFF else battery_current_raw - 0x10000

                # --- Print a clean, formatted output ---
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

        except ModbusException as e:
            log.error(f"Modbus communication error: {e}")
            client.close()
        except Exception as e:
            log.error(f"An unexpected error occurred: {e}")
            client.close()

        # Wait before the next poll
        time.sleep(2)

    client.close()
    log.info("Master application has stopped.")

# --- Main Execution ---
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log.info("Shutdown requested by user.")
