import time
from webdriver_setup import setup_webdriver
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.bag_page import BagPage
from pages.checkout_page import CheckoutPage


class TestCheckout:
    def setup_method (self, driver):
        self.driver = driver
        self.driver = setup_webdriver()
        self.login_page = LoginPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.bag_page = BagPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_checkout_shop_by_whatsapp_valid(self):
        self.login_page.unlogin()
        self.search_page.search("Chypre Calfskin Sandals Black Women")
        self.bag_page.add_to_bag_product()
        #time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url = "https://web.whatsapp.com/send?text=Hi%20voil%C3%A0,%20I%E2%80%99d%20like%20to%20order%20Chypre%20Calfskin%20Sandals%20Black%20Women.%20Please%20inform%20me%20of%20the%20process%20and%20assist%20me%20with%20the%20next%20steps.%20https://voila.id/products/hermes-chypre-calfskin-sandals-black-women-19818&phone=+62818683683"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_checkout_without_select_shipment_or_payment_method_invalid(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.search_page.search("Cassette Tri-Fold Zip Wallet Emerald Travertine")
        self.bag_page.add_to_bag_product()
        self.bag_page.click_bag_button()
        self.checkout_page.click_checkout()
        self.checkout_page.click_place_order_button()
        assert self.checkout_page.get_alert_cant_proceed_text() == ("Select shipping service and payment method to place order.")

    def test_checkout_without_payment_method_invalid(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.search_page.search("Cassette Tri-Fold Zip Wallet Emerald Travertine")
        self.bag_page.add_to_bag_product()
        self.bag_page.click_bag_button()
        self.checkout_page.click_checkout()
        self.checkout_page.select_shipping_service()
        self.checkout_page.click_place_order_button()
        assert self.checkout_page.get_alert_cant_proceed_text() == ("Select payment method to place order.")

    def test_checkout_without_select_shipment(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.search_page.search("Cassette Tri-Fold Zip Wallet Emerald Travertine")
        self.bag_page.add_to_bag_product()
        self.bag_page.click_bag_button()
        time.sleep(3)
        self.checkout_page.click_checkout()
        self.checkout_page.select_payment_method_with_virtual_account()
        self.checkout_page.click_place_order_button()
        assert self.checkout_page.get_alert_cant_proceed_text() == ("Select shipping service to place order.")

    def test_checkout_valid_with_virtual_account(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.search_page.search("Cassette Tri-Fold Zip Wallet Emerald Travertine")
        self.bag_page.add_to_bag_product()
        self.bag_page.click_bag_button()
        time.sleep(3)
        self.checkout_page.click_checkout()
        self.checkout_page.select_shipping_service()
        self.checkout_page.select_payment_method_with_virtual_account()
        self.checkout_page.click_place_order_button()
        assert self.checkout_page.get_alert_order_success() == ("Order has been placed")

    def test_checkout_valid_with_bank_transfer(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.search_page.search("Cassette Tri-Fold Zip Wallet Emerald Travertine")
        self.bag_page.add_to_bag_product()
        time.sleep(3)
        self.bag_page.click_bag_button()
        time.sleep(3)
        self.checkout_page.click_checkout()
        self.checkout_page.select_shipping_service()
        self.checkout_page.select_payment_method_with_bank_transfer()
        self.checkout_page.click_place_order_button()
        assert self.checkout_page.get_alert_order_success() == ("Order has been placed")


    def test_checkout_without_select_product(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.search_page.search("Cassette Tri-Fold Zip Wallet Emerald Travertine")
        self.bag_page.add_to_bag_product()
        self.bag_page.click_bag_button()
        self.checkout_page.click_checkbox()
        time.sleep(3)
        self.checkout_page.click_checkout()
        assert self.checkout_page.get_alert_select_product_to_checkout() == ("Select product to checkout.")

    def test_checkout_and_cancel_order(self):
        self.login_page.login("fihokob723@aqqor.com", "Tonoyoga999")
        self.search_page.search("Cassette Tri-Fold Zip Wallet Emerald Travertine")
        self.bag_page.add_to_bag_product()
        self.bag_page.click_bag_button()
        # time.sleep(3)
        self.checkout_page.click_checkout()
        time.sleep(3)
        self.checkout_page.select_shipping_service()
        self.checkout_page.select_payment_method_with_virtual_account()
        self.checkout_page.click_place_order_button()
        self.checkout_page.click_check_order_status()
        self.checkout_page.cancel_order()
        time.sleep(3)
        assert self.checkout_page.get_alert_canceled_order() == ("Order Canceled")