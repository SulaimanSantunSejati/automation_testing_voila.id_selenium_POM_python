from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://voila.id/account/register"
        self.register_button = (By.CSS_SELECTOR, '[data-test-id="CT_component_register_submit"]')
        self.registers_button = (By.CSS_SELECTOR, '[data-test-id="CT_component_register_submit"]') #nonvisible
        self.please_error_message_text = (By.CSS_SELECTOR, "p._15kd2wejk._1ccbe2wc#base") 
        self.didnt_receive_code_text = (By.CSS_SELECTOR, "p._15kd2weow.wovzo5a._1ccbe2wb#base") 
        self.code_send_text = (By.CSS_SELECTOR, "p._15kd2weow._15r4f4dap._15r4f4dg9.wovzoqj._1ccbe2wb#base") 
        #self.dont_allow_button = (By.ID, 'moe-dontallow_button')


    def open(self):
        self.driver.get(self.url)  
        self.driver.maximize_window() 
        #self.click_dont_allow()


    def click_register_button(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.register_button)).click()
    
    def click_registers_button(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.registers_button)).click()

    def get_error_message_password(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.please_error_message_text)).text
    
    def get_didnt_receive_code_text(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.didnt_receive_code_text)).text

    def get_code_sent_text(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.code_send_text)).text
    
    # def click_dont_allow(self):
    #     WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.dont_allow_button)).click()