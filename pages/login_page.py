from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        
        self.driver = driver
        self.url_login = "https://voila.id/account/login"
        self.url_unlogin = "https://voila.id/"
        self.username_input = (By.NAME, "identifier")
        #self.username_input = (By.XPATH, "//div[@class='yihd6a0 ldkv8w0']//input[@name='identifier']")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "[data-test-id='CT_component_login_submit']")
        self.logins_button = (By.CSS_SELECTOR, "[data-test-id='CT_component_login_submit']")
        self.greeting_text = (By.CSS_SELECTOR, "p._15kd2weps._17zx15tdc._1ccbe2wb#base")
        self.profile_button = (By.CSS_SELECTOR,'[data-test-id="CT_Component_ProfileMenu"]')
        self.sign_out_button1 = (By.CSS_SELECTOR, '[data-test-id="CT_account_navigation-item_Sign Out"]') 
        self.sign_out_button2 = (By.CSS_SELECTOR, '[data-test-id="CT_SignOut_Confirm"]')
        self.sign_in_text = (By.CSS_SELECTOR, "[data-test-id='CT-SignIn-Btn']")
        self.register_text = (By.CSS_SELECTOR, "[data-test-id='CT-Register-Btn']")
        self.unregist_text = (By.CSS_SELECTOR, "._15kd2weog._17zx15t9c._17zx15t6p._17zx15tgg._17zx15thd._17zx15te8._17zx15t4g#base") #masih salah
        self.invalid_pass_text = (By.CSS_SELECTOR, "._7q2fqh7#base") 
        self.empty_email_text = (By.CSS_SELECTOR, "p._15kd2wejk._1ccbe2wc#base") 
        self.forgot_password_button1 = (By.CSS_SELECTOR, 'p._5y0pl50._5y0pl5e._5y0pl5a#base')
        self.forgot_password_button2 = (By.CSS_SELECTOR, "button._920fuu5._920fuug._920fuub._920fuu6[data-test-id='CT_Component_UpdatePassword_Submit']")
        self.forgot_password_text = (By.CSS_SELECTOR, "p._15kd2weow._15r4f4dap._15r4f4dg9.wovzoqj._1ccbe2wb#base")
        self.sign_in_to_shop_text = (By.CSS_SELECTOR, "p._15kd2weow.wovzoqj._17zx15ta8._17zx15t7l._17zx15tg0._17zx15tgh#base")
        #self.dont_allow_button = (By.ID, 'moe-dontallow_button')

    def open(self):
        self.driver.get(self.url_login)
        self.driver.maximize_window()
        #self.click_dont_allow()

    def set_username(self, username):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.username_input)).send_keys(username)

    def set_password(self, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.login_button)).click()

    # def click_dont_allow(self): 
    #     WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.dont_allow_button)).click()

    def login(self, username, password):
        self.driver.get(self.url_login)
        #self.click_dont_allow()
        self.driver.maximize_window()
        self.set_username(username)
        self.set_password(password)
        self.click_login()

    def unlogin(self):
        self.driver.get(self.url_unlogin)
        self.driver.maximize_window()
        #self.click_dont_allow()

    def click_logins(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.logins_button)).click()

    def get_greeting_text(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.greeting_text)).text
    
    def click_profile_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.profile_button)).click()

    def click_sign_out1(self): 
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sign_out_button1)).click() 

    def click_sign_out2(self): 
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sign_out_button2)).click()

    def get_sign_in_text(self): 
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.sign_in_text)).text 

    def get_register_text(self): 
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.register_text)).text

    def get_unregist_text(self): 
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.unregist_text)).text
   
    def get_invalid_pass_text(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.invalid_pass_text)).text
    
    def get_empty_email_text(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.empty_email_text)).text
    
    def click_forgot_password1(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.forgot_password_button1)).click()

    def click_forgot_password2(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.forgot_password_button2)).click()

    def get_forgot_password_text(self):
        return WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.forgot_password_text)).text

    def get_sign_in_to_shop_text(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.sign_in_to_shop_text)).text

