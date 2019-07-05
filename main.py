import RPi.GPIO as GPIO
from stock_data import get_stock_data
from lcd_driver import LCDDriver

from time import sleep


tickers =	[
				"AAPL",
				"TSLA",
				"DIS",
				"BRK.B",
				"BYND",
				"SNAP",
				"S&P500",
				"EXSA.DE"
			]


aliases =   {
				"DOW":"^DJI",
				"S&P500":"^GSPC",
				"BRK.B":"BRK-B",
				"BRK.A":"BRK-A",
				"SHIT":"SNAP",
				"EUR/USD":"EURUSD=X",
				"USD/EUR":"USDEUR=X",
				"BTC/EUR":"BTCEUR=X",
				"BTC/USD":"BTCUSD=X",
				"EUR/NZD":"EURNZD=X",
				"NZD/EUR":"NZDEUR=X"
            }


if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	lcd_driver = LCDDriver()
	while True:
		for ticker in tickers:
			if ticker in aliases:
				symbol = aliases[ticker]
			else:
				symbol = ticker
			data = get_stock_data(symbol)
			lcd_driver.show(ticker, str(data[0]) + " " + str(data[1]) + "%")
			sleep(5)
