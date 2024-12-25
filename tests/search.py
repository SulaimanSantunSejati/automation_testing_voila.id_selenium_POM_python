import time
from webdriver_setup import setup_webdriver
from pages.login_page import LoginPage
from pages.search_page import SearchPage


class TestSearch():
    def setup_method(self):
        self.driver = setup_webdriver()
        self.login_page = LoginPage(self.driver)
        self.search_page = SearchPage(self.driver)

    def teardown_method(self):
        self.driver.quit()
    
    def test_search_special_characters_invalid(self):
        self.login_page.unlogin()
        self.search_page.search("!@#$%")
        time.sleep(5)
        print(f"Text found: {self.search_page.get_not_found_text()}")
        assert self.search_page.get_not_found_text() == "Product not found"
        print(f"Text found: {self.search_page.get_invalid_found_text()}")
        assert self.search_page.get_invalid_found_text() == "We can’t find any products that matches your search. Please try another keyword."

    def test_search_empty_invalid(self):
        self.login_page.unlogin()
        self.search_page.search("")
        time.sleep(5)
        print(f"Text found: {self.search_page.get_not_found_text()}")
        assert self.search_page.get_not_found_text() == "Product not found"
        print(f"Text found: {self.search_page.get_invalid_found_text()}")
        assert self.search_page.get_invalid_found_text() == "We can’t find any products that matches your search. Please try another keyword."

    def test_search_missing_items_invalid(self):
        self.login_page.unlogin()
        self.search_page.search("jengkol")
        time.sleep(5)
        print(f"Text found: {self.search_page.get_not_found_text()}")
        assert self.search_page.get_not_found_text() == "Product not found"
        print(f"Text found: {self.search_page.get_invalid_found_text()}")
        assert self.search_page.get_invalid_found_text() == "We can’t find any products that matches your search. Please try another keyword."

    def test_search_specific_item_valid(self):
        self.login_page.unlogin()
        self.search_page.search("Bon Bon 32 - RH32-13 Ceramic Playful Multicolor Dial Pink Rubber Strap")
        time.sleep(5)
        print(f"Text found: {self.search_page.get_specific_item_text()}")
        assert self.search_page.get_specific_item_text() == "Bon Bon 32 - RH32-13 Ceramic Playful Multicolor Dial Pink Rubber Strap"

    def test_search_price_invalid(self):
        self.login_page.unlogin()
        self.search_page.search("Rp. 2.890.000")
        time.sleep(5)
        print(f"Text found: {self.search_page.get_not_found_text()}")
        assert self.search_page.get_not_found_text() == "Product not found"
        print(f"Text found: {self.search_page.get_invalid_found_text()}")
        assert self.search_page.get_invalid_found_text() == "We can’t find any products that matches your search. Please try another keyword."

    def test_search_specific_brand_valid(self):
        self.login_page.unlogin()
        self.search_page.search("nike")
        time.sleep(5)
        print(f"Text found: {self.search_page.get_filter_text()}")
        assert self.search_page.get_filter_text() == "Filter"
        print(f"Text found: {self.search_page.get_logo_nike()}")
        assert self.search_page.get_logo_nike() == "Nike"
        