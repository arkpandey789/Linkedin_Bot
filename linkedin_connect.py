import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# LinkedIn credentials
username = ''
password = ''

# Custom message for connection requests
custom_message = "Hi, I would like to connect with you to discuss potential collaborations."

# Setup WebDriver using ChromeDriverManager
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())  # This will automatically download and install the appropriate Chromedriver
driver = webdriver.Chrome(service=service, options=options)

def linkedin_login():
    driver.get('https://www.linkedin.com/feed/')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

def search_vp_of_engineering():
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search"]')))
    search_box.send_keys('VP of engineering')
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the search results to load and click on the "People" filter
    people_filter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="People"]')))
    people_filter.click()

    # Wait for the updated search results to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//ul[contains(@class, "reusable-search__entity-result-list")]'))
    )

def send_connection_requests():
    # Get the profile links
    profile_links = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/in/') and contains(@aria-label, 'Search result')]"))
    )
    
    profile_urls = [link.get_attribute('href') for link in profile_links[:10]]
    print(f"Found {len(profile_urls)} profiles")

    for index, profile_url in enumerate(profile_urls):
        driver.get(profile_url)
        print(f"Opened profile {index + 1}")

        try:
            connect_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Connect')]"))
            )
            connect_button.click()
            print(f"Clicked connect on profile {index + 1}")

            add_note_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Add a note']"))
            )
            add_note_button.click()

            message_box = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@name='message']"))
            )
            message_box.send_keys(custom_message)

            send_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send now']"))
            )
            send_button.click()
            print(f"Connection request {index + 1} sent with a message")
        except Exception as e:
            print(f"Could not send connection request for profile {index + 1}: {e}")
        
        time.sleep(2)  # Small delay between requests

    driver.get('https://www.linkedin.com/search/results/people/?keywords=VP%20of%20engineering')

def main():
    linkedin_login()
    search_vp_of_engineering()
    send_connection_requests()

if __name__ == "__main__":
    main()
