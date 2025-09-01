import serial
import threading

def read_serial():
    ser = serial.Serial('COM3', 9600)
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            model_id, quality = line.split(',')
            print(f"Model ID: {model_id}, Quality: {quality}")
            # Here’s where we’ll insert into SQL later

# Start the reader thread
thread = threading.Thread(target=read_serial)
thread.daemon = True
thread.start()

# Main loop can do other things (e.g., UI, logging, etc.)
while True:
    pass