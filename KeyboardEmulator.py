import serial
from pynput.keyboard import Controller, Key
import time

keyboard = Controller()
ser = serial.Serial('COM3', 9600)  # Replace with your correct COM port
time.sleep(2)  # Let Arduino boot up

while True:
    if ser.in_waiting > 0:
        command = ser.readline().decode().strip()
        if command == 'J':
            keyboard.press(Key.up)
            time.sleep(0.1)
            keyboard.release(Key.up)
        elif command == 'C':
            keyboard.press(Key.down)
            time.sleep(0.1)
            keyboard.release(Key.down)
