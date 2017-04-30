from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import UnexpectedAlertPresentException
import time,os
import getpass


def main():
	u_name = raw_input("Enter Your Facebook Username >> ")
	u_pass = getpass.getpass("Enter Your Facebook Password >> ")
	msg = raw_input("Enter the Message >> ")
	display = Display(visible=1, size=(900, 700))
	display.start()
	driver = webdriver.Chrome()
	driver.get('https://mbasic.facebook.com')
	username = driver.find_element_by_name('email')
	password = driver.find_element_by_name('pass')
	sub = driver.find_element_by_name('login')
	username.send_keys(u_name)
	password.send_keys(u_pass)
	sub.click()
	time.sleep(5)
	groups = ["https://mbasic.facebook.com/groups/samplegroup1","https://mbasic.facebook.com/groups/samplegroup2?refid=27"]
	for grp in groups:
		driver.get(grp)
		time.sleep(2)
		post_form = driver.find_element_by_name('xc_message')
		post_form.send_keys(msg)
		post_btn = driver.find_element_by_name('view_post')
		post_btn.click()
		time.sleep(3)
	
main()
