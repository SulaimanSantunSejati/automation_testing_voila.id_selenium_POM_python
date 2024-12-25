from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WishlistPage :
    def __init__ (self,driver):
        self.driver = driver
        self.choose_product_button = (By.CSS_SELECTOR, '[data-test-id="CT_component_product-item_Search-Result-Item"]')
        self.wishlist_button = (By.CSS_SELECTOR, "[data-test-id='CT-PDP-Add-to-Wishlist']")
        self.product_on_wishlist = (By.CSS_SELECTOR, '[data-test-id="CT-wishlist-link"]')
        self.wishlist_text = (By.CSS_SELECTOR, "p._17zx15t4g._1ccbe2w2#base")
        self.item_on_wishlist = (By.CSS_SELECTOR, "p._15r4f4dg9._1ccbe2wb#base")
        self.edit_wishlist_button = (By.CSS_SELECTOR, "[data-test-id='CT-Wishlist-Edit']")
        self.to_check_item = (By.CSS_SELECTOR, 'button.glci2q5.glci2q7')
        self.remove_wishlist_button = (By.CSS_SELECTOR, 'button._920fuu5._920fuue._920fuub._920fuu6._920fuui')
        self.confirm_to_remove_button = (By.CSS_SELECTOR, 'button._920fuu5._920fuuf._920fuub._920fuu6._920fuui')                                            
        self.wishlist_empty_text = (By.CSS_SELECTOR, "p._15kd2we1f4._17zx15tm8._17zx15te8._1ccbe2wa#base")


#step method
    def click_product_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.choose_product_button)).click()

    def click_wishlist_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.wishlist_button)).click()  

    def click_heart_wishlist_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.product_on_wishlist)).click()

    def get_wishlist_text(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.wishlist_text)).text
    
    def get_item_on_wishlist(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.item_on_wishlist)).text
    
    def click_edit_wishlist_button(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.edit_wishlist_button)).click() 
       
    def click_item_to_check(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.to_check_item)).click()

    def click_remove_wishlist_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.remove_wishlist_button)).click()

    def click_confirm_remove_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.confirm_to_remove_button)).click()
   
    def get_wishlist_empty_text(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.wishlist_empty_text)).text