from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import setup

print('loading...')
setup.print_information()
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

def start(website_link, XPATH1, XPATH2):
    login = input('Would you like to login? (y/n) ')
    if login == 'n':
        browser.get(website_link)
        startTyping(browser, XPATH1, XPATH2)
    if login == 'y':
        browser.get('https://10fastfingers.com/login')
        login_continue = input('Would you like to continue? (y/n) ')
        if login_continue == 'y':
            browser.get(website_link)
            startTyping(browser, XPATH1, XPATH2)
        if login_continue == 'n':
            exit()

def startTyping(browser, XPATH1, XPATH2):
    input_variable = input("Start? (y/n) ")
    if input_variable == "y":
        inputField = browser.find_element(By.XPATH, '//*[@id="inputfield"]')
        counter = 1
        while True:
            wordElement = browser.find_element(By.XPATH, XPATH1 + str(counter) + XPATH2)

            word = wordElement.text

            inputField.send_keys(word)
            inputField.send_keys(" ")

            if counter >= 380:
                input_variable = input(".")

            counter = counter + 1
            time.sleep(0.65)
