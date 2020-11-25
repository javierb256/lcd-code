import Adafruit_DHT
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()
sensor=Adafruit_DHT.DHT22

gpio = 17

humidity, tempterature = Adafruit_DHT.read_retry(sensor, gpio)

if humidity is not None and tempterature is not None:
    print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(tempterature, humidity))
    mylcd.lcd_display_string(('Temp={0:0.1f}*C'.format(tempterature)),1)
    mylcd.lcd_display_string(('Humidity={0:0.1f}%'.format(humidity)),2)

else:
    print('Failed to get reading. Try again!')