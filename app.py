from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from logging import error

#pip install selenium

# ServiceNow credentials
username = "admin"
password = "uC9zSLnlK6rN"


def automationLogin():
    # initialize the Chrome driver
    driver = webdriver.Chrome("chromedriver")

    # head to ServiceNow PDI login page
    driver.get("https://dev107519.service-now.com/")
    driver.implicitly_wait(30)

    #since the login box is inside an iframe in servicenow url
    driver.switch_to.frame('gsft_main')

    # find username/email field and send the username itself to the input field
    driver.find_element_by_name("user_name").send_keys(username)
    # find password input field and insert password as well

    driver.find_element_by_name("user_password").send_keys(password)

    # click login button
    driver.find_element_by_name("not_important").click()

    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=30).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    error_message = "Incorrect username or password."
    # get the errors (if there are)
    errors = driver.find_elements_by_class_name("flash-error")
    # print the errors optionally
    # for e in errors:
    #     print(e.text)
    # if we find that error message within errors, then login is failed
    if any(error_message in e.text for e in errors):
        print("[!] Login failed")
    else:
        print("[+] Login successful")

    # close the driver
    driver.close()

automationLogin()


#scheduling to run every 6 hours
# schedule.every(6).hours.do(automationLogin)

# while True:
#     schedule.run_pending()
#     time.sleep(1)