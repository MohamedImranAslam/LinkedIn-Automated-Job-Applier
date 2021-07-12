from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

MAIL = "YOUR MAIL"
PASSWORD = "YOUR PASSWORD"
PHONE = "YOUR PHONE NUMBER"

chrome_driver_path = "DRIVER PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

result = driver.find_element_by_class_name("nav__button-secondary")
print(result.text)
result.click()
time.sleep(5)
email = driver.find_element_by_id("username")
email.send_keys(MAIL)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
time.sleep(5)
sign_in = driver.find_element_by_class_name("btn__primary--large")
print(sign_in.text)
sign_in.click()

time.sleep(5)
remember = driver.find_element_by_class_name("btn__primary--large")
print(remember.text)
remember.click()

time.sleep(5)
all_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")
for job in all_jobs:
    print("Selected")
    job.click()
    try:
        time.sleep(5)
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        phone.send_keys(PHONE)
        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue
time.sleep(5)
driver.quit()

# Alternative - Instead of applying just save and follow the company
# time.sleep(10)
# save_button = driver.find_element_by_class_name("jobs-save-button")
# print(save_button.text)
# save_button.click()
# driver.find_element_by_css_selector(".display-flex button").click()
