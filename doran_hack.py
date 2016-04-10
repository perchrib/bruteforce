# coding=utf-8
import time
import collections
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import data
import getpass

def get_input_from_user():
	password = getpass.getpass('Password -> ')
	return password
 
def init_driver():

	driver = webdriver.Firefox()
	driver.wait = WebDriverWait(driver, 5)
	return driver
 
 
def log_in(driver):
	driver.get("https://daron.no/oppgave/AE/")
	try:
		driver.find_element_by_css_selector('.button').click()
		print("Logg In -> Pressed")
		driver.find_element_by_css_selector('.button-filled.button-filled__has-icon.login-form__facebook').click()
		print("Logg In With Facebook -> Pressed")

		for handle in driver.window_handles:
			driver.switch_to_window(handle)
		email = driver.find_element_by_id('email')

		password = driver.find_element_by_id('pass')
		email.send_keys('**********')
		password.send_keys(get_input_from_user())
		email.send_keys(Keys.ENTER)
		print("Logg Inn -> Completed")
	except TimeoutException:
		print("Box or Button not found in google.com")

def brute_force_ae(driver,place):
	for i in range(8):
		char = place[i]
		temp_input = driver.find_element_by_id('i' + str(i)).send_keys(char)
	driver.find_element_by_css_selector('.button-filled').click()



def iterate_data(driver):
	world_of_places = data.get_data()
	counter = 1
	print(world_of_places)
	for place in world_of_places:
		brute_force_ae(driver,place[0])
		counter += 1
		if counter % 1000 == 0: 
			print(counter)
if __name__ == "__main__":
	driver = init_driver()
	log_in(driver)
	time.sleep(5)
	for handle in driver.window_handles:
		driver.switch_to_window(handle)
	iterate_data(driver)

	#driver.quit()