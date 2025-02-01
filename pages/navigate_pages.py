from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NavigatePage:
    def __init__ (self, driver):
        self.driver = driver
        #Official Store
        self.tokopedia_button = (By.CSS_SELECTOR, 'img[alt="tokopedia"]')
        self.shopee_button = (By.CSS_SELECTOR, 'img[alt="shopee"]')
        self.blibli_button = (By.CSS_SELECTOR, 'img[alt="blibli"]')
        self.tiktok_button = (By.CSS_SELECTOR, 'img[alt="tiktok"]')
        self.zalora_button = (By.CSS_SELECTOR, 'img[alt="zalora"]')

       #About Us
        self.about_button = (By.CSS_SELECTOR, "a[href='https://edit.voila.id/about']")
        self.our_boutiques_button = (By.CSS_SELECTOR,'a[href="https://edit.voila.id/our-boutiques"]')
        self.blog_button = (By.CSS_SELECTOR,'a[href="https://edit.voila.id"]')
        #self.promotions_button = (By.XPATH,'//a[normalize-space()="Promotions"]')
        self.promotions_button = (By.CSS_SELECTOR,'a[href*="https://voila.id/promotions"]')
        self.program_and_partnership_button = (By.CSS_SELECTOR,'a[href="https://voila.id/pages/programs-and-partnerships"]')
        self.shop_by_request_button = (By.CSS_SELECTOR,'a[href="https://voila.id/pages/shop-by-request"]')
        self.careers_button = (By.CSS_SELECTOR,'a[href="https://career.ctlyst.id/jobs"]')
        self.voilaid_x_kaya_leathers_button = (By.CSS_SELECTOR,'a[href="https://edit.voila.id/voila-kaya"]')

       #Customer Service
        self.contact_us_button = (By.CSS_SELECTOR,'a[href="https://edit.voila.id/contact"]')
        self.help_center_button = (By.CSS_SELECTOR,'a[href="https://helpcenter.voila.id/hc/id"]')
        self.terms_and_conditions_button = (By.CSS_SELECTOR,'a[href="https://edit.voila.id/terms-and-conditions"]')
        self.privacy_policy_button = (By.CSS_SELECTOR,'a[href="https://edit.voila.id/privacy-policy"]')

        #Social Media
        self.instagram_voila_button = (By.CSS_SELECTOR, 'a[href="https://www.instagram.com/voila.id/"]')
        self.tiktok_voila_button = (By.CSS_SELECTOR, 'a[href="https://www.tiktok.com/@voila.id?lang=en"]')
        self.youtube_voila_button = (By.CSS_SELECTOR, 'a[href="https://www.youtube.com/channel/UCYkAZ9ERvRASlKhIqrGpeQA"]')
        self.facebook_voila_button = (By.CSS_SELECTOR, 'a[href="https://www.facebook.com/voilalux"]')

        # Voila App
        self.google_play_store_button = (By.CSS_SELECTOR, 'a[href="https://play.google.com/store/apps/details?id=com.voila.id&pli=1"]')
        self.apple_store_button = (By.CSS_SELECTOR, 'a[href="https://apps.apple.com/id/app/voila-id/id1560619001?l=id"]')
        #self.google_playstore_button = (By.CSS_SELECTOR, '.vds-container > #base > #base > #base > .rdkhex8:nth-child(1) img')
        #self.apple_store_button = (By.CSS_SELECTOR, '.vds-container > #base > #base > #base > .rdkhex8:nth-child(2) img')


    def scroll_to_position(self, y_position): self.driver.execute_script(f"window.scrollTo(0, {y_position});")

    #Official Store
    def click_tokopedia_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.tokopedia_button)).click()

    def click_shopee_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.shopee_button)).click()

    def click_blibli_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.blibli_button)).click()

    def click_tiktok_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.tiktok_button)).click()

    def click_zalora_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.zalora_button)).click()

    #About Us
    def click_about_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.about_button)).click()
    
    def click_our_boutiques_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.our_boutiques_button)).click()   

    def click_blog_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.blog_button)).click()   

    def click_promotions_button_navigate(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.promotions_button)).click()   

    def click_program_and_partnership_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.program_and_partnership_button)).click()   

    def click_shop_by_request_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.shop_by_request_button)).click()   

    def click_careers_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.careers_button)).click()   

    def click_voilàid_x_KayaLeathers_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.voilaid_x_kaya_leathers_button)).click()   

    #Customer Service

    def click_contact_us_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.contact_us_button)).click()   
    
    def click_help_center_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.help_center_button)).click()   
    
    def click_terms_and_conditions_button_navigate(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.terms_and_conditions_button)).click()   

    def click_privacy_policy_button_navigate(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.privacy_policy_button)).click()   

    #Social media
    def click_instagram_voila_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.instagram_voila_button)).click()   
    
    def click_tiktok_voila_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.tiktok_voila_button)).click()   
    
    def click_youtube_voila_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.youtube_voila_button)).click()   
    
    def click_facebook_voila_button_navigate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.facebook_voila_button)).click()   
    

    #Voila App
    def click_google_play_store_button_navigate(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.google_play_store_button)).click()   

    def click_apple_store_button_navigate(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.apple_store_button)).click()   
    
