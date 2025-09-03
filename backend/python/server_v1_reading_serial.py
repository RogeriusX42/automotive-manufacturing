import serial
import json 
import threading
from datetime import datetime

def read_serial():
    ser = serial.Serial('COM3', 9600)
    while True:
        line = ser.readline().decode('utf-8').strip().split(',')
        if line:
            timestamp = datetime.now().strftime('Date: %Y-%m-%d, Time:%H:%M:%S')
            #data = {'timestamp': {timestamp}, 'ProductID': line[0], 'Quality':line[1]}
            
            data = { 
                "timestamp": timestamp, 
                "ProductID": line[0], 
                "Quality": line[1]
            }
            
            print(json.dumps(data, indent=2)) 

            with open('production_cars_v1.json', 'a') as file:
                    file.write(json.dumps(data) + ',\n')
            
        
# Start the reader thread
thread = threading.Thread(target=read_serial)
thread.daemon = True
thread.start()

# Main loop can do other things (e.g., UI, logging, etc.)
while True:
    pass


#### Commands 

