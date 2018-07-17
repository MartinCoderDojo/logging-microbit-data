# Original by Andrew Mulholland - Forked from
# https://github.com/gbaman/microbit-experiments

import serial
import csv
import sys
from serial.tools.list_ports import comports as list_serial_ports
import atexit


def guess_port():
    """
    From https://github.com/ntoll/microrepl
    Returns the port for the first micro:bit found connected to the computer
    running this script. If no micro:bit is found, returns None.
    """
    ports = list_serial_ports()
    platform = sys.platform
    if platform.startswith('linux'):
        for port in ports:
            if 'VID:PID=0D28:0204' in port[2].upper():
                return port[0]
    elif platform.startswith('darwin'):
        for port in ports:
            if 'VID:PID=0D28:0204' in port[2].upper():
                return port[0]
    elif platform.startswith('win'):
        for port in ports:
            if 'VID:PID=0D28:0204' in port[2].upper():
                return port[0]
    return None


def close_port(port):
    port.close()


def write_file(data):
    with open('microbit_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for val in data:
            row = val.split()
            writer.writerow(row)
        print('Data saved to microbit_data.csv!')


def main():
    data = []
    atexit.register(write_file, data)
    port = guess_port()
    if port is None:
        print('No micro:bit detected!')
        sys.exit(1)
    ser = serial.Serial(port, baudrate=115200)
    atexit.register(close_port, ser)
    print('Micro:bit connected and reading data from it.')
    print('To save the data, simply close the program and it will be saved to \
          microbit_data.csv.')
    while True:
        line = ser.readline().decode()
        data.append(line)


main()
