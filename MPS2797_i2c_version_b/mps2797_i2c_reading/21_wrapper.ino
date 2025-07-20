/****************************************************************
 * Wrapper Functions for MP2797 BMS
 * These functions provide a high-level interface for interacting
 * with the MP2797, simplifying common tasks.
 ****************************************************************/

// --- Cell Configuration ---
// -- CELLS_CTRL (0x00) --
/**
 * @brief Gets the number of cells the BMS is configured to monitor.
 * @return The 16-bit value from the CELLS_CTRL register.
 */
uint16_t getCellCountConfig() {
  return readData(MPS_ADDRESS, CELLS_CTRL);
}

/**
 * @brief Sets the number of cells the BMS should monitor.
 * @param cellCount The number of cells (7-16). Use the hex codes from the datasheet (e.g., 0xA for 10 cells).
 * @return True on success, false on failure.
 */
bool setCellCount(uint8_t cellCount) {
  return writeData(MPS_ADDRESS, CELLS_CTRL, cellCount);
}


// --- IC State Control ---

// -- PWR_STATUS (0x01) --
/**
 * @brief (Parser) Extracts the 5-bit Power State from the raw register value.
 * @param raw_pwr_status The 16-bit value you already read using get_PWR_STATUS().
 * @return The decoded Power State value (e.g., 0x01 for Safe, 0x04 for Active).
 */
byte getPowerState() {
  uint16_t reg_value = get_PWR_STATUS();
  return reg_value & ((1 << 5) - 1);
}

/**
 * @brief (Parser) Extracts the 3-bit Current Status from the raw register value.
 * @param raw_pwr_status The 16-bit value you already read using get_PWR_STATUS().
 * @return The decoded Current Status value (e.g., 0x1 for Discharging, 0x4 for Charging).
 */
byte getCurrentStatus() {
  uint16_t reg_value = get_PWR_STATUS();
  return (reg_value >> 7) & ((1 << 3) - 1);
}

// -- STB_STATUS (0x02) --
/**
 * @brief (Parser) Checks if Standby Mode is enabled from the raw register value.
 * @return True if enabled, false if disabled.
 */
bool isStandbyEnabled() {
  uint16_t reg_value = get_STB_STATUS();
  return reg_value & (1 << 0);
}

/**
 * @brief
 * @return
 */
bool isStandbyFETOn() {
  uint16_t reg_value = get_STB_STATUS();
  return (reg_value >> 6) & (1 << 0);
}

/**
 * @brief (Parser) Extracts the 3-bit PACKP vs VTOP comparison status.
 * @return The decoded comparison status value.
 */
byte getPackVoltageComparisonStatus() {
  uint16_t reg_value = get_STB_STATUS();
  return (reg_value >> 8) & ((1 << 3) - 1);
}

// -- LOAD_CHARGER_STATUS (0x03) --
/**
 * @brief
 * @return
 */
bool isLoadDetected() {
  uint16_t reg_value = get_LOAD_CHARGER_STATUS();
  return reg_value & (1 << 0);
}

/**
 * @brief (Parser) Checks if a charger has been detected.
 * @return True if a charger is detected[cite: 1645].
 */
bool isChargerDetected() {
    uint16_t reg_value = get_LOAD_CHARGER_STATUS();
    return reg_value & (1 << 15); // Check CHG_IN (Bit 15)
}

// --- Fault and Recovery Wrappers ---
/**
 * @brief Gets the primary fault status register.
 * @return A 16-bit bitmask of active faults from FT_STS1.
 */
uint16_t getFaultStatus1() {
    return readData(MPS_ADDRESS, FT_STS1);
}

/**
 * @brief Gets the secondary fault status register.
 * @return A 16-bit bitmask of active faults from FT_STS2.
 */
uint16_t getFaultStatus2() {
    return readData(MPS_ADDRESS, FT_STS2);
}

/**
 * @brief Clears faults by writing to the FT_CLR register.
 * @param clear_mask A 16-bit mask of the faults you want to clear.
 * @return True on success, false on failure.
 */
bool clearFaults(uint16_t clear_mask) {
    return writeData(MPS_ADDRESS, FT_CLR, clear_mask);
}


// --- ADC and Coulomb Counter (CC) Wrappers ---
// This section follows the required scan-based process.

/**
 * @brief Configures which channels to include in a high-resolution ADC scan.
 * @param scan0 Bitmask for cells 1-16[cite: 2049].
 * @param scan1 Bitmask for NTCs and GPIOs[cite: 2049].
 * @param scan2 Bitmask for regulators[cite: 2049].
 * @return True if all writes are successful, false otherwise.
 */
bool configureADCScan(uint16_t scan0, uint16_t scan1, uint16_t scan2) {
    bool success = true;
    if (!writeData(MPS_ADDRESS, HR_SCAN0, scan0)) success = false;
    if (!writeData(MPS_ADDRESS, HR_SCAN1, scan1)) success = false;
    if (!writeData(MPS_ADDRESS, HR_SCAN2, scan2)) success = false;
    return success;
}

/**
 * @brief Starts a high-resolution ADC scan.
 * @return True on success, false on failure.
 */
bool startADCScan() {
    // Set the ADC_SCAN_GO bit (bit 0) in the ADC_CTRL register
    return writeData(MPS_ADDRESS, ADC_CTRL, 0x0001);
}

/**
 * @brief Checks if the ADC scan has completed.
 * @return True if scan is done, false otherwise[cite: 1058].
 */
bool isADCScanComplete() {
    uint16_t adc_status = readData(MPS_ADDRESS, ADC_STS);
    // Check the VSCAN_DONE_STS bit (bit 11 in RD_INT0, but also reflected here)
    // The ADC_STS register (0x98) would be the primary place to check scan status.
    // However, the datasheet does not fully detail its bits. The interrupt status is a reliable alternative.
    uint16_t int_status = readData(MPS_ADDRESS, RD_INT0);
    return (int_status & (1 << 11)); // VSCAN_DONE_INT_STS
}

/**
 * @brief Reads the ADC value for the pack voltage from the VTOP pin AFTER a scan.
 * @return The 16-bit raw ADC reading for VTOP.
 */
uint16_t getPackVoltage() {
    // NOTE: An ADC scan including VTOP must have been completed before calling this.
    return readData(MPS_ADDRESS, RD_VTOP);
}

/**
 * @brief Reads the ADC value for the pack current from the ITOP pin AFTER a scan.
 * @return The 16-bit raw ADC reading for the current.
 */
uint16_t getPackCurrent() {
    // NOTE: An ADC scan including ITOP must have been completed before calling this.
    return readData(MPS_ADDRESS, RD_ITOP);
}

/**
 * @brief Reads the raw ADC value for the internal die temperature AFTER a scan.
 * @return The 16-bit raw ADC reading.
 */
uint16_t getDieTemperatureADC() {
    // NOTE: An ADC scan including the die temp must have been completed.
    return readData(MPS_ADDRESS, RD_T_DIE);
}

