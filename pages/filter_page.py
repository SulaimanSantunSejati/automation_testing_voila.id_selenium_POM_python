from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FilterPage:
    def __init__(self,driver):
        self.driver = driver
        #Boutiques
        self.mall_of_indonesia =(By.XPATH, "//p[contains(text(), 'Jakarta - Mall of Indonesia')]")
        self.pondok_indah =(By.XPATH, "//p[contains(text(), 'Jakarta - Pondok Indah')]")
        self.pantai_indah_kapuk =(By.XPATH, "//p[contains(text(), 'Jakarta - Pantai Indah Kapuk')]")
        self.bukit_darmo_golf =(By.XPATH, "//p[contains(text(), 'Surabaya - Bukit Darmo Golf')]")
        self.medan_sun_plaza =(By.XPATH, "//p[contains(text(), 'Medan - Sun Plaza')]")

        #Availability
        self.boutique_availability = (By.CSS_SELECTOR, "[data-test-id='CT-quick-filter-pill-storeAvailability']")
        self.gender_availability = (By.CSS_SELECTOR, "[data-test-id='CT-quick-filter-pill-gender']")
        self.stock_availability = (By.CSS_SELECTOR, "[data-test-id='CT-quick-filter-pill-stockAvailability']")
        self.category_availability = (By.CSS_SELECTOR, "[data-test-id='CT-quick-filter-pill-category']")
        self.product_type_availability = (By.CSS_SELECTOR, "[data-test-id='CT-quick-filter-pill-productType']")

        #Gender
        self.women = (By.XPATH, "//p[contains(text(), 'Women')]")
        self.men = (By.XPATH, "//p[contains(text(), 'Men')]")
        self.kids = (By.XPATH, "//p[contains(text(), 'Kids')]")

        #Stock Availability
        self.ready_stock = (By.XPATH, "//p[contains(text(), 'Ready Stock')]")
        self.preorder = (By.XPATH, "//p[contains(text(), 'Preorder')]")

        #Category
        self.shoes = (By.XPATH, "//p[contains(text(), 'Shoes')]")
        self.clothes = (By.XPATH, "//p[contains(text(), 'Clothes')]")
        self.bags = (By.XPATH, "//p[contains(text(), 'Bags')]")
        self.accessories = (By.XPATH, "//p[contains(text(), 'Accessories')]")
        self.beauty = (By.XPATH, "//p[contains(text(), 'Beauty')]")
        self.watches = (By.XPATH, "//p[contains(text(), 'Watches')]")

        #Product type
        self.card_holders         = (By.XPATH, "//p[contains(text(), 'Card holders')]")
        self.belts                = (By.XPATH, "//p[contains(text(), 'Belts')]")
        self.earrings             = (By.XPATH, "//p[contains(text(), 'Earrings')]")
        self.watches              = (By.XPATH, "//p[contains(text(), 'Watches')]")
        self.heeled_sandals       = (By.XPATH, "//p[contains(text(), 'Heeled Sandals')]")
        self.shorts               = (By.XPATH, "//p[contains(text(), 'Shorts')]")
        self.bag_charms           = (By.XPATH, "//p[contains(text(), 'Bag Charms')]")
        self.blankets             = (By.XPATH, "//p[contains(text(), 'Blankets')]")
        self.vests                = (By.XPATH, "//p[contains(text(), 'Vests')]")
        self.rings                = (By.XPATH, "//p[contains(text(), 'Rings')]")
        self.slip_ons             = (By.XPATH, "//p[contains(text(), 'Slip-Ons')]")
        self.caps                 = (By.XPATH, "//p[contains(text(), 'Caps')]")
        self.necklaces            = (By.XPATH, "//p[contains(text(), 'Necklaces')]")
        self.other_essentials     = (By.XPATH, "//p[contains(text(), 'Other Essentials')]")
        self.long_sleeved_shirts  = (By.XPATH, "//p[contains(text(), 'Long Sleeved Shirts')]")
        self.other_tops           = (By.XPATH, "//p[contains(text(), 'Other Tops')]")
        self.pouches              = (By.XPATH, "//p[contains(text(), 'Pouches')]")
        self.scarves              = (By.XPATH, "//p[contains(text(), 'Scarves')]")
        self.wallets              = (By.XPATH, "//p[contains(text(), 'Wallets')]")
        self.strap                = (By.XPATH, "//p[contains(text(), 'Strap')]")
        self.bracelets            = (By.XPATH, "//p[contains(text(), 'Bracelets')]")
        self.lips                 = (By.XPATH, "//p[contains(text(), 'Lips')]")
        self.nails                = (By.XPATH, "//p[contains(text(), 'Nails')]")
        self.bucket_bags          = (By.XPATH, "//p[contains(text(), 'Bucket Bags')]")
        self.luggage              = (By.XPATH, "//p[contains(text(), 'Luggage')]")
        self.twilly               = (By.XPATH, "//p[contains(text(), 'Twilly')]")
        self.ties                 = (By.XPATH, "//p[contains(text(), 'Ties')]")
        self.bag_straps           = (By.XPATH, "//p[contains(text(), 'Bag Straps')]")
        self.shoulder_bags        = (By.XPATH, "//p[contains(text(), 'Shoulder Bags')]")
        self.face                 = (By.XPATH, "//p[contains(text(), 'Face')]")
        self.fragrance            = (By.XPATH, "//p[contains(text(), 'Fragrance')]")
        self.woc                  = (By.XPATH, "//p[contains(text(), 'WOC')]")
        self.backpacks            = (By.XPATH, "//p[contains(text(), 'Backpacks')]")
        self.belt_bags            = (By.XPATH, "//p[contains(text(), 'Belt Bags')]")
        self.clutch_bags          = (By.XPATH, "//p[contains(text(), 'Clutch Bags')]")
        self.handbags             = (By.XPATH, "//p[contains(text(), 'Handbags')]")
        self.crossbody_bags       = (By.XPATH, "//p[contains(text(), 'Crossbody Bags')]")
        self.dresses              = (By.XPATH, "//p[contains(text(), 'Dresses')]")
        self.hoodie               = (By.XPATH, "//p[contains(text(), 'Hoodie')]")
        self.sandals              = (By.XPATH, "//p[contains(text(), 'Sandals')]")
        self.t_shirts             = (By.XPATH, "//p[contains(text(), 'T-Shirts')]")
        self.sweatshirts          = (By.XPATH, "//p[contains(text(), 'Sweatshirts')]")
        self.jackets              = (By.XPATH, "//p[contains(text(), 'Jackets')]")
        self.cardigan             = (By.XPATH, "//p[contains(text(), 'Cardigan')]")
        self.winterwear           = (By.XPATH, "//p[contains(text(), 'Winterwear')]")
        self.boots                = (By.XPATH, "//p[contains(text(), 'Boots')]")
        self.loafers              = (By.XPATH, "//p[contains(text(), 'Loafers')]")
        self.passport_holders     = (By.XPATH, "//p[contains(text(), 'Passport Holders')]")
        self.key_chains           = (By.XPATH, "//p[contains(text(), 'Key Chains')]")
        self.towels               = (By.XPATH, "//p[contains(text(), 'Towels')]")
        self.wedges               = (By.XPATH, "//p[contains(text(), 'Wedges')]")
        self.blouses              = (By.XPATH, "//p[contains(text(), 'Blouses')]")
        self.bucket_hats          = (By.XPATH, "//p[contains(text(), 'Bucket Hats')]")
        self.beanies              = (By.XPATH, "//p[contains(text(), 'Beanies')]")
        self.berets               = (By.XPATH, "//p[contains(text(), 'Berets')]")
        self.brooches             = (By.XPATH, "//p[contains(text(), 'Brooches')]")
        self.sling_bags           = (By.XPATH, "//p[contains(text(), 'Sling Bags')]")
        self.other_heels          = (By.XPATH, "//p[contains(text(), 'Other Heels')]")
        self.polo_shirts          = (By.XPATH, "//p[contains(text(), 'Polo Shirts')]")
        self.mules                = (By.XPATH, "//p[contains(text(), 'Mules')]")
        self.slingbacks           = (By.XPATH, "//p[contains(text(), 'Slingbacks')]")
        self.sneakers             = (By.XPATH, "//p[contains(text(), 'Sneakers')]")




#step method boutiques
    def click_MOI(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.mall_of_indonesia)).click()

    def click_PI(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.pondok_indah)).click()

    def click_BDG(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.bukit_darmo_golf)).click()

    def click_PIK(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.pantai_indah_kapuk)).click()

    def click_MSP(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.medan_sun_plaza)).click()

#step method gender 
    def click_Women(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.women)).click()

    def click_Men(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.men)).click()   

    def click_Kids(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.kids)).click()   

#Assert Values
    def get_boutique_availability_text(self):
        return WebDriverWait (self.driver, 20).until(EC.visibility_of_element_located(self.boutique_availability)).text

    def get_gender_availability_text(self):
        return WebDriverWait (self.driver, 20).until(EC.visibility_of_element_located(self.gender_availability)).text    

    def get_stock_availability_text(self):
        return WebDriverWait (self.driver, 20).until(EC.visibility_of_element_located(self.stock_availability)).text 

    def get_category_availability_text(self):
        return WebDriverWait (self.driver, 20).until(EC.visibility_of_element_located(self.category_availability)).text 

    def get_product_type_availability_text(self):
        return WebDriverWait (self.driver, 20).until(EC.visibility_of_element_located(self.product_type_availability)).text 

#method Stock Availability 
    def click_Ready_Stock(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.ready_stock)).click()  

    def click_Preorder(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.preorder)).click() 

#method Category
    def click_Shoes(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.shoes)).click()

    def click_Clothes(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.clothes)).click() 

    def click_Bags(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.bags)).click() 

    def click_Accessories(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.accessories)).click() 

    def click_Beauty(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.beauty)).click() 
        
# method product type
    def click_Other_Heels(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.other_heels)).click()        

    def click_Polo_Shirts(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.polo_shirts)).click()

    def click_Mules(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.mules)).click()

    def click_Slingbacks(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.slingbacks)).click()

    def click_Sneakers(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sneakers)).click()

    def click_card_holders(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.card_holders)).click()

    def click_belts(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.belts)).click()

    def click_earrings(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.earrings)).click()

    def click_watches(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.watches)).click()

    def click_heeled_sandals(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.heeled_sandals)).click()

    def click_shorts(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.shorts)).click()

    def click_sandals(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sandals)).click()

    def click_bag_charms(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.bag_charms)).click()

    def click_blankets(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.blankets)).click()

    def click_vests(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.vests)).click()

    def click_rings(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.rings)).click()

    def click_slip_ons(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.slip_ons)).click()

    def click_caps(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.caps)).click()

    def click_necklaces(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.necklaces)).click()

    def click_other_essentials(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.other_essentials)).click()

    def click_long_sleeved_shirts(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.long_sleeved_shirts)).click()

    def click_other_tops(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.other_tops)).click()

    def click_pouches(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.pouches)).click()

    def click_scarves(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.scarves)).click()

    def click_wallets(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.wallets)).click()

    def click_strap(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.strap)).click()

    def click_bracelets(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.bracelets)).click()

    def click_lips(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.lips)).click()

    def click_nails(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.nails)).click()

    def click_bucket_bags(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.bucket_bags)).click()

    def click_luggage(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.luggage)).click()

    def click_twilly(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.twilly)).click()

    def click_ties(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.ties)).click()

    def click_bag_straps(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.bag_straps)).click()

    def click_shoulder_bags(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.shoulder_bags)).click()

    def click_face(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.face)).click()

    def click_fragrance(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.fragrance)).click()

    def click_woc(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.woc)).click()

    def click_backpacks(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.backpacks)).click()

    def click_belt_bags(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.belt_bags)).click()

    def click_clutch_bags(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.clutch_bags)).click()

    def click_handbags(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.handbags)).click()

    def click_crossbody_bags(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.crossbody_bags)).click()

    def click_dresses(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.dresses)).click()

    def click_hoodie(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.hoodie)).click()

    def click_t_shirts(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.t_shirts)).click()

    def click_sling_bags(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sling_bags)).click()

    def click_sweatshirts(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sweatshirts)).click()

    def click_jackets(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.jackets)).click()

    def click_cardigan(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.cardigan)).click()

    def click_winterwear(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.winterwear)).click()

    def click_boots(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.boots)).click()

    def click_loafers(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.loafers)).click()

    def click_passport_holders(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.passport_holders)).click()

    def click_key_chains(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.key_chains)).click()

    def click_towels(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.towels)).click()

    def click_wedges(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.wedges)).click()

    def click_blouses(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.blouses)).click()

    def click_bucket_hats(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.bucket_hats)).click()

    def click_beanies(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.beanies)).click()

    def click_berets(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.berets)).click()

    def click_brooches(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.brooches)).click()
    