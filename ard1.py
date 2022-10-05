from email import message
from tkinter import Y
import serial
import time

lenghs = {'s' : 3, 
          'y': 0,
          'n': 0}

def get_connection(port):
    ser = serial.Serial(port, timeout = 1)
    return ser

def send(ser, message, msg_len):
    ser.write(message)
    time.sleep(0.1)
    if msg_len != 0:
        data = ser.read(msg_len)
        result = data.decode()
        result = result.strip()
        print(result)
        
        
        
def switch(result):
    if result >= 200:
        param = 'y'   
    else:
        param = 'n'
    return param
    
        
        
        
        
if __name__ == '__main__':
    ser = get_connection("COM9")
    while True:
        inp = input("Enter command: ")
        length = lenghs.get(inp,13)
#S        send(ser, inp.encode(), length)
        if length == 13:
            switch(send(ser, inp.encode(), length))