# importing modules to automate my login in my university portal (a bot will visit the page and auto fill it)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def runUniversityBot(usernameStr, passwordStr):
    chrome_path = "/Users/macbookpro/Desktop/chromedriver"
    browser = webdriver.Chrome(executable_path= chrome_path)
    browser.get(("https://login.navigate.navitas.com/ENTERPRISE/index/login?SAMLRequest"
             "=fVPLbtswELznKwLdbT0i2zVhCXCdPgy4tmCrPfTGUOuGgESy3FXi%2Fn1JSWmcohUvApYzszPL1Qp5Uxu2bulRHeFnC0g3t"
             "%2B5cmloh6y6zoLWKaY4SmeINICPBTusvO5ZMI2asJi10HfxFG2dxRLAktepp2%2FssOOw%2F7A6ftvt5HMcwv3uIovOMp8vZ"
             "%2FBy%2F4xUkszSaJ8u7NF0s4mUV8575DSw6mSxwqoMWYgtbhcQVuXKUJJMomSSLMl6yNGVJ%2FL3HFYPx91JVUv0Y9"
             "%2FvQg5B9LstiUhxOZS"
             "%2Byfsmx0QrbBuwJ7JMU8PW4y4JHIoMsDPlF4lTxJ0kcp0I3ITemloJ7XuhnFYqeHeSd6MrXWJfD5v8TWYXXqFeeYXvnfntfaNfiV1f356O2DafxkL4iq8m5gzLjJ4sEioI%2FKuu61s8bC5wgC8i2znHv423XN3aGrYKq2zE3J4IL3W50Y7iV6J8OLlzQkP01%2FzV8U7uFOcI5H90pwYTHuXLhPs%2FaVv6NQbjepeUKjbY0jO2f4r3rcMR2fvNyff3D5L8B"))
    username = browser.find_element(By.ID, 'username')
    username.send_keys(usernameStr)
    password = WebDriverWait(browser, 300).until(
             EC.presence_of_element_located((By.ID, 'password')))
    password.send_keys(passwordStr)

    logIn = browser.find_element((By.ID, 'submit'))
    logIn.click()
