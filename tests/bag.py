import time
from webdriver_setup import setup_webdriver
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.bag_page import BagPage



class TestSearch():
    def setup_method(self):
        self.driver = setup_webdriver()
        self.login_page = LoginPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.bag_page = BagPage(self.driver)

    def teardown_method(self):
        self.driver.quit()
        

    def test_click_bag_button_without_login_invalid(self):
        self.login_page.unlogin()
        self.bag_page.click_bag_button()
        assert self.login_page.get_sign_in_to_shop_text() == ("Sign in to shop with vouchers, track your order, and save your favorite products.")

    def test_add_product_to_bag_without_login_invalid(self):
        self.login_page.unlogin()
        self.search_page.search("Rockstud Strappy Sandal Flats Light Ivory Ghw")
        self.bag_page.add_to_bag_product()
        assert self.login_page.get_sign_in_to_shop_text() == ("Sign in to shop with vouchers, track your order, and save your favorite products.")

    def test_add_product_to_bag_valid(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.search_page.search("Rockstud Strappy Sandal Flats Light Ivory Ghw")
        self.bag_page.add_to_bag_product()
        self.bag_page.click_bag_button()
        assert self.bag_page.get_shopping_bag_text() == ("Shopping Bag")
        assert self.bag_page.get_valentino_text() == ("Rockstud Strappy Sandal Flats Light Ivory Ghw")

    def test_remove_product_from_bag(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.bag_page.click_bag_button()
        self.bag_page.remove_product_from_bag()
        assert self.bag_page.get_shopping_bag_is_empty_text() == ("Your shopping bag is empty")

    def test_add_product_to_bag_and_verify_after_logout_and_login(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.search_page.search("Rockstud Strappy Sandal Flats Light Ivory Ghw")
        self.bag_page.add_to_bag_product()
        self.bag_page.click_bag_button()
        time.sleep(3)
        self.login_page.click_profile_button()
        self.login_page.click_sign_out1()
        self.login_page.click_sign_out2()
        time.sleep(5)
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.bag_page.click_bag_button()
        assert self.bag_page.get_shopping_bag_text() == ("Shopping Bag")
        assert self.bag_page.get_valentino_text() == ("Rockstud Strappy Sandal Flats Light Ivory Ghw")
