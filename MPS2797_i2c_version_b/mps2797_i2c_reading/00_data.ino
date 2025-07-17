/****************************************************************
 * MP2797 Register Map
 * This file contains the register addresses for the
 * Monolithic Power Systems (MPS) MP2797 BMS chip.
 *
 * All information is based on datasheet Rev. 1.0, 6/28/2023.
 ****************************************************************/

// The default I2C slave address for the MP2797.
// Note: This can be changed by writing to the DEVICE_ADD field in register 0xA3.
const int MPS_ADDRESS = 0x01;

// --- Register Addresses ---

// --- Cell Configuration ---
const byte CELLS_CTRL = 0x00;           // Sets the number of battery cells in use (7 to 16). [cite: 1627]

// --- IC State Control ---
const byte PWR_STATUS = 0x01;           // READ-ONLY: Reports the chip's power state (Safe, Standby, Active, Fault) and current direction (Charging/Discharging). [cite: 1629]
const byte STB_STATUS = 0x02;           // READ-ONLY: Reports standby mode status and PACKP pin voltage comparison results. [cite: 1637]
const byte LOAD_CHARGER_STATUS = 0x03;  // READ-ONLY: Reports the status of automatic load and charger plug-in detection. [cite: 1637]
const byte ACT_CFG = 0x05;              // Configures the source (GPIO or register) and logic (Simple or Direct) for turning on the main protection MOSFETs. [cite: 1644]
const byte STB_CFG = 0x06;              // Configures standby mode, including current thresholds and monitoring intervals. [cite: 1652]
const byte SAFE_CFG = 0x07;             // Configures options for safe mode, like enabling protection monitoring while in safe mode. [cite: 1652, 1660]
const byte RGL_CFG = 0x08;              // Configures the 3.3V regulator's behavior during shutdown mode. [cite: 1660]
const byte LOAD_CHARGER_CFG = 0x09;     // Configures and enables load/charger detection and the PACKP comparator. [cite: 1660, 1672]

// --- Pins and GPIO ---
const byte GPIO_STATUS = 0x0A;          // READ-ONLY: Reports the high/low logic status of the GPIO pins. [cite: 1669]
const byte GPIO_OUT = 0x0B;             // Sets the desired output level (high/low) for GPIO pins when they are configured as outputs. [cite: 1669]
const byte GPIO_CFG = 0x0C;             // Configures each GPIO's direction (input/output), type (digital/analog), and pull-up resistor status. [cite: 1669, 1685]
const byte PINS_CFG = 0x0D;             // Configures special pin functions, like the polarity of the XALERT pin and behavior of the WDT pin. [cite: 1685]

// --- Watchdog ---
const byte WDT_STATUS = 0x0E;           // READ-ONLY: Reports the status of the watchdog timer (e.g., if a "bark" or "bite" event has occurred). [cite: 1687]
const byte WDT_RST = 0x0F;              // WRITE-ONLY: Writing to this register resets the watchdog timer to prevent a timeout. [cite: 1694]
const byte WDT_CFG = 0x10;              // Configures the watchdog timer, including enabling it and setting the timeout intervals for "bark" and "bite" events. [cite: 1694]

// --- MOSFET Driver ---
const byte FET_STATUS = 0x11;           // READ-ONLY: Reports the on/off status of the Charge (CHG), Discharge (DSG), and Standby (SBYDSG) MOSFET drivers. [cite: 1697]
const byte FET_CTRL = 0x12;             // Controls the standby P-channel MOSFET driver manually. [cite: 1697]
const byte FET_MODE = 0x13;             // Enables/disables soft-start for CHG and DSG FETs and sets turn-on timeout behavior. [cite: 1697, 1704]
const byte FET_CFG = 0x14;              // Configures the details of the MOSFET drivers, such as the DSG soft-start slope and the gate drive voltage level. [cite: 1704, 1712]

// --- Interrupt ---
const byte RD_INT0 = 0x15;              // READ-ONLY: Main interrupt status register, reports combined flags for major events like OV, UV, Over-Current, etc. [cite: 1715, 1722]
const byte RD_INT1 = 0x16;              // READ-ONLY: Secondary interrupt status register, reports flags for events like diagnostics, balancing, and driver errors. [cite: 1729, 1736]
const byte INT0_CLR = 0x17;             // WRITE-ONLY: Writing to the bits in this register clears the corresponding main interrupt status flags in RD_INT0. [cite: 1736, 1743]
const byte INT1_CLR = 0x18;             // WRITE-ONLY: Writing to the bits in this register clears the corresponding secondary interrupt status flags in RD_INT1. [cite: 1743, 1750]
const byte INT0_EN = 0x19;              // Enables or disables each specific interrupt source for the main interrupt register (RD_INT0). [cite: 1750, 1758]
const byte INT1_EN = 0x1A;              // Enables or disables each specific interrupt source for the secondary interrupt register (RD_INT1). [cite: 1758, 1765]
const byte INT_TYPE0 = 0x1B;            // Configures the trigger type (level, rising/falling edge) for VTOP and NTC interrupts. [cite: 1765]
const byte INT_TYPE1 = 0x1C;            // Configures the trigger type for REGIN, 3V3, and VDD UV interrupts. [cite: 1772]
const byte INT_TYPE2 = 0x1D;            // Configures the trigger type for dead cell, mismatch, die temp, and other interrupts. [cite: 1772, 1779]
const byte MASK_INT0 = 0x1E;            // Masks (temporarily ignores) specific main interrupts without disabling them. [cite: 1779, 1786]
const byte MASK_INT1 = 0x1F;            // Masks (temporarily ignores) specific secondary interrupts without disabling them. [cite: 1786, 1793]

// --- Over-Current Protection (OCP) ---
const byte OC_STATUS = 0x20;            // READ-ONLY: Reports latched and real-time status for discharge and charge over-current events. [cite: 1795, 1803]
const byte OCFT_CTRL = 0x23;            // Configures OCP: enables monitoring, enables fault triggering, and sets interrupt types for over-current events. [cite: 1803, 1809]
const byte DSGOC_LIM = 0x24;            // Sets the voltage thresholds and measurement ranges for Discharge Over-Current Protection (both OC1 and OC2). [cite: 1817]
const byte DSGOC_DEG = 0x25;            // Sets the deglitch times (how long an over-current condition must persist) for Discharge OCP. [cite: 1824]
const byte CHGOC_DEG = 0x26;            // Sets the threshold, range, and deglitch time for Charge Over-Current Protection. [cite: 1824, 1831]

// --- Short-Circuit Protection (SCP) ---
const byte SC_STATUS = 0x27;            // READ-ONLY: Reports latched and real-time status for discharge and charge short-circuit events. [cite: 1832, 1840]
const byte SCFT_CTRL = 0x2A;            // Configures SCP: enables monitoring, enables fault triggering, and sets interrupt types for short-circuit events. [cite: 1840, 1849]
const byte DSGSC_CFG = 0x2B;            // Configures the limit, range, and deglitch time for Discharge Short-Circuit Protection. [cite: 1849]
const byte CHGSC_CFG = 0x2C;            // Configures the limit, range, and deglitch time for Charge Short-Circuit Protection. [cite: 1856]

// --- Over-Voltage (OV), Under-Voltage (UV), Dead Cell, and Mismatched Cell Protections ---
const byte RD_CELL_UV = 0x2D;           // READ-ONLY: Reports which individual cells are in an under-voltage (UV) condition. [cite: 1856, 1866]
const byte RD_CELL_OV = 0x2E;           // READ-ONLY: Reports which individual cells are in an over-voltage (OV) condition. [cite: 1873, 1880]
const byte RD_CELL_MSMT = 0x2F;         // READ-ONLY: Reports which individual cells have a voltage mismatch compared to the others. [cite: 1880, 1886]
const byte RD_CELL_DEAD = 0x30;         // READ-ONLY: Reports which individual cells have dropped below the "dead cell" threshold. [cite: 1894, 1903]
const byte CELL_MSMT_STS = 0x33;        // READ-ONLY: Reports the voltage difference between the highest and lowest cells. [cite: 1910, 1918]
const byte PACKFT_CTRL = 0x34;          // Enables monitoring and fault triggering for the entire pack (VTOP OV/UV, Dead Cell, Mismatch). [cite: 1918, 1923]
const byte CELLFT_CTRL = 0x35;          // Enables monitoring and fault triggering for individual cell OV/UV protections. [cite: 1923, 1932]
const byte CELL_HYST = 0x36;            // Sets the voltage hysteresis for cell UV and OV recovery. [cite: 1932]
const byte PACK_UV_OV = 0x37;           // READ-ONLY status of VTOP UV/OV conditions; also used to set the VTOP hysteresis values. [cite: 1932]
const byte CELL_UV = 0x38;              // Sets the specific voltage threshold and deglitch counter for cell under-voltage protection. [cite: 1932]
const byte CELL_OV = 0x39;              // Sets the specific voltage threshold and deglitch counter for cell over-voltage protection. [cite: 1941]
const byte PACK_UV = 0x3A;              // Sets the specific voltage threshold and deglitch counter for pack (VTOP) under-voltage protection. [cite: 1941]
const byte PACK_OV = 0x3B;              // Sets the specific voltage threshold and deglitch counter for pack (VTOP) over-voltage protection. [cite: 1941]
const byte CELL_DEAD_THR = 0x3C;        // Sets the voltage threshold and deglitch counter for dead cell detection. [cite: 1941, 1948]
const byte CELL_MSMT = 0x3D;            // Sets the voltage difference threshold and deglitch counter for cell mismatch detection. [cite: 1948]

// --- NTC and Die Temperature Protection ---
const byte RD_NTC_DIE = 0x3E;           // READ-ONLY: Reports status for NTC hot/cold events and die over-temperature events. [cite: 1951, 1958, 1966, 1972, 1980, 1989]
const byte RD_V_NTC4_LR = 0x3F;         // READ-ONLY: Reports the ADC voltage reading for NTC4 thermistor. [cite: 1989, 1997]
const byte RD_V_NTC3_LR = 0x40;         // READ-ONLY: Reports the ADC voltage reading for NTC3 thermistor. [cite: 1997]
const byte RD_V_NTC2_LR = 0x41;         // READ-ONLY: Reports the ADC voltage reading for NTC2 thermistor. [cite: 1997]
const byte RD_V_NTC1_LR = 0x42;         // READ-ONLY: Reports the ADC voltage reading for NTC1 thermistor. [cite: 1997]
const byte RD_T_DIE = 0x43;             // READ-ONLY: Reports the internal die temperature ADC reading (convertible to °C). [cite: 2003]
const byte NTC_CLR = 0x44;              // WRITE-ONLY: Clears die temperature fault flags. [cite: 2003]
const byte DIE_CFG = 0x46;              // Configures the digital die temperature protection (enables sensor and fault triggering). [cite: 2003]
const byte NTC_CFG = 0x47;              // Enables and configures each of the 4 NTC inputs (e.g., for cell or PCB monitoring). [cite: 2003, 2011]
const byte NTCC_OTHR_DSG = 0x48;        // Sets the NTC hot threshold for cell monitoring during DISCHARGE. [cite: 2011]
const byte NTCC_UTHR_DSG = 0x49;        // Sets the NTC cold threshold for cell monitoring during DISCHARGE. [cite: 2011]
const byte NTCC_OTHR_CHG = 0x4A;        // Sets the NTC hot threshold for cell monitoring during CHARGE. [cite: 2011]
const byte NTCC_UTHR_CHG = 0x4B;        // Sets the NTC cold threshold for cell monitoring during CHARGE and the hysteresis value. [cite: 2019]
const byte NTCM_OTHR = 0x4C;            // Sets the NTC hot threshold and hysteresis for NTCs configured in PCB monitor mode. [cite: 2019]
const byte DIE_OT = 0x4D;               // Sets the digital die over-temperature threshold and its hysteresis value. [cite: 2019]

// --- Diagnosis ---
const byte SELF_STS = 0x4E;             // READ-ONLY: Reports status of self-tests (ADC, regulators) and OTP CRC check outcome. [cite: 2021, 2029]
const byte RD_VA1P8 = 0x4F;             // READ-ONLY: ADC reading for the internal 1.8V VDD regulator. [cite: 2029]
const byte RD_VA3P3 = 0x50;             // READ-ONLY: ADC reading for the internal 3.3V regulator. [cite: 2029]
const byte RD_VA5 = 0x51;               // READ-ONLY: ADC reading for the 5V REGIN regulator. [cite: 2029]
const byte RD_VASELF = 0x52;            // READ-ONLY: ADC reading for the internal fixed voltage reference used for self-testing. [cite: 2029]
const byte RD_OPENH = 0x53;             // READ-ONLY: Reports open-wire status for cells 0-15. [cite: 2029, 2036]
const byte RD_OPENL = 0x54;             // READ-ONLY: Reports open-wire status for cell 16. [cite: 2036]
const byte SFT_GO = 0x55;               // Command register to start an OTP CRC check or an open-wire check. [cite: 2036, 2044]
const byte SELF_CFG = 0x56;             // Enables/disables various diagnostic checks like regulator monitoring, ADC self-test, and OTP CRC. [cite: 2044]
const byte OPEN_CFG = 0x57;             // Configures the open-wire detection parameters (timing and voltage threshold). [cite: 2045, 2049]
const byte REGIN_UV = 0x58;             // Sets the under-voltage threshold for the REGIN supply. [cite: 2049]
const byte V3P3_UV = 0x59;              // Sets the under-voltage threshold for the 3.3V supply. [cite: 2049]
const byte VDD_UV = 0x5A;               // Sets the under-voltage threshold for the 1.8V VDD supply. [cite: 2049]
const byte SELF_THR = 0x5B;             // Sets the under-voltage and over-voltage thresholds for the ADC self-test. [cite: 2049]

// --- Fault and Recovery ---
const byte FT_STS1 = 0x5D;              // READ-ONLY: Primary fault status register, shows which conditions are triggering a fault. [cite: 2053, 2058]
const byte FT_STS2 = 0x5E;              // READ-ONLY: Secondary fault status register. [cite: 2058, 2065]
const byte FT_CLR = 0x5F;               // WRITE-ONLY: Writing to bits in this register manually clears specific faults. [cite: 2065, 2074]
const byte FT_REC = 0x60;               // Configures automatic recovery methods for various faults. [cite: 2074, 2080]
const byte FT0_CFG = 0x61;              // Configures fault recovery logic, such as for standby mode and cell UV/OV recovery. [cite: 2080, 2089]
const byte FT1_CFG = 0x62;              // Not listed in the provided datasheet.
const byte FT2_CFG = 0x63;              // Not listed in the provided datasheet.

// --- ADC and Coulomb Counter (CC) ---
const byte RD_CCIRQL = 0x65;
const byte RD_CCIRQH = 0x66;
const byte RD_CCACCQL = 0x67;
const byte RD_CCACCQH = 0x68;
const byte RD_VPACKP = 0x69;
const byte RD_VTOP = 0x6A;
const byte RD_ITOP = 0x6B;

const byte RD_VCELL1 = 0x6C;
const byte RD_ICELL1 = 0x6D;
const byte RD_VCELL2 = 0x6E;
const byte RD_ICELL2 = 0x6F;
const byte RD_VCELL3 = 0x70;
const byte RD_ICELL3 = 0x71;
const byte RD_VCELL4 = 0x72;
const byte RD_ICELL4 = 0x73;
const byte RD_VCELL5 = 0x74;
const byte RD_ICELL5 = 0x75;
const byte RD_VCELL6 = 0x76;
const byte RD_ICELL6 = 0x77;
const byte RD_VCELL7 = 0x78;
const byte RD_ICELL7 = 0x79;
const byte RD_VCELL8 = 0x7A;
const byte RD_ICELL8 = 0x7B;
const byte RD_VCELL9 = 0x7C;
const byte RD_ICELL9 = 0x7D;
const byte RD_VCELL10 = 0x7E;
const byte RD_ICELL10 = 0x7F;
const byte RD_VCELL11 = 0x80;
const byte RD_ICELL11 = 0x81;
const byte RD_VCELL12 = 0x82;
const byte RD_ICELL12 = 0x83;
const byte RD_VCELL13 = 0x84;
const byte RD_ICELL13 = 0x85;
const byte RD_VCELL14 = 0x86;
const byte RD_ICELL14 = 0x87;
const byte RD_VCELL15 = 0x88;
const byte RD_ICELL15 = 0x89;
const byte RD_VCELL16 = 0x8A;
const byte RD_ICELL16 = 0x8B;

const byte RD_VNTC4 = 0x8C;
const byte RD_VNTC3 = 0x8D;
const byte RD_VNTC2 = 0x8E;
const byte RD_VNTC1 = 0x8F;
const byte RD_VGPIO3 = 0x90;
const byte RD_VGPIO2 = 0x91;
const byte RD_VGPIO1 = 0x92;
const byte RD_TDIE = 0x93;
const byte RD_V1P8 = 0x94;
const byte RD_V3P3 = 0x95;
const byte RD_V5 = 0x96;

const byte CC_STS = 0x97;             // READ-ONLY: Reports the status of the Coulomb Counter.
const byte ADC_STS = 0x98;            // READ-ONLY: Reports the status of the high-resolution ADC.
const byte ADC_CTRL = 0x99;           // Main control register to start/stop ADC scans and enable measurement classes (cells, NTCs, etc.).
const byte CC_CFG = 0x9A;             // Configures the coulomb counter accumulation settings.
const byte TRIMG_IPCB = 0x9B;         // Trimming register.
const byte HR_SCAN0 = 0x9C;           // Selects which specific cells (1-16) to include in a high-resolution ADC scan.
const byte HR_SCAN1 = 0x9D;           // Selects which NTCs and GPIOs to include in a high-resolution ADC scan.
const byte HR_SCAN2 = 0x9E;           // Selects which regulator and other voltages to include in a high-resolution ADC scan.

// --- Communication ---
const byte SILC_INFO1 = 0xA0;         // Silicon information register (e.g., version/revision).
const byte COMM_CFG = 0xA3;           // Communication configuration, primarily to set the I2C slave address. [cite: 1619]

// --- Cell-Balancing ---
const byte BAL_STS = 0xA4;            // READ-ONLY: Reports the status of the cell balancing operation (e.g., which cells are currently balancing).
const byte BAL_LIST = 0xA5;           // Manually specifies which cells to balance by setting the corresponding bits. [cite: 1170]
const byte BAL_CTRL = 0xA6;           // Main control register to start balancing (`BALANCE_GO`) and configure repetitions for manual balancing.
const byte BAL_CFG = 0xA7;            // Configures the overall balancing mode (e.g., manual vs. automatic, enable during charge/standby). [cite: 1176]
const byte BAL_THR = 0xA8;            // Sets the voltage thresholds for automatic balancing (minimum voltage to start, minimum delta between cells). [cite: 1181, 1183]

// --- Memory Control ---
const byte MEM_STATUS = 0xB4;             // READ-ONLY: Reports status of MTP/NVM (non-volatile memory) operations.
const byte OTP_CRC_STATUS = 0xB6;         // READ-ONLY: Reports CRC status for the One-Time Programmable memory.
const byte NVM_CRC_STATUS = 0xB7;         // READ-ONLY: Reports CRC status for the Non-Volatile Memory.
const byte OTP_STORE_CMD = 0xB8;          // WRITE-ONLY: Command to store current register values into the non-volatile memory. [cite: 1316]
const byte STORE_CMD_ACCESS_CODE = 0xB9;  // WRITE-ONLY: A specific code (`0xA5B6`) must be written here before a store command is accepted. [cite: 1315]