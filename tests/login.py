import time
from webdriver_setup import setup_webdriver
from pages.login_page import LoginPage


class TestLogin():
    def setup_method(self):
        self.driver =setup_webdriver()
        self.login_page = LoginPage(self.driver)
  
    def teardown_method(self):
        self.driver.quit()
        
    def test_login_success(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        time.sleep(5)
        assert self.login_page.get_greeting_text() == "Hi, Tono!"

    def test_login_logout_success(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.login_page.click_profile_button()
        self.login_page.click_sign_out1()
        self.login_page.click_sign_out2()
        time.sleep(3)
        assert self.login_page.get_sign_in_text() == "Sign In"
        assert self.login_page.get_register_text() == "Register"  

    def test_login_unregistered(self):
        self.login_page.open()
        self.login_page.set_username("blabla123@gmail.com")
        self.login_page.click_login()
        time.sleep(5)
        assert self.login_page.get_unregist_text() == "Register"

    def test_login_invalid_password(self):
        self.login_page.login("fihokob723@aqqor.com", "Invalidpassword123")
        time.sleep(5)
        assert self.login_page.get_invalid_pass_text() == "Your account ID or password is incorrect. Please try again."

    def test_login_invalid_email(self):
        self.login_page.open()
        self.login_page.set_username("invalidemail")
        self.login_page.click_logins()
        time.sleep(5)
        assert self.login_page.get_empty_email_text() == "Please enter a valid email format or phone number."
    
    def test_login_empty_username(self):
        self.login_page.open()
        self.login_page.set_username("")
        self.login_page.click_logins()
        time.sleep(5)
        assert self.login_page.get_empty_email_text() == "Please enter email or phone number."
        
    def test_login_forgot_password(self):
        self.login_page.open()
        self.login_page.set_username("fihokob723@aqqor.com")
        self.login_page.click_forgot_password1()
        time.sleep(5)
        self.login_page.set_username("fihokob723@aqqor.com")
        self.login_page.click_forgot_password2()
        time.sleep(5)
        assert self.login_page.get_forgot_password_text() == "Enter the verification code we sent to your registered email."  