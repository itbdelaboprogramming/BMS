// -- PWR_STATUS (0x01) --
void decodePowerStatus(uint16_t status_word) {
  Serial.println("Power Status:");

  // --- Decode the Power State (Bits 4:0) ---
  byte PWR_STATE = status_word & ((1 << 5) - 1);
  Serial.print("\t- Power State: ");
  switch (PWR_STATE) {
    case 0x01: Serial.println("Safe mode"); break;
    case 0x02: Serial.println("Standby mode"); break;
    case 0x04: Serial.println("Active mode"); break;
    case 0x08: Serial.println("Fault mode"); break;
    case 0x10: Serial.println("Recovery mode"); break;
    default:   Serial.println("Unknown"); break;
  }

  // --- Decode the Pack Current Status (Bits 9:7) ---
  byte PACK_CURRENT_STATUS = (status_word >> 7) & ((1 << 3) - 1);
  Serial.print("\t- Current Status:");
  switch (PACK_CURRENT_STATUS) {
    case 0x01: Serial.println("Discharging"); break;
    case 0x02: Serial.println("Standby range (low current)"); break;
    case 0x04: Serial.println("Charging"); break;
    default:   Serial.println("Unknown"); break;
  }
}

// -- STB_STATUS (0x02) --
void decodeStandbyStatus(uint16_t status_word) {
  Serial.println("Standby Status:");

  // --- Decode the Enable Standby Status (Bit 0) ---
  Serial.print("\t- Standby Mode: ");
  bool STBY_STATE = status_word & (1 << 0) ? Serial.println("On") : Serial.println("Off");

  // --- Decode the SBYDSG Driver Status (Bit 6) ---
  Serial.print("\t- SBYDSG Driver: ");
  bool DSG_PFET_SYNC = (status_word >> 6) & (1 << 0) ? Serial.println("On") : Serial.println("Off");

  // --- Decode the Pack Comparison Status (Bits 10:8) ---
  Serial.print("\t- Voltage Comparison: ");
  bool PACKP_COMP_STS = (status_word >> 8) & ((1 << 3) - 1);
  switch (PACKP_COMP_STS) {
    case 0x0: Serial.println("Not available"); break;
    case 0x1: Serial.println("V_PACKP < V_VTOP - 1.6V"); break;
    case 0x2: Serial.println("V_VTOP + 160mV > V_PACKP > V_VTOP - 1V"); break;
    case 0x3: Serial.println("PACKP comparator invalid"); break;
    case 0x4: Serial.println("V_PACKP > V_VTOP + 270mV"); break;
  }
}

// -- LOAD_CHARGER_STATUS (0x03) --
void decodeLoadChargerStatus(uint16_t status_word) {
  Serial.println("Load Charger Status:");

  // --- Decode Load Plugin Enable Status ---
  Serial.print("\t- Load Detection Enabled: ");
  bool LDDET_EN = status_word & (1 << 0) ? Serial.println("True") : Serial.prinltn("False");

  // --- Decode Charger Plugin Enable Status ---
  Serial.print("\t- Charger Detection Enabled: ");
  bool CHCONN_EN = (status_word >> 1) & (1 << 0) ? Serial.println("True") : Serial.prinltn("False");

  // --- Decode PACKP Detection Pre-charging Status ---
  Serial.print("\t- PACKP Detection Status: ");
  bool LD_SETTLING = (status_word >> 1) & (1 << 0) ? Serial.println("True") : Serial.prinltn("False");

  // --- Decode PACKP Detection Pre-charging Status ---
  Serial.print("\t- PACKP Detection Status: ");
  bool LD_SETTLING = (status_word >> 2) & (1 << 0) ? Serial.println("True") : Serial.prinltn("False");

  // ...
}