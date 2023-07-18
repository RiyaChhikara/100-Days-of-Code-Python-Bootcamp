# Day 49
# Use selenium to automate applying for jobs
# Use Linkedin's Easy Apply function

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL = "YOUR EMAIL ADDRESS"
PASSWORD = "YOUR PASSWORD"
PHONE = "YOUR PHONE NUMBER"

JOB_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3644646093&f_LF=f_AL&geoId=102713980&keywords=data%20science&location=India&refresh=true"
LOGIN_URL = "https://www.linkedin.com/login?emailAddress=&fromSignIn=&trk=public_jobs_conversion-modal-signin&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3FcurrentJobId%3D3667144542%26f_LF%3Df_AL%26geoId%3D102257491%26keywords%3Dpython%2520developer%26location%3DLondon%252C%2520England%252C%2520United%2520Kingdom"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(JOB_URL)

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()


user = driver.find_element(By.ID, "username")
user.send_keys(EMAIL)

password = driver.find_element(By.NAME, "session_password")
password.send_keys(PASSWORD)

user.send_keys(Keys.ENTER)

all_listings = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")

for listing in all_listings:
      print("called")
      listing.click()
      time.sleep(2)

      # Try to locate the apply button, if can't locate then skip the job.
      try:
            apply_button = driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
            apply_button.click()
            time.sleep(5)

            # If phone field is empty, then fill your phone number.
            phone = driver.find_element(By.CLASS_NAME,"fb-single-line-text__input")
            if phone.text == "":
                  phone.send_keys(PHONE)

            submit_button = driver.find_element(By.CSS_SELECTOR,"footer button")

            # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
            if submit_button.get_attribute("data-control-name") == "continue_unify":
                  close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
                  close_button.click()
                  time.sleep(2)
                  discard_button = driver.find_elements(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")[1]
                  discard_button.click()
                  print("Complex application, skipped.")
                  continue
            else:
                  submit_button.click()

            # Once application completed, close the pop-up window.
            time.sleep(2)
            close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
            close_button.click()

      # If already applied to job or job is no longer accepting applications, then skip.
      except NoSuchElementException:
            print("No application button, skipped.")
            continue

time.sleep(5)
driver.quit()
