from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckoutPage:
    def __init__ (self, driver):
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, "[data-test-id='CT_Component_btnCheckout']")
        #self.select_shipping_method = (By.CSS_SELECTOR, "p._15kd2weog._15r4f4dmn._17zx15tdc._1ccbe2wb#base") 
        self.select_shipping_method = (By.XPATH, '//div[@data-test-id="CT_Component_ShippingSelector_ButtonShipping"]//p[text()="Select shipping service"]')
        #self.select_JNE_REG = (By.CSS_SELECTOR, "p._15kd2we74._17zx15ta8._17zx15tdc#base")
        self.select_JNE_REG = (By.CSS_SELECTOR, "[alt='JNE REG']")
        #self.select_payment_method_button = (By.CSS_SELECTOR, "p._15r4f4dmn._17zx15tdc._1ccbe2wb#base")
        self.select_payment_method_button = (By.XPATH, '//div[@data-test-id="CT_Component_SelectorPayment_ButtonPayment"]//p[text()="Select Payment"]')
        #self.virtual_account_button = (By.CSS_SELECTOR, "p._15kd2weog._17zx15te8._1ccbe2wb#base")
        self.virtual_account_button = (By.CSS_SELECTOR, "[data-test-id='CT_Component_PaymentGroup_ButtonPaymentGroup']")
        self.virtual_account_BCA_button = (By.CSS_SELECTOR, "[data-test-id='CT_Component_SelectorPayment_ButtonSelectBank_VABCA']")
        self.bank_transfer_button = (By.XPATH, '//button[@data-test-id="CT_Component_PaymentGroup_ButtonPaymentGroup"]//p[text()="Bank Transfer"]')
        self.bank_transfer_BCA_button = (By.CSS_SELECTOR, '[data-test-id="CT_Component_SelectorPayment_ButtonSelectBank_BANKTRANSFER"]')
        self.confirm_shipment_button = (By.CSS_SELECTOR, "div[class='_1jc0z8o1'] button[class='_920fuu5 _920fuuf _920fuub _920fuu6']")
        self.confirm_payment_method = (By.CSS_SELECTOR, "[data-test-id='CT_Component_PaymentListFooter_ButtonConfirm']")
        self.place_order_button = (By.CSS_SELECTOR, "[data-test-id='CT_Component_btnPlaceOrder']")
        self.check_order_status_button = (By.CSS_SELECTOR, "[data-test-id='CT_page_payment-proof-button']")
        self.checkbox_button = (By.CSS_SELECTOR, "[data-test-id='CT_Component_CartItemCheckbox']")
        self.cancel_order_button = (By.CSS_SELECTOR, "[data-test-id='CT_Component_cancelOrder']")
        self.change_my_mind_radio_button = (By.CSS_SELECTOR, "[data-test-id='CT_CancelOrderReason_itemRadio0']")
        self.cancel_confirm_button = (By.CSS_SELECTOR, "[data-test-id='CT_Button_confirmReason']")
        
    #Element Assert
        self.alert_cant_proceed_text = (By.CSS_SELECTOR, "[data-test-id='toast-']")
        self.alert_select_product_to_checkout_text = (By.CSS_SELECTOR, "p._15kd2wee8._17zx15tdc._1ccbe2wb#base")
        self.alert_order_success_text = (By.CSS_SELECTOR, "p._15kd2we7k._15r4f4dgo._17zx15t8w._17zx15te8._17zx15t28#base")
        self.canceled_order_text = (By.CSS_SELECTOR, "p._17zx15te8._1ccbe2wc#base")

    #Method Step
    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.checkout_button)).click()

    def click_select_shipping_method(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.select_shipping_method)).click()

    def click_select_JNE_REG(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.select_JNE_REG)).click()

    def click_confirm_shipment_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.confirm_shipment_button)).click()



    def click_select_payment_method(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.select_payment_method_button)).click()

    def click_virtual_account(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.virtual_account_button)).click()

    def click_virtual_account_BCA(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.virtual_account_BCA_button)).click()

    def click_bank_transfer(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.bank_transfer_button)).click()

    def click_bank_transfer_BCA(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.bank_transfer_BCA_button)).click()

    def click_confirm_payment_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.confirm_payment_method)).click()

    def click_place_order_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.place_order_button)).click()

    def get_alert_cant_proceed_text(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.alert_cant_proceed_text)).text

    def get_alert_order_success(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.alert_order_success_text)).text

    def click_check_order_status(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.check_order_status_button)).click()

    def get_alert_select_product_to_checkout(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.alert_select_product_to_checkout_text)).text

    def click_checkbox(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.checkbox_button)).click()
    
    def click_cancel_order(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cancel_order_button)).click()

    def click_change_my_mind_cancel(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.change_my_mind_radio_button)).click()

    def click_confirm_cancel_order(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.cancel_confirm_button)).click()

    def get_alert_canceled_order(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.canceled_order_text)).text

    def scroll_to_position(self, y_position): self.driver.execute_script(f"window.scrollTo(0, {y_position});")


    #Combined Step

    def select_shipping_service(self):
        self.click_select_shipping_method()
        time.sleep(2)
        self.click_select_JNE_REG()
        self.click_confirm_shipment_button() 


    def select_payment_method_with_virtual_account(self):
        time.sleep(3)
        self.scroll_to_position(342)
        time.sleep(3)
        self.click_select_payment_method()
        self.click_virtual_account()
        time.sleep(2)
        self.click_virtual_account_BCA()
        self.click_confirm_payment_button()


    def select_payment_method_with_bank_transfer(self):
        time.sleep(3)
        self.scroll_to_position(342)
        time.sleep(3)
        self.click_select_payment_method()
        self.click_bank_transfer()
        time.sleep(2)
        self.click_bank_transfer_BCA()
        self.click_confirm_payment_button()


    def cancel_order(self):
        self.scroll_to_position(586)
        self.click_cancel_order()
        self.click_change_my_mind_cancel()
        self.click_confirm_cancel_order()