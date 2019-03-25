import os,time
import serial

def robot(text):
	os.system("espeak -ven-us+f4-s160 ' "+text+" ' 2>/dev/null")
	 ser.write ("1"+text)

ser=serial.Serial("/dev/ttyS0",9600)
time.sleep(3)
robot("System initialise")
time.sleep(2)
while True:
	if(ser.in_waiting>0):
		line = ser.readline()
		print(line)
		robot(line)
