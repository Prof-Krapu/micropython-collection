from machine import Pin, ADC            #importing Pin and ADC class
from time import sleep                  #importing sleep class

adc = ADC(Pin(33))            #creating potentiometer object
adc.atten(ADC.ATTN_11DB)       #3.3V full range of voltage
def remap(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    # return int(rightMin + (valueScaled * rightSpan))
    return rightMin + (valueScaled * rightSpan)
while True:
    soil = adc.read()   #reading analog pin
    print(soil)#printing the ADC value
    soil2 = remap(soil, 3344,1780,0,100)
    print(soil2)
    sleep(0.250)
