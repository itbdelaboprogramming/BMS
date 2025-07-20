/****************************************************************
 * Wrapper Functions for MP2797 BMS
 * These functions provide a high-level interface for interacting
 * with the MP2797, simplifying common tasks.
 ****************************************************************/

uint16_t get_CELLS_CTRL() {
  return readData(MPS_ADDRESS, CELLS_CTRL);
}

uint16_t get_PWR_STATUS() {
  return readData(MPS_ADDRESS, PWR_STATUS);
}

uint16_t get_STB_STATUS() {
  return readData(MPS_ADDRESS, STB_STATUS);
}

uint16_t get_LOAD_CHARGER_STATUS() {
  return readData(MPS_ADDRESS, LOAD_CHARGER_STATUS);
}