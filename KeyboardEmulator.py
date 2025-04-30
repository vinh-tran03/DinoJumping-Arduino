import serial
from pynput.keyboard import Controller, Key
import time

keyboard = Controller()
ser = serial.Serial('/dev/cu.usbmodem101', 9600)  
time.sleep(2)  # Wait for Arduino to initialize

print("Listening for input from Arduino...")

while True:
    if ser.in_waiting > 0:
        command = ser.readline().decode().strip()
        print(f"Received from Arduino: {command}") 

        if command == 'J':
            print("Jump command detected. Pressing UP arrow.")
            keyboard.press(Key.up)
            time.sleep(0.1)
            keyboard.release(Key.up)

        elif command == 'C':
            print("Crouch command detected. Pressing DOWN arrow.")
            keyboard.press(Key.down)
            time.sleep(0.1)
            keyboard.release(Key.down)
