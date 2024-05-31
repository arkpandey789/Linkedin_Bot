import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# LinkedIn credentials
USERNAME = 'arkpandey222@gmail.com'
PASSWORD = 'arknova1999'

# Custom message to send with connection request
CUSTOM_MESSAGE = 'Hello, I came across your profile and would love to connect and learn more about your work as a VP of Engineering.'

def login(driver):
    driver.get('https://www.linkedin.com/login')
    time.sleep(5)
    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

def search_and_connect(driver, job_title):
    search_box = driver.find_element(By.XPATH, '//input[@aria-label="Search"]')
    search_box.send_keys(job_title)
    search_box.send_keys(Keys.RETURN)
    time.sleep(15)

    people_tab = driver.find_element(By.XPATH, '//button[text()="People"]')
    people_tab.click()
    time.sleep(5)

    profiles = driver.find_elements(By.XPATH, '//button[text()="Connect"]')
    for profile in profiles:
        try:
            profile.click()
            time.sleep(2)
            
            # Locate and click "Add a note" button
            add_note_button = driver.find_element(By.XPATH, '//button[text()="Send without a note"]')
            add_note_button.click()
            time.sleep(2)
            
            # Enter custom message
            message_box = driver.find_element(By.XPATH, '//textarea[@name="message"]')
            message_box.send_keys(CUSTOM_MESSAGE)
            
            # Locate and click "Send" button
            send_button = driver.find_element(By.XPATH, '//button[text()="Send"]')
            send_button.click()
            time.sleep(2)
        
        except Exception as e:
            print(f"Error connecting to profile: {e}")
            continue

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())  
    driver = webdriver.Chrome(service=service, options=options)
    try:
        login(driver)
        search_and_connect(driver, 'John')
    finally:
        driver.quit()
