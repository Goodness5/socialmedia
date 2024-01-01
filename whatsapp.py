from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def automate_whatsapp_responses():
    # Specify the path to your webdriver (e.g., chromedriver.exe)
    driver_path = '/path/to/chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path)

    # Open WhatsApp Web in the browser
    driver.get("https://web.whatsapp.com/")
    
    # Wait for the user to scan the QR code
    input("Scan the QR code and press Enter when ready...")

    # Specify the message you want to send
    response_message = "Wish you the same! 🎉"

    # Define a list of contacts or groups to reply to
    contacts_to_reply = ["Contact1", "Contact2", "Group1"]

    for contact in contacts_to_reply:
        # Search for the contact
        search_box = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
        search_box.click()
        search_box.send_keys(contact)
        search_box.send_keys(Keys.ENTER)

        # Wait for the chat to load
        time.sleep(2)

        # Type and send the response message
        message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
        message_box.click()
        message_box.send_keys(response_message)
        message_box.send_keys(Keys.ENTER)

        # Wait for a while before moving to the next contact
        time.sleep(1)

    # Close the browser window
    driver.quit()

# Call the function to automate responses
automate_whatsapp_responses()
