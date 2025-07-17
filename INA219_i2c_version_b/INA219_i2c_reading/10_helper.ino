int16_t readData(byte address, int size) {
  Wire.beginTransmission(UPS_ADDRESS);
  Wire.write(address);

  byte error = Wire.endTransmission(false);
  if (error != 0) {
    Serial.print("Error: Could not set register pointer to 0x");
    Serial.println(address, HEX);
    return 0;
  }

  if (Wire.requestFrom(UPS_ADDRESS, size) != size) {
    Serial.println("Error: Failed to receive expected data from device.");
    return 0;
  }

  if (size == 2) {
    byte low_byte = Wire.read();
    byte high_byte = Wire.read();
    int16_t value = (high_byte << 8) | low_byte;
    return value;
  }

  if (size == 1) {
    return Wire.read();
  }

  return 0;
}