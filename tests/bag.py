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
        

    # def test_click_bag_button_without_login_invalid(self):
    #     self.login_page.unlogin()
    #     self.bag_page.click_bag_button()
    #     assert self.login_page.get_sign_in_to_shop_text() == ("Sign in to shop with vouchers, track your order, and save your favorite products.")

    # def test_add_product_to_bag_without_login_invalid(self):
    #     self.login_page.unlogin()
    #     self.search_page.search("Rockstud Strappy Sandal Flats Light Ivory Ghw")
    #     self.bag_page.add_to_bag_product()
    #     assert self.login_page.get_sign_in_to_shop_text() == ("Sign in to shop with vouchers, track your order, and save your favorite products.")

    # def test_add_product_to_bag_valid(self):
    #     self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
    #     self.search_page.search("Rockstud Strappy Sandal Flats Light Ivory Ghw")
    #     self.bag_page.add_to_bag_product()
    #     self.bag_page.click_bag_button()
    #     assert self.bag_page.get_shopping_bag_text() == ("Shopping Bag")
    #     assert self.bag_page.get_valentino_text() == ("Rockstud Strappy Sandal Flats Light Ivory Ghw")

    # def test_remove_product_from_bag(self):
    #     self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
    #     self.bag_page.click_bag_button()
    #     self.bag_page.remove_product_from_bag()
    #     assert self.bag_page.get_shopping_bag_is_empty_text() == ("Your shopping bag is empty")
        
    # def test_total_price_calculation(self):
    #     self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
    #     self.search_page.search("Cassette Tri-Fold Zip Wallet Emerald Travertine")
    #     self.bag_page.add_to_bag_product()
    #     self.bag_page.click_bag_button()
    #     #time.sleep(3)

    #     product_price = self.bag_page.get_product_price()
    #     quantity = 4
    #     for _ in range(quantity):
    #         self.bag_page.click_increase_product()
    #     cart_total_price = self.bag_page.get_total_price()
    #     expected_total_price = product_price * quantity
    #     time.sleep(15)
    #     if cart_total_price == expected_total_price:
    #         print(f"Total harga di keranjang sesuai: {cart_total_price}")
    #     else:
    #         print(f"Total harga di keranjang tidak sesuai! Diharapkan: {expected_total_price}, tetapi ditemukan: {cart_total_price}")


    def test_total_price_calculation(self):

        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")

        self.search_page.search("Cassette Tri-Fold Zip Wallet Emerald Travertine")
        self.bag_page.add_to_bag_product() 
        self.bag_page.click_bag_button()  

        time.sleep(3)

        for _ in range(2):  
            self.bag_page.click_increase_product()
        time.sleep(3)    
        product_price = self.bag_page.get_product_price()
        expected_total_price = product_price * 3 
        
        cart_total_price = self.bag_page.get_total_price()
        time.sleep(3)
        assert cart_total_price == expected_total_price, (
            f"Total harga di keranjang tidak sesuai! "
            f"Diharapkan: {expected_total_price}, tetapi ditemukan: {cart_total_price}"
        )
        print(f"Total harga di keranjang sesuai: {cart_total_price}")