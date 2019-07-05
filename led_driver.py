import RPi.GPIO as GPIO
import time


class LEDDriver:

	def __init__(self, green_pin_nr, red_pin_nr):
		self.green_led = green_pin_nr
		self.red_led = red_pin_nr
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.green_led, GPIO.OUT)
		GPIO.setup(self.red_led, GPIO.OUT)
		GPIO.output(self.red_led, GPIO.HIGH)
		self.red_on = True

	def toggle(self):
		if self.red_on:
			GPIO.output(self.red_led, GPIO.LOW)
			GPIO.output(self.green_led, GPIO.HIGH)
			self.red_on = False
		else:
			GPIO.output(self.green_led, GPIO.LOW)
			GPIO.output(self.red_led, GPIO.HIGH)
			self.red_on = True


	def kill_all(self):    
		GPIO.output(self.green_led, GPIO.LOW)
		GPIO.output(self.red_led, GPIO.LOW)


if __name__ == "__main__":
	led_driver = LEDDriver(25, 24)
	led_driver.kill_all()
#	while True:
#		led_driver.toggle()
#		time.sleep(1)
