import machine
import utime

testButton = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)
i =0
while True:
    if testButton.value()==1:
        print(i)
        i+=1
        utime.sleep(0.5)
        