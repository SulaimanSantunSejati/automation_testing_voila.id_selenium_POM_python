import time
from webdriver_setup import setup_webdriver
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.filter_page import FilterPage


class TestFilter():
    def setup_method(self):
        self.driver = setup_webdriver()
        self.login_page = LoginPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.filter_page = FilterPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

#Boutique Availability
    def test_filter_search_result_based_on_item_available_on_Jakarta_Mall_of_Indonesia_Boutique(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_MOI()    
        assert self.filter_page.get_boutique_availability_text() == 'Jakarta - Mall of Indonesia'

    def test_filter_search_result_based_on_item_available_on_Jakarta_Pondok_Indah_Boutique(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_PI()    
        assert self.filter_page.get_boutique_availability_text() == 'Jakarta - Pondok Indah'

    def test_filter_search_result_based_on_item_available_on_Jakarta_Pantai_Indah_Kapuk_Boutique(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_PIK()    
        assert self.filter_page.get_boutique_availability_text() == 'Jakarta - Pantai Indah Kapuk'

    def test_filter_search_result_based_on_item_available_on_Surabaya_Bukit_Darmo_Golf_Boutique(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_BDG()    
        assert self.filter_page.get_boutique_availability_text() == 'Surabaya - Bukit Darmo Golf'

    def test_filter_search_result_based_on_item_available_on_Medan_Sun_Plaza_Boutique(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_MSP()    
        assert self.filter_page.get_boutique_availability_text() == 'Medan - Sun Plaza'

#Gender 
    def test_filter_search_result_based_on_item_available_for_women(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_Women()    
        assert self.filter_page.get_gender_availability_text() == 'Women'

    def test_filter_search_result_based_on_item_available_for_men(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        time.sleep(3)  
        self.filter_page.click_Men()    
        assert self.filter_page.get_gender_availability_text() == 'Men'

    def test_filter_search_result_based_on_item_available_for_kids(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        time.sleep(3)  
        self.filter_page.click_Kids()    
        assert self.filter_page.get_gender_availability_text() == 'Kids'

#Stock Availability
    def test_filter_search_result_based_on_item_available_Ready_Stock(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_Ready_Stock() 
        time.sleep(3)     
        assert self.filter_page.get_stock_availability_text() == 'Ready Stock'   

    def test_filter_search_result_based_on_item_available_Preorder(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        time.sleep(7)  
        self.filter_page.click_Preorder()
        time.sleep(3)      
        assert self.filter_page.get_stock_availability_text() == 'Preorder'

# #Category
    def test_filter_search_result_based_on_shoes(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        time.sleep(3)
        self.filter_page.click_Shoes() 
        time.sleep(3)     
        assert self.filter_page.get_category_availability_text() == 'Shoes'         

    def test_filter_search_result_based_on_clothes(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_Clothes() 
        time.sleep(3)     
        assert self.filter_page.get_category_availability_text() == 'Clothes' 

    def test_filter_search_result_based_on_Category_bags(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_Bags() 
        time.sleep(3)     
        assert self.filter_page.get_category_availability_text() == 'Bags'  

    def test_filter_search_result_based_on_Category_accessories(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_Accessories() 
        time.sleep(3)     
        assert self.filter_page.get_category_availability_text() == 'Accessories' 
 
    def test_filter_search_result_based_on_Category_watches(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        time.sleep(3)
        self.filter_page.click_Watches() 
        time.sleep(3)     
        assert self.filter_page.get_category_availability_text() == 'Watches'                 

    def test_filter_search_result_based_on_Category_Beauty(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_Beauty() 
        time.sleep(3)     
        assert self.filter_page.get_category_availability_text() == 'Beauty' 
        
    #Product Type    
    def test_filter_search_result_based_on_card_holders(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_card_holders()
        time.sleep(3)     
        assert self.filter_page.get_product_type_availability_text() == 'Card holders'   

    def test_filter_search_result_based_on_belts(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        time.sleep(3)
        self.filter_page.click_belts()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Belts'

    def test_filter_search_result_based_on_earrings(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_earrings()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Earrings'

    def test_filter_search_result_based_on_watches(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        time.sleep(3)
        self.filter_page.click_watches()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Watches'

    def test_filter_search_result_based_on_heeled_sandals(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_heeled_sandals()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Heeled Sandals'

    def test_filter_search_result_based_on_shorts(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_shorts()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Shorts'

    def test_filter_search_result_based_on_bag_charms(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_bag_charms()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Bag Charms'

    def test_filter_search_result_based_on_blankets(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_blankets()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Blankets'

    def test_filter_search_result_based_on_vests(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_vests()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Vests'

    def test_filter_search_result_based_on_rings(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_rings()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Rings'

    def test_filter_search_result_based_on_slip_ons(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_slip_ons()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Slip-Ons'

    def test_filter_search_result_based_on_caps(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_caps()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Caps'

    def test_filter_search_result_based_on_necklaces(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_necklaces()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Necklaces'

    def test_filter_search_result_based_on_other_essentials(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_other_essentials()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Other Essentials'

    def test_filter_search_result_based_on_long_sleeved_shirts(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_long_sleeved_shirts()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Long Sleeved Shirts'

    def test_filter_search_result_based_on_other_tops(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_other_tops()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Other Tops'

    def test_filter_search_result_based_on_pouches(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_pouches()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Pouches'

    def test_filter_search_result_based_on_scarves(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_scarves()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Scarves'

    def test_filter_search_result_based_on_wallets(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_wallets()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Wallets'

    def test_filter_search_result_based_on_strap(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_strap()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Strap'

    def test_filter_search_result_based_on_bracelets(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_bracelets()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Bracelets'

    def test_filter_search_result_based_on_lips(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_lips()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Lips'

    def test_filter_search_result_based_on_nails(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_nails()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Nails'

    def test_filter_search_result_based_on_bucket_bags(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_bucket_bags()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Bucket Bags'

    def test_filter_search_result_based_on_luggage(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_luggage()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Luggage'

    def test_filter_search_result_based_on_twilly(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_twilly()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Twilly'

    def test_filter_search_result_based_on_ties(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_ties()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Ties'

    def test_filter_search_result_based_on_bag_straps(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_bag_straps()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Bag Straps'

    def test_filter_search_result_based_on_shoulder_bags(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_shoulder_bags()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Shoulder Bags'

    def test_filter_search_result_based_on_face(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_face()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Face'

    def test_filter_search_result_based_on_fragrance(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_fragrance()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Fragrance'

    def test_filter_search_result_based_on_woc(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_woc()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'WOC'

    def test_filter_search_result_based_on_backpacks(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_backpacks()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Backpacks'

    def test_filter_search_result_based_on_belt_bags(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_belt_bags()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Belt Bags'

    def test_filter_search_result_based_on_clutch_bags(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_clutch_bags()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Clutch Bags'

    def test_filter_search_result_based_on_handbags(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_handbags()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Handbags'

    def test_filter_search_result_based_on_crossbody_bags(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_crossbody_bags()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Crossbody Bags'

    def test_filter_search_result_based_on_dresses(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_dresses()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Dresses'

    def test_filter_search_result_based_on_hoodie(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_hoodie()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Hoodie'

    def test_filter_search_result_based_on_t_shirts(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_t_shirts()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'T-Shirts'

    def test_filter_search_result_based_on_sweatshirts(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_sweatshirts()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Sweatshirts'

    def test_filter_search_result_based_on_jackets(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_jackets()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Jackets'

    def test_filter_search_result_based_on_cardigan(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_cardigan()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Cardigan'

    def test_filter_search_result_based_on_winterwear(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_winterwear()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Winterwear'

    def test_filter_search_result_based_on_boots(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_boots()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Boots'

    def test_filter_search_result_based_on_loafers(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_loafers()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Loafers'

    def test_filter_search_result_based_on_passport_holders(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_passport_holders()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Passport Holders'

    def test_filter_search_result_based_on_key_chains(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_key_chains()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Key Chains'

    def test_filter_search_result_based_on_towels(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_towels()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Towels'

    def test_filter_search_result_based_on_wedges(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_wedges()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Wedges'

    def test_filter_search_result_based_on_blouses(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_blouses()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Blouses'

    def test_filter_search_result_based_on_bucket_hats(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_bucket_hats()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Bucket Hats'

    def test_filter_search_result_based_on_beanies(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_beanies()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Beanies'

    def test_filter_search_result_based_on_berets(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_berets()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Berets'

    def test_filter_search_result_based_on_brooches(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_brooches()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Brooches'
        
    def test_filter_search_result_based_on_other_heels(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_Other_Heels()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Other Heels'

    def test_filter_search_result_based_on_sling_bags(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_sling_bags()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Sling Bags'

    def test_filter_search_result_based_on_polo_shirts(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_Polo_Shirts()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Polo Shirts'

    def test_filter_search_result_based_on_mules(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_Mules()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Mules'

    def test_filter_search_result_based_on_sandals(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_sandals()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Sandals'

    def test_filter_search_result_based_on_slingbacks(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_Slingbacks()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Slingbacks'

    def test_filter_search_result_based_on_sneakers(self):
        self.login_page.unlogin()
        self.search_page.search("hermes")
        self.filter_page.click_Sneakers()
        time.sleep(3)
        assert self.filter_page.get_product_type_availability_text() == 'Sneakers'
