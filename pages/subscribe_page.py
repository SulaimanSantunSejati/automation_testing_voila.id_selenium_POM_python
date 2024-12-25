from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SubscribePage:
    def __init__ (self, driver):
        self.driver = driver
        self.input_email_subscribe = (By.NAME, "email")
        self.subscribe_button = (By.NAME, 'subscribe-button')
        self.subscribed_notification_text = (By.CSS_SELECTOR, "p._17zx15t6o._17zx15te8._17zx15t4g._17zx15thc#base")
        self.email_already_subscribed_text = (By.CSS_SELECTOR, "[data-test-id='toast-']")
        self.please_error_message_text = (By.CSS_SELECTOR, "p._15kd2wejk._1ccbe2wc#base") 

#step method 
    def scroll_to_position(self, y_position): self.driver.execute_script(f"window.scrollTo(0, {y_position});")

    def get_error_message_text(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.please_error_message_text)).text
    
    def click_input_email_subscribe(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.input_email_subscribe)).click()

    def set_email_input_subscribe(self, email):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.input_email_subscribe)).send_keys(email)

    def click_subscribe_submit_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.subscribe_button)).click()
    
    def get_subscribed_notification_text(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.subscribed_notification_text)).text

    def get_email_already_subscribed_text(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.email_already_subscribed_text)).text
    
    #Combined step
    def set_subscribe(self, email):
       self.scroll_to_position(4800)
       self.click_input_email_subscribe()
       self.set_email_input_subscribe(email)
       self.click_subscribe_submit_button()