void setup() {
  Wire.begin();
  Serial.begin(115200);
  while (!Serial);
}

void loop()
{
  uint16_t PWR_STATUS_value = get_PWR_STATUS();
  uint16_t STB_STATUS_value = get_STB_STATUS();
  uint16_t LOAD_CHARGER_STATUS_value = get_LOAD_CHARGER_STATUS();

  decodePowerStatus(PWR_STATUS_value);
  decodeStandbyStatus(STB_STATUS_value);
  decodeLoadChargerStatus(LOAD_CHARGER_STATUS_value);
}