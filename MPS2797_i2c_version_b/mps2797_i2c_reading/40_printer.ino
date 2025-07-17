void printPowerStatus() {
  uint16_t status_word = get_PWR_STATUS();
  decodePowerStatus(status_word);
}