#!/usr/bin/env python3

import smbus
import struct
import socket
from time import sleep

class HostLink:
    def __init__(self):
        # TCP Client Socket
        self.plc_address = "192.168.110.10"
        self.plc_port    = 8501

        # Create a TCP/IP socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # connect the client
        self.client.connect((self.plc_address, self.plc_port))

    def confirm_response(self):
        response_msg = self.client.recv(4096).decode()
        response_msg = response_msg.rstrip()

        if response_msg == "OK":
            return True
        else:
            return False

    def data_response(self):
        response_msg = self.client.recv(4096).decode()
        response_msg = response_msg.rstrip()
        return response_msg

    def change_mode(self, mode):
        mode_no = { "program": 0, "run": 1 }
        cmd = "M{}\r\n".format(mode_no[mode])
        self.client.send(cmd.encode())
        return self.confirm_response()

    def confirm_mode(self):
        cmd = "?M\r\n"
        self.client.send(cmd.encode())
        response = self.data_response()
        mode = { 0: "program", 1: "run"}
        return mode[int(response)]

    def query_model(self):
        cmd = "?K \r\n"
        self.client.send(cmd.encode())
        response = self.data_response()
        plc_model = {
            57  : "KV-8000",   55  : "KV-7500", 
            128 : "KV-NC32T",  132 : "KV-N60", 
            133 : "KV-N40",    134 : "KV-N24"
        }
        return plc_model[int(response)]

    def forced_set(self, mode, addr):
        """
        Device Type: R, MR, LR, CR, T, C, CTC, VB
        """
        if mode == "continuous":
            cmd = "STS {}\r\n".format(addr)
        else:
            cmd = "ST {}\r\n".format(addr)

        self.client.send(cmd.encode())
        return self.confirm_response()

    def forced_reset(self, mode, addr):
        """
        Device Type: R, MR, LR, CR, T, C, CTC, VB
        """
        if mode == "continuous":
            cmd = "RSS {}\r\n".format(addr)
        else:
            cmd = "RS {}\r\n".format(addr)

        self.client.send(cmd.encode())
        return self.confirm_response()

    def single_read(self, addr, data_format=None):
        """
        .U : Decimal, 16bit, unsigned
        .S : Decimal, 16bit, signed
        .D : Decimal, 32bit, unsigned
        .L : Decimal, 32bit, signed
        """

        if "M" in addr or "LR" in addr:
            cmd = "RD {}\r\n".format(addr)
        else:
            if data_format == None:
                data_format = ".U"
            cmd = "RD {}{}\r\n".format(addr, data_format)

        self.client.send(cmd.encode())
        return self.data_response()

    def batch_read(self, addr, length=0, data_format=".U"):
        """
        .U : Decimal, 16bit, unsigned
        .S : Decimal, 16bit, signed
        .D : Decimal, 32bit, unsigned
        .L : Decimal, 32bit, signed
        """

        if "M" in addr or "LR" in addr:
            cmd = "RDS {} {}\r\n".format(addr, length)
        else:
            if data_format == None:
                data_format = ".U"
            cmd = "RDS {}{} {}\r\n".format(addr, data_format, length)

        self.client.send(cmd.encode())
        list_resp = self.data_response().split()
        return list_resp

    def single_write(self, addr, value=0, data_format=".U"):
        """
        .U : Decimal, 16bit, unsigned
        .S : Decimal, 16bit, signed
        .D : Decimal, 32bit, unsigned
        .L : Decimal, 32bit, signed
        """
        cmd = "WR {}{} {}\r\n".format(addr, data_format, value)
        self.client.send(cmd.encode())
        return self.confirm_response()

    def batch_write(self, addr, data_format=".U", length=None, values=None):
        """
        .U : Decimal, 16bit, unsigned
        .S : Decimal, 16bit, signed
        .D : Decimal, 32bit, unsigned
        .L : Decimal, 32bit, signed
        """
        vals = ' '.join(values)
        cmd = "WRS {}{} {} {}\r\n".format(addr, data_format, length, vals)
        self.client.send(cmd.encode())
        return self.confirm_response()

if __name__ == "__main__":
    keyence = HostLink()

    I2C_ADDR = 0x2D
    bus = smbus.SMBus(1)
    
    # testing code
    while True:
        # read = keyence.single_read("W05")
        # number = random.randint(0,10)
        # keyence.single_write("DM100", number)

        data = bus.read_i2c_block_data(I2C_ADDR, 0x02, 1); charging_status = data[0]
        data = bus.read_i2c_block_data(I2C_ADDR, 0x10, 6); vbus_voltage = data[0] | data[1] << 8; vbus_current = data[2] | data[3] << 8; vbus_power = data[4] | data[5] << 8
        data = bus.read_i2c_block_data(I2C_ADDR, 0x20, 12); battery_voltage = data[0] | data[1] << 8; battery_current_raw = data[2] | data[3] << 8; battery_percent = data[4] | data[5] << 8; battery_capacity = data[6] | data[7] << 8; empty_time = data[8] | data[9] << 8; full_time = data[10] | data[11] << 8
        data = bus.read_i2c_block_data(I2C_ADDR, 0x30, 8); voltage_V1 = data[0] | data[1] << 8; voltage_V2 = data[2] | data[3] << 8; voltage_V3 = data[4] | data[5] << 8; voltage_V4 = data[6] | data[7] << 8

        values_to_write = [
            charging_status, vbus_voltage, vbus_current, vbus_power,
            battery_voltage, battery_current_raw, battery_percent,
            battery_capacity, empty_time, full_time, voltage_V1,
            voltage_V2, voltage_V3, voltage_V4
        ]

        keyence.batch_write("DM100", length=len(values_to_write), values=values_to_write)
        sleep(0.1)

