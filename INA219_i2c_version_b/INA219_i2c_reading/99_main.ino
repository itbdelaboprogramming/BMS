void setup() {
  Wire.begin();
  Serial.begin(115200);
  while (!Serial);
  Serial.println("UPS HAT (E) Reader Initialized");
}

void loop()
{
  // Read data from UPS HAT (E)
  int16_t charging_status = readChargingStatus();
  int16_t comm_status = readCommStatus();
  int16_t vbus_voltage = readVbusVoltage();
  int16_t vbus_current = readVbusCurrent();
  int16_t vbus_power = readVbusPower();
  int16_t voltage = readVoltage();
  int16_t current = readCurrent();
  int16_t percent = readPercent();
  int16_t remaining_capacity = readRemainingCapacity();
  int16_t remaining_discharge = readRemainingDischarge();
  int16_t remaining_charge = readRemainingCharge();
  int16_t voltage_cell1 = readVoltageCell1();
  int16_t voltage_cell2 = readVoltageCell2();
  int16_t voltage_cell3 = readVoltageCell3();
  int16_t voltage_cell4 = readVoltageCell4();

  // Logging
  Serial.print("Charging Status: ");
  decodeChargingStatus(charging_status);
  Serial.println();
  
  Serial.print("VBUS Voltage\t\t: ");
  Serial.print(vbus_voltage);
  Serial.println(" mV");

  Serial.print("VBUS Current\t\t: ");
  Serial.print(vbus_current);
  Serial.println(" mA");

  Serial.print("VBUS Power\t\t: ");
  Serial.print(vbus_power);
  Serial.println(" mW");

  Serial.print("Battery Voltage\t\t: ");
  Serial.print(voltage);
  Serial.println(" mV");

  Serial.print("Battery Current\t\t: ");
  Serial.print(current);
  Serial.println(" mA");

  Serial.print("Battery Percent\t\t: ");
  Serial.print(percent);
  Serial.println(" %");

  Serial.print("Remaining Capacity\t: ");
  Serial.print(remaining_capacity);
  Serial.println(" mAh");

  if (remaining_discharge > -1) {
    Serial.print("Time to Empty\t\t: ");
    Serial.print(remaining_discharge);
    Serial.println(" min");
  }
  else {
    Serial.print("Time to Full\t\t: ");
    Serial.print(remaining_charge);
    Serial.println(" min");
  }

  Serial.print("Cell Voltage 1\t\t: ");
  Serial.print(voltage_cell1);
  Serial.println(" mV");

  Serial.print("Cell Voltage 2\t\t: ");
  Serial.print(voltage_cell2);
  Serial.println(" mV");

  Serial.print("Cell Voltage 3\t\t: ");
  Serial.print(voltage_cell3);
  Serial.println(" mV");

  Serial.print("Cell Voltage 4\t\t: ");
  Serial.print(voltage_cell4);
  Serial.println(" mV");

  Serial.println();

  delay(3000);
}

void decodeChargingStatus(int16_t charging_status) {
  if (charging_status & 0b10000000) {
    if (charging_status & 0b01000000) {
      Serial.print("Fast charging");
    }
    else {
      Serial.print("Charging");
    }
  }
  else {
    Serial.print("Not charging");
  }

  Serial.print(" | VBUS: ");
  if (charging_status & 0b00100000) {
    Serial.print("Powered");
  }
  else {
    Serial.print("Not powered");
  }

  byte charge_state = charging_status & 0b00000111;
  Serial.print(" | Detail: ");
  switch (charge_state) {
    case 0b000: Serial.print("standby"); break;
    case 0b001: Serial.print("trickle charge"); break;
    case 0b010: Serial.print("constant current charge"); break;
    case 0b011: Serial.print("constant voltage charge"); break;
    case 0b100: Serial.print("charging pending"); break;
    case 0b101: Serial.print("full state"); break;
    case 0b110: Serial.print("charge timeout"); break;
  }
}