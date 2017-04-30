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
	groups = ["https://mbasic.facebook.com/groups/848709015143177?refid=27","https://mbasic.facebook.com/groups/197057617034917?refid=27","https://mbasic.facebook.com/groups/922122447864810?refid=27","https://mbasic.facebook.com/groups/425072864252439?refid=27","https://mbasic.facebook.com/groups/141391402584840?refid=27","https://mbasic.facebook.com/groups/628556940545528?refid=27","https://mbasic.facebook.com/groups/1499611193585045?refid=27","https://mbasic.facebook.com/groups/1604245399825835?refid=27","https://mbasic.facebook.com/groups/769790473038426?refid=27","https://mbasic.facebook.com/groups/190003027727763?refid=27","https://mbasic.facebook.com/groups/251629428263817?refid=27","https://mbasic.facebook.com/groups/304437439602456?refid=27","https://mbasic.facebook.com/groups/166467676886727?refid=27","https://mbasic.facebook.com/groups/14194475589?refid=27","https://mbasic.facebook.com/groups/121575854607473?refid=27","https://mbasic.facebook.com/groups/203631149766047?refid=27"]
	for grp in groups:
		driver.get(grp)
		time.sleep(2)
		post_form = driver.find_element_by_name('xc_message')
		post_form.send_keys(msg)
		post_btn = driver.find_element_by_name('view_post')
		post_btn.click()
		time.sleep(3)
	
main()
