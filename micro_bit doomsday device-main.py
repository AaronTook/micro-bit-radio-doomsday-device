from microbit import *
import radio

# micro_bit_doomsday_script.py

from microbit import *
import radio
radio.on()
messageToSend = input("Message to send: ")
homeChannel = int(input("Home channel (safe): "))

sleep(1000)

maxChannel = 83
iterationNumber = 0
while True:
	if not uart.any():
		for i in range(0, maxChannel):
			if i!= homeChannel:
				radio.config(channel=i)
				radio.send(messageToSend)
		print("Iteration #" + str(iterationNumber))
		iterationNumber += 1