import Adafruit_CharLCD as LCD
from time import sleep
from collections import deque

lcd_rs        = 25
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 1

lcd_columns = 16
lcd_rows    = 2

class LCDDriver():

	def __init__(self):
		self.lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
									lcd_columns, lcd_rows, lcd_backlight)
		self.top_row = ""
		self.bottom_row = ""
		self.messages = list()
		self.message_index = 0

	def add_message(self, message_top, message_bottom):
		self.messages.append({"top": message_top, "bottom": message_bottom})

	def tick(self):
		if self.message_index < len(self.messages):
			message = self.messages[self.message_index]
			self.lcd.clear()
			self.lcd.message( message["top"] + "\n" + message["bottom"])
			self.message_index = (self.message_index + 1) % len(self.messages)


	def show(self, top, bottom):
		self.lcd.clear()
		self.lcd.message(top + "\n" + bottom)	


if __name__ == "__main__":
	lcd_driver = LCDDriver()
	lcd_driver.add_message("TIMO", "DE WAELE")
	lcd_driver.add_message("ZOHRA", "DEVOS")
	lcd_driver.add_message("AMBER", "DE WAELE")
	while True:
		lcd_driver.tick()
		sleep(5)
