import serial
from time import sleep

ser = serial.Serial('/dev/ttyACM0',9600)

strAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sizeList = [5, 3, 7, 9, 6, 8, 4]
locationList = [3, 5, 7, 9]

i = 20
while True:
	alpha = 'A' + strAlphabet[locationList[i%len(locationList)] + 1:sizeList[i%len(sizeList)] + 3] + '\n'
	ser.writelines(alpha)	
	i+=1
	print("INPUT: %d, %s" %(i, alpha))
	try:
		while True:
			received_data = ser.readline()
			if received_data == alpha:
				print(received_data)
				break
		
	except:
		pass

	
