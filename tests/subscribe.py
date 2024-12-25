from webdriver_setup import setup_webdriver
from pages.login_page import LoginPage
from pages.subscribe_page import SubscribePage


class TestSubscribe():
    def setup_method(self):
        self.driver = setup_webdriver()
        self.login_page = LoginPage(self.driver)
        self.subscribe_page = SubscribePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_subscribe_valid(self):
        self.login_page.unlogin()
        self.subscribe_page.set_subscribe("unsubscribedemail@gmail.com")
        print(f"Text found: {self.subscribe_page.get_subscribed_notification_text()}")
        assert self.subscribe_page.get_subscribed_notification_text() ==  ("Thanks for joining our community!")

    def test_subscribed_email_valid(self):
        self.login_page.unlogin()
        self.subscribe_page.set_subscribe("test@gmail.com")
        print(f"Text found: {self.subscribe_page.get_email_already_subscribed_text()}")
        assert self.subscribe_page.get_email_already_subscribed_text() == ("This email address is already subscribed, please try a different one.")
    
    def test_subscribe_invalid(self):
        self.login_page.unlogin()
        self.subscribe_page.set_subscribe("emailsalah")
        print(f"Text found: {self.subscribe_page.get_error_message_text()}")
        assert self.subscribe_page.get_error_message_text() == ("Please enter your email address in format: yourname@example.com")

    def test_subscribe_empty_field_invalid(self):
        self.login_page.unlogin()
        self.subscribe_page.set_subscribe("")
        print(f"Text found: {self.subscribe_page.get_error_message_text()}")
        assert self.subscribe_page.get_error_message_text() == ("Please enter your email address in format: yourname@example.com")