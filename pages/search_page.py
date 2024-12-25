from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class SearchPage:
    def __init__(self,driver):
        self.driver = driver
        self.search_box =(By.CSS_SELECTOR, "[data-test-id='CT-Search']")
        self.search_box_input = (By.CSS_SELECTOR, "[data-test-id='CT-Search-Input']")
        self.filter_text = (By.CSS_SELECTOR,"p._17zx15te8._1ccbe2w9#base") 
        self.search_result_not_found_text = (By.CSS_SELECTOR, "p._15kd2we1f4._17zx15tm8._17zx15te8._1ccbe2wa#base")
        self.search_result_invalid_found_text = (By.CSS_SELECTOR, "p._15kd2we1f4._15kd2weow._17zx15tm8._1ccbe2wb#base")
        self.search_specific_item_text = (By.CSS_SELECTOR, "p._15r4f4dg9._1ccbe2wb#base")
        self.logo_nike = (By.CSS_SELECTOR,'img[alt="Nike"]')


#step method
    def click_search(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.search_box)).click()

    def get_filter_text(self):
        return WebDriverWait (self.driver, 20).until(EC.visibility_of_element_located(self.filter_text)).text
    
    def search_for_item(self, item): 
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.search_box_input)).send_keys(item) 
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.search_box_input)).send_keys(Keys.RETURN)

    def get_not_found_text(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.search_result_not_found_text)).text
    
    def get_invalid_found_text(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.search_result_invalid_found_text)).text
    
    def get_specific_item_text(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.search_specific_item_text)).text
    
    def get_logo_nike(self):
        logo_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.logo_nike))
        return logo_element.get_attribute("alt")


#combined step method
    def search(self, item):
        self.click_search()
        self.search_for_item(item)






    