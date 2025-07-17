// I2C address of UPS HAT (E)
const int UPS_ADDRESS = 0x2D;

// Register addresses
const byte ID_REGISTER = 0x00;
const byte REBOOT_REGISTER = 0x01; 
const byte CHARGING_STATUS_REGISTER = 0x02;     // charging status
const byte COMM_REGISTER = 0x03;                // communication status
const byte VBUS_VOLTAGE_REGISTER = 0x10;        // VBUS voltage data (mV)
const byte VBUS_CURRENT_REGISTER = 0x12;        // VBUS current data (mA)
const byte VBUS_POWER_REGISTER = 0x14;          // VBUS power data (mW)
const byte VOLTAGE_REGISTER = 0x20;             // Battery total voltage (mV)
const byte CURRENT_REGISTER = 0x22;             // Battery current (mA)
const byte PERCENT_REGISTER = 0x24;             // Battery percent (%)
const byte REMAINING_CAPACITY_REGISTER = 0x26;  // Battery remaining capacity (mAh)
const byte REMAINING_DISCHARGE_REGISTER = 0x28; // Battery remaining discharge time
const byte REMAINING_CHARGE_REGISTER = 0x2a;    // Battery remaining charging time
const byte CELL1_VOLTAGE_REGISTER = 0x30;       // Voltage of cell 1 (mAh)
const byte CELL2_VOLTAGE_REGISTER = 0x32;       // Voltage of cell 2 (mAh)
const byte CELL3_VOLTAGE_REGISTER = 0x34;       // Voltage of cell 3 (mAh)
const byte CELL4_VOLTAGE_REGISTER = 0x36;       // Voltage of cell 4 (mAh)