from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Replace these with your LinkedIn login credentials
username = 'arkpandey222@gmail.com'
password = 'arknova1999'

# Setup Chrome options
chrome_options = Options()

# Install Chrome WebDriver
service = Service(ChromeDriverManager().install())

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open LinkedIn login page
    driver.get('https://www.linkedin.com/login')

    # Wait until the login elements are present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))

    # Enter the username
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys(username)

    # Enter the password
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)

    # Click the login button
    password_input.send_keys(Keys.RETURN)

    # Wait until the profile page loads
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'profile-nav-item')))
    
    print("Login successful")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
