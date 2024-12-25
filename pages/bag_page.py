from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BagPage:
    def __init__ (self, driver):
        self.driver = driver
        self.bag_button = (By.CSS_SELECTOR, "[data-test-id='CT_Component_cartIcon']")
        self.add_to_bag_button = (By.CSS_SELECTOR, "[data-test-id='CT-add-to-bag-desktop']")
        self.choose_product_button = (By.CSS_SELECTOR, '[data-test-id="CT_component_product-item_Search-Result-Item"]')
        self.shopping_bag_text = (By.CSS_SELECTOR, "p._15r4f4daf._17zx15te8._17zx15ths._17zx15t80._17zx15t4g#base")
        self.valentino_text = (By.CSS_SELECTOR, "p._15kd2weog._17zx15ta8._17zx15tg0.clamp-2#base")
        self.remove_from_cart_button = (By.CSS_SELECTOR,"[data-test-id='CT_Component_removeSelectedCart']")
        self.confirm_to_remove_button = (By.CSS_SELECTOR,"[data-test-id='CT_Component_ConfirmContent_Ok']")
        self.shopping_bag_is_empty_text = (By.CSS_SELECTOR, "p._17zx15te8._17zx15t7k._17zx15tgg#base")
        self.uncheck_button = (By.CSS_SELECTOR, "[data-test-id='CT_Component_CartItemCheckbox']")
        self.increase_product = (By.CSS_SELECTOR, "[data-test-id='CT_Container_NumberStepper_Increase0']")
        self.product_price = (By.CSS_SELECTOR, "p._15kd2we74._17zx15te8._17zx15tgg._17zx15t9s._17zx15t9d#base")
        self.total_price = (By.CSS_SELECTOR, "p._15kd2we74._17zx15tgg._17zx15t9s._17zx15te8#base")

#Step Method

    def click_bag_button (self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.bag_button)).click()

    def click_add_to_bag_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_to_bag_button)).click()

    def click_choose_product_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.choose_product_button)).click()

    def get_shopping_bag_text(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.shopping_bag_text)).text
    
    def get_valentino_text(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.valentino_text)).text
    
    def click_remove_from_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.remove_from_cart_button)).click()

    def click_confirm_to_remove_from_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirm_to_remove_button)).click()

    def get_shopping_bag_is_empty_text(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.shopping_bag_is_empty_text)).text
    
    def click_checkbox_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.uncheck_button)).click()

    def click_increase_product(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.increase_product)).click()

    def get_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.product_price)).text

    def get_total_price(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.total_price)).text
    

    #Combined Step
    def add_to_bag_product(self):
        time.sleep(3)
        self.click_choose_product_button()
        self.click_add_to_bag_button()

    def remove_product_from_bag(self):
        time.sleep(3)
        self.click_remove_from_cart()
        self.click_confirm_to_remove_from_cart()

