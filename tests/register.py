import time
from webdriver_setup import setup_webdriver
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

class TestRegister():
    def setup_method(self):
        self.driver = setup_webdriver()
        self.login_page = LoginPage(self.driver)
        self.register_page = RegisterPage (self.driver)

    def teardown_method(self):
        self.driver.quit()
    
    def test_register_invalid_email(self):
        self.register_page.open()
        self.login_page.set_username("invalidemail")
        self.login_page.set_password("Password123")
        self.register_page.click_registers_button()
        assert self.register_page.get_error_message_password() == ("Please enter a valid email format or phone number.")

    def test_register_password_invalid1(self):
        self.register_page.open()
        self.login_page.set_username("emailvalid@gmail.com")
        self.login_page.set_password("AAAAAAAAAAaaaaaaaaaaa")
        self.register_page.click_registers_button()
        assert self.register_page.get_error_message_password() == ("Password must be at most 20 characters.") 
        
    def test_register_password_invalid2(self):
        self.register_page.open()
        self.login_page.set_username("emailvalid@gmail.com")
        self.login_page.set_password("12345678")
        self.register_page.click_registers_button()
        assert self.register_page.get_error_message_password() == ("Password must be at least 6 characters with uppercase letters, lowercase letters, and numbers.")

    def test_register_empty_password_invalid(self):
        self.register_page.open()
        self.login_page.set_username("emailvalid@gmail.com")
        self.login_page.set_password("")
        self.register_page.click_registers_button()
        assert self.register_page.get_error_message_password() == ("Please create a password.")

    def test_register_empty_email_or_phone_number_invalid(self):
        self.register_page.open()
        self.login_page.set_username("")
        self.register_page.click_registers_button()
        assert self.register_page.get_error_message_password() == ("Please enter email or phone number.")
        
    def test_register_phone_number_valid(self):
        self.register_page.open()
        self.login_page.set_username("088562772152")
        self.login_page.set_password("Password123")
        self.register_page.click_register_button()
        assert self.register_page.get_code_sent_text() == "Enter the verification code we sent to your registered phone number."

    def test_register_email_valid(self):
        self.register_page.open()
        self.login_page.set_username("emailvaliddd@gmail.com")
        self.login_page.set_password("Password123")
        self.register_page.click_register_button()
        assert self.login_page.get_forgot_password_text() == "Enter the verification code we sent to your registered email."

    def test_register_with_existing_account(self):
        self.register_page.open()
        self.login_page.set_username("fihokob723@aqqor.com")
        self.login_page.set_password("Password123")
        self.register_page.click_register_button()
        assert self.login_page.get_sign_in_to_shop_text() == ("Sign in to shop with vouchers, track your order, and save your favorite products.")


