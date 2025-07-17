bool writeData(byte deviceAddress, byte registerAddress, uint16_t data) {
  Wire.beginTransmission(deviceAddress);
  Wire.write(registerAddress);
  
  // split the 16-bit data into two 8-bit bytes
  byte low_byte = data & 0xFF;
  byte high_byte = (data >> 8) & 0xFF;

  // The low byte is sent first (based on datasheet)
  Wire.write(low_byte);
  Wire.write(high_byte);

  byte error = Wire.endTransmission();
  if (error != 0) {
    Serial.print("I2C Write Error for register 0x");
    Serial.print(registerAddress, HEX);
    Serial.print(": Error code ");
    Serial.println(error);
    return false;
  }
  return true;
}

uint16_t readData(byte deviceAddress, byte registerAddress, int size = 2) {
  Wire.beginTransmission(deviceAddress);
  Wire.write(registerAddress);

  byte error = Wire.endTransmission(false);
  if (error != 0) {
    Serial.print("I2C Read Error (set pointer): Could not set register pointer to 0x");
    Serial.println(registerAddress, HEX);
    return 0;
  }

  // Request the specified number of bytes from the device
  if (Wire.requestFrom(deviceAddress, size) != size) {
    Serial.println("Error: Failed to receive expected data from device.");
    return 0;
  }

  if (size == 2) {
    // The low byte is received first (based on datasheet)
    byte low_byte = Wire.read();
    byte high_byte = Wire.read();
    uint16_t value = (high_byte << 8) | low_byte;
    return value;
  }
  else if (size == 1) {
    return Wire.read();
  }
  return 0;
}