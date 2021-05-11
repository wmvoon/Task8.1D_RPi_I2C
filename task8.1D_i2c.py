import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

I2C_SCL = 3 ##trigger
I2C_SDA = 2 ##echo

GPIO.setup(I2C_SCL,GPIO.OUT)
GPIO.setup(I2C_SDA,GPIO.IN)

try:
    while True:
        GPIO.output(I2C_SCL,False)
        print("Sensor Reading Data")
        GPIO.output(I2C_SCL,True)
        time.sleep(1)
        GPIO.output(I2C_SCL,False)
        
        while GPIO.input(I2C_SDA)==0:
            pulse_start=time.time()
            
        while GPIO.input(I2C_SDA)==1:
            pulse_end=time.time()
            
        pulse_duration=pulse_end - pulse_start
        
        distance=pulse_duration*11150
        
        distance=round(distance,2)
        
        print("The Distance between Object and Sensor: " + str(distance))
        
        ##prompt different message depending on the distance 
        if distance > 100:
            print("Object is very far.")
        elif 50 < distance < 100:
            print("Object is far.")
        elif 20 < distance < 50:
            print("Obejct is getting closer but still safe distance.")
        elif 10 < distance < 20:
            print("Object is near.")
        else:
            print("Object is too near !!!!")
            
except KeyboardInterrupt:
    GPIO.cleanup()
