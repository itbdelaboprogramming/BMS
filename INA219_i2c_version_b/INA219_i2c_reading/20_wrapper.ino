int16_t readChargingStatus() {
  return readData(CHARGING_STATUS_REGISTER, 1);
}

int16_t readCommStatus() {
  return readData(COMM_REGISTER, 1);
}

int16_t readVbusVoltage() {
  return readData(VBUS_VOLTAGE_REGISTER, 2);
}

int16_t readVbusCurrent() {
  return readData(VBUS_CURRENT_REGISTER, 2);
}

int16_t readVbusPower() {
  return readData(VBUS_POWER_REGISTER, 2);
}

int16_t readVoltage() {
  return readData(VOLTAGE_REGISTER, 2);
}

int16_t readCurrent() {
  return readData(CURRENT_REGISTER, 2);
}

int16_t readPercent() {
  return readData(PERCENT_REGISTER, 2);
}

int16_t readRemainingCapacity() {
  return readData(REMAINING_CAPACITY_REGISTER, 2);
}

int16_t readRemainingDischarge() {
  return readData(REMAINING_DISCHARGE_REGISTER, 2);
}

int16_t readRemainingCharge() {
  return readData(REMAINING_CHARGE_REGISTER, 2);
}

int16_t readVoltageCell1() {
  return readData(CELL1_VOLTAGE_REGISTER, 2);
}

int16_t readVoltageCell2() {
  return readData(CELL2_VOLTAGE_REGISTER, 2);
}

int16_t readVoltageCell3() {
  return readData(CELL3_VOLTAGE_REGISTER, 2);
}

int16_t readVoltageCell4() {
  return readData(CELL4_VOLTAGE_REGISTER, 2);
}