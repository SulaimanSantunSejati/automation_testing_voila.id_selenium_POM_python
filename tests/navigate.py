import time
from webdriver_setup import setup_webdriver
from pages.login_page import LoginPage
from pages.navigate_pages import NavigatePage

class TestNavigate():
    def setup_method(self):
        self.driver = setup_webdriver()
        self.login_page = LoginPage(self.driver)
        self.navigate_page = NavigatePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    #Official Store

    def test_navigate_tokopedia_link(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_tokopedia_button_navigate()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url = "https://www.tokopedia.com/voilaid"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_to_shopee_link(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_shopee_button_navigate()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url = "https://shopee.co.id/voila.id_officialshop"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_to_blibli_link(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_blibli_button_navigate()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url = "https://www.blibli.com/challenge/landing/?redirect=%2Fmerchant%2Fvoila-id%2FVOI-70003%3Fpage%3D1%26start%3D0%26pickupPointCode%3DPP-3176345%26cnc%3D%26multiCategory%3Dtrue%26excludeProductList%3Dtrue%26promoTab%3Dfalse%26sort%3D7"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_tiktok_link(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_tiktok_button_navigate()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url = "https://www.tiktok.com/@voila.id?lang=en"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_zalora_link(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_zalora_button_navigate()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url = "https://www.zalora.co.id/store/voila-id"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"
        
    #About Us

    def test_navigate_about_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_about_button_navigate()
        time.sleep(5)
        expected_url = "https://edit.voila.id/about/"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_our_boutiques_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_our_boutiques_button_navigate()
        time.sleep(5)
        expected_url = "https://edit.voila.id/our-boutiques/"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_blog_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_blog_button_navigate()
        time.sleep(5)
        expected_url = "https://edit.voila.id/"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_promotions_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_promotions_button_navigate()
        time.sleep(7)
        expected_part = "/promotions/"
        actual_url = self.driver.current_url
        assert expected_part in actual_url, f"Expected URL to contain '{expected_part}', but got: {actual_url}"

    def test_navigate_program_and_partnership_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_program_and_partnership_button_navigate()
        time.sleep(5)
        expected_url = "https://voila.id/pages/programs-and-partnerships"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_shop_by_request_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_shop_by_request_button_navigate()
        time.sleep(5)
        expected_url = "https://voila.id/pages/shop-by-request"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_careers_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_careers_button_navigate()
        time.sleep(5)
        expected_url = "https://ctlyst.freshteam.com/jobs"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_voilàid_x_KayaLeathers_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        self.navigate_page.click_voilàid_x_KayaLeathers_button_navigate()
        time.sleep(5)
        expected_url = "https://edit.voila.id/voila-kaya/"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

#Customer Service

    def test_navigate_contact_us_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        time.sleep(3)
        self.navigate_page.click_contact_us_button_navigate()
        time.sleep(3)
        expected_url = "https://edit.voila.id/contact/"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_help_center_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        time.sleep(3)
        self.navigate_page.click_help_center_button_navigate()
        time.sleep(3)
        expected_url = "https://helpcenter.voila.id/hc/id"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_terms_and_conditions_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        time.sleep(5)
        self.navigate_page.click_terms_and_conditions_button_navigate()
        time.sleep(3)
        expected_url = "https://edit.voila.id/terms-and-conditions/"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_privacy_policy_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(5300)
        time.sleep(5)
        self.navigate_page.click_privacy_policy_button_navigate()
        time.sleep(3)
        expected_url = "https://edit.voila.id/privacy-policy/"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    #Social Media

    def test_navigate_instagram_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(6000)
        self.navigate_page.click_instagram_voila_button_navigate()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url = "https://www.instagram.com/voila.id/"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_tiktok_voila_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(6000)
        self.navigate_page.click_tiktok_voila_button_navigate()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])    
        expected_url = "https://www.tiktok.com/@voila.id?lang=en"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_youtube_voila_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(6000)
        self.navigate_page.click_youtube_voila_button_navigate()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url = "https://www.youtube.com/channel/UCYkAZ9ERvRASlKhIqrGpeQA"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_facebook_voila_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(6000)
        self.navigate_page.click_facebook_voila_button_navigate()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url = "https://www.facebook.com/voilalux"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    # Voila App

    def test_navigate_google_play_store_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(4400)
        time.sleep(5)
        self.navigate_page.click_google_play_store_button_navigate()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url = "https://play.google.com/store/apps/details?id=com.voila.id&pli=1"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    def test_navigate_apple_store_page(self):
        self.login_page.unlogin()
        self.navigate_page.scroll_to_position(4400)
        time.sleep(5)
        self.navigate_page.click_apple_store_button_navigate()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url = "https://apps.apple.com/id/app/voil%C3%A0-id/id1560619001?l=id"
        actual_url = self.driver.current_url 
        assert expected_url == actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"






