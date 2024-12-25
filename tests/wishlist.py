from webdriver_setup import setup_webdriver
import time
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.wishlist_page import WishlistPage

class TestWishlist():
    def setup_method(self):
        self.driver = setup_webdriver()
        self.login_page = LoginPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.wishlist_page = WishlistPage(self.driver)
  
    def teardown_method(self):
        self.driver.quit()

    def test_add_product_to_wishlist_without_login_invalid(self):
        self.login_page.unlogin()
        self.search_page.search("Bon Bon 32 - RH32-13 Ceramic Playful Multicolor Dial Pink Rubber Strap")
        time.sleep(2)
        self.wishlist_page.click_product_button()
        self.wishlist_page.click_wishlist_button()
        time.sleep(5)
        assert self.login_page.get_sign_in_to_shop_text() == ("Sign in to shop with vouchers, track your order, and save your favorite products.")

    def test_wishlist_valid(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        time.sleep(3)
        self.search_page.search("Bon Bon 32 - RH32-13 Ceramic Playful Multicolor Dial Pink Rubber Strap")
        time.sleep(5)
        self.wishlist_page.click_product_button()
        self.wishlist_page.click_wishlist_button()
        time.sleep(5)
        self.wishlist_page.click_heart_wishlist_button()
        assert self.wishlist_page.get_wishlist_text() == ("Wishlist")
        assert self.wishlist_page.get_item_on_wishlist() == ("Bon Bon 32 - RH32-13 Ceramic Playful Multicolor Dial Pink Rubber Strap")

    def test_remove_wishlist_product(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        time.sleep(5)
        self.wishlist_page.click_heart_wishlist_button()
        time.sleep(5)
        self.wishlist_page.click_edit_wishlist_button()
        time.sleep(5)
        self.wishlist_page.click_item_to_check()
        time.sleep(3)
        self.wishlist_page.click_remove_wishlist_button()
        self.wishlist_page.click_confirm_remove_button()
        assert self.wishlist_page.get_wishlist_empty_text() == ("Your wishlist is empty")


    def test_click_wishlist_button_without_login_invalid(self):
        self.login_page.unlogin()
        self.wishlist_page.click_heart_wishlist_button()
        assert self.login_page.get_sign_in_to_shop_text() == ("Sign in to shop with vouchers, track your order, and save your favorite products.")
        
    def test_wishlist_after_logout(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.search_page.click_search()
        self.search_page.search_for_item("Bon Bon 32 - RH32-13 Ceramic Playful Multicolor Dial Pink Rubber Strap")
        time.sleep(5)
        self.wishlist_page.click_product_button()
        self.wishlist_page.click_wishlist_button()
        time.sleep(3)
        self.login_page.click_profile_button()
        self.login_page.click_sign_out1()
        self.login_page.click_sign_out2()
        time.sleep(5)
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.wishlist_page.click_heart_wishlist_button()
        assert self.wishlist_page.get_wishlist_text() == ("Wishlist")
        assert self.wishlist_page.get_item_on_wishlist() == ("Bon Bon 32 - RH32-13 Ceramic Playful Multicolor Dial Pink Rubber Strap")
        