from selenium import webdriver
import Util

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/google-chrome"
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_position(0,0)
driver.set_window_size(1600,900)
driver.get('http://gineco.bayer.foster.com.br/')
Util.fullpage_screenshot(driver, "/home/lancemaker/Documents/Github/PageToPDF/img/test.png")
driver.close()