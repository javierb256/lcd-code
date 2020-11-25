import Adafruit_DHT

sensor=Adafruit_DHT.DHT22

gpio = 17

humidity, tempterature = Adafruit_DHT.read_retry(sensor, gpio)

if humidity is not None and tempterature is not None:
    print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(tempterature, humidity))
else:
    print('Failed to get reading. Try again!')