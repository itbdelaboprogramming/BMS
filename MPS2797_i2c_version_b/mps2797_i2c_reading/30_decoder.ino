void decodePowerStatus(uint16_t status_word) {
  // --- Decode the Power State (Bits 4:0) ---
  byte powerState = status_word & ((1 << 5) - 1);
  Serial.print("\t- Power State: ");
  switch (powerState) {
    case 0x01: Serial.println("Safe mode"); break;
    case 0x02: Serial.println("Standby mode"); break;
    case 0x04: Serial.println("Active mode"); break;
    case 0x08: Serial.println("Fault mode"); break;
    case 0x10: Serial.println("Recovery mode"); break;
    default:   Serial.println("Unknown"); break;
  }

  // --- Decode the Pack Current Status (Bits 9:7) ---
  byte currentStatus = (status_word >> 7) & ((1 << 3) - 1);
  Serial.print("\t- Current Status:");
  switch (currentStatus) {
    case 0x01: Serial.println("Discharging"); break;
    case 0x02: Serial.println("Standby range (low current)"); break;
    case 0x04: Serial.println("Charging"); break;
    default:   Serial.println("Unknown"); break;
  }
}

void decodeStandbyStatus() {

}