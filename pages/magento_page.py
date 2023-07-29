from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator
from .base_page import BasePage

class MagentoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    url = 'https://magento.softwaretestingboard.com/'

    # Locator 1
    @property
    def create_account_button1(self):
        locator = Locator(By.LINK_TEXT, 'Create an Account')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 1: Create Account Button')

    # Locator 2
    @property
    def first_name_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="firstname"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 2: First Name Input')

    # Locator 3
    @property
    def last_name_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="lastname"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 3: Last Name Input')

    # Locator 4
    @property
    def create_account_email_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="email_address"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 4: Create Account Email Input')

    # Locator 5
    @property
    def create_account_password_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="password"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 5: Create Account Password Input')

    # Locator 6
    @property
    def confirm_password_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="password-confirmation"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 6: Confirm Password Input')

    # Locator 7
    @property
    def create_account_button2(self):
        locator = Locator(By.CSS_SELECTOR, 'button[title="Create an Account"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 7: Create Account Button 2')

    # Locator 8
    @property
    def contact_info_text(self):
        locator = Locator(By.CSS_SELECTOR, 'div[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 8: Contact Info Text')

    # Locator 9
    @property
    def account_link(self):
        locator = Locator(By.CSS_SELECTOR, 'button.action.switch[data-action="customer-menu-toggle"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 9: Account Link')

    # Locator 10
    @property
    def log_out_link(self):
        locator = Locator(By.CSS_SELECTOR, 'a[href="https://magento.softwaretestingboard.com/customer/account/logout/"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 10: Log Out Link')

    # Locator 11
    @property
    def sign_out_title(self):
        locator = Locator(By.CSS_SELECTOR, 'span.base[data-ui-id="page-title-wrapper"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 11: Sign Out Title')

    # Locator 12
    @property
    def sign_in_link(self):
        locator = Locator(By.XPATH, '//a[contains(text(), "Sign In")]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 12: Sign In Link')

    # Locator 13
    @property
    def sign_in_email_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="email"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 13: Sign In Email Input')

    # Locator 14
    @property
    def sign_in_password_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="pass"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 14: Sign In Password Input')

    # Locator 15
    @property
    def sign_in_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="send2"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 15: Sign In Button')

    # Locator 16
    @property
    def welcome_link(self):
        locator = Locator(By.XPATH, '(//span[@class="logged-in"])[1]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 16: Welcome Link')

    # Locator 17
    @property
    def contact_info(self):
        locator = Locator(By.XPATH, '(//div[@class="box-content"])[1]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 17: Contact Info')

    # Locator 18
    @property
    def search_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="search"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 18: Search input')

    # Locator 19
    @property
    def first_item_link(self):
        locator = Locator(By.XPATH, '//a[@class="product-item-link"][1]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 19: first item_link')

    # Locator 20
    @property
    def size_m_button(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="option-label-size-143-item-168"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 20: size_m_button')

    # Locator 21
    @property
    def color_1_button(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="option-label-color-93-item-50"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 21: color_1_button')

    # Locator 22
    @property
    def qty_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="qty"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 22: qty_input')

    # Locator 23
    @property
    def add_to_card_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="product-addtocart-button"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 23: add_to_card_button')

    # Locator 24
    @property
    def shopping_card_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[class="action showcart"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 24: shopping_card_button')

    # Locator 25
    @property
    def shopping_card_msg(self):
        locator = Locator(By.CSS_SELECTOR, 'div[data-bind^="html: $parent.prepareMessageForHtml"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 25: shopping_card_msg')

    # Locator 26
    @property
    def checkout_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="top-cart-btn-checkout"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 26: checkout_button')

    # Locator 27
    @property
    def summary_item_name(self):
        locator = Locator(By.CSS_SELECTOR, 'strong.product-item-name')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 27: summary_item_name')

    # locator 28
    @property
    def summary_item_qty(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="value"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 28: summary_item_qty')

    # locator 29
    @property
    def view_details_expand(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="title"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 29: view_details_expand')

    # locator 30
    @property
    def shipping_email_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[data-bind*="email"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 30: shipping_email_input')

    # locator 31
    @property
    def shipping_firstname_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="firstname"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 31: shipping_firstname_input')

    # locator 32
    @property
    def shipping_lastname_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="lastname"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 32: shipping_lastname_input')

    # locator 33
    @property
    def shipping_company_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="company"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 33: shipping_company_input')

    # locator 34
    @property
    def shipping_street_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="street[0]"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 34: shipping_street_input')

    # locator 35
    @property
    def shipping_city_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="city"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 35: shipping_city_input')

    # locator 36
    @property
    def shipping_zip_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="postcode"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 36: shipping_zip_input')

    # locator 37
    @property
    def shipping_country_dropdown(self):
        locator = Locator(By.CSS_SELECTOR, 'select[name="country_id"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 37: shipping_country_dropdown')

    # locator 38
    @property
    def shipping_phone_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="telephone"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 38: shipping_phone_input')

    # locator 39
    @property
    def shipping_next_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[class="button action continue primary"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 39: shipping_next_button')

    # locator 40
    @property
    def flat_rate_radiobutton(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="ko_unique_2"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 40: shipping_next_button')

    # locator 40
    @property
    def place_order_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[title="Place Order"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 40: shipping_next_button')

    # locator 41
    @property
    def billing_details_text(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="billing-address-details"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 41: billing_details_text')

    # locator 42
    @property
    def order_number_text(self):
        locator = Locator(By.XPATH, '//div[@class="checkout-success"]/p[1]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 42: order_number_text')

    # locator 43
    @property
    def expand_menu_woman(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="ui-id-4"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 43: expand_menu_woman')

    # locator 44
    @property
    def expand_tops_woman(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="ui-id-9"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 43: expand_tops_woman')

    # locator 46
    @property
    def expand_jackets_woman(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="ui-id-11"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 46: expand_jackets_woman')

    # locator 47
    @property
    def names_jackets_woman(self):
        locator = Locator(By.CSS_SELECTOR, 'a[class="product-item-link"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 47: names_jackets_woman')

    # locator 48
    @property
    def price_jackets_woman(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="price"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 48: price_jackets_woman')


    # locator 49
    @property
    def sort_by_expand(self):
        locator = Locator(By.XPATH, '(//select[@id="sorter"])[1]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 49: sort_by_expand')

    # locator 50
    @property
    def sort_by_price(self):
        locator = Locator(By.CSS_SELECTOR, 'option[value="price"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 50: sort_by_price')

    # locator 51
    @property
    def sort_by_name(self):
        locator = Locator(By.CSS_SELECTOR, 'option[value="name"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 51: sort_by_name')

    # locator 52
    @property
    def shopping_price_expand(self):
        locator = Locator(By.XPATH, '//div[text()="Price"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 52: shopping_price_expand')

    # locator 53
    @property
    def shopping_price_1(self):
        locator = Locator(By.XPATH, '//div[@class="filter-options-content"]/ol[@class="items"]/li[@class="item"][1]/a/span[@class="price"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 53: shopping_price_1')

    # locator 54
    @property
    def shopping_price_2(self):
        locator = Locator(By.XPATH, '//div[@class="filter-options-content"]/ol[@class="items"]/li[@class="item"][2]/a/span[@class="price"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 54: shopping_price_2')

    # locator 55
    @property
    def first_name_register_error(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="firstname-error"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 55: first_name_error')

    # locator 56
    @property
    def last_name_register_error(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="lastname-error"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 56: last_name_error')

    # locator 57
    @property
    def emai_register_error(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="email_address-error"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 57: email_error')

    # locator 58
    @property
    def password_register_error(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="password-error"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 58: password_error')

    # locator 59
    @property
    def confirm_password_error(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="password-confirmation-error"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 59: confirm_password_error')

    # locator 60
    @property
    def logo(self):
        locator = Locator(By.CSS_SELECTOR, 'a[class="logo"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 60: logo')

    # locator 61
    @property
    def welcome_button(self):
        locator = Locator(By.XPATH, '//button[@class="action switch"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 61: welcome_button')

    # locator 62
    @property
    def email_signin_error(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="email-error"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 62: email_signin_error')

    # locator 63
    @property
    def password_signin_error(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="pass-error"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 63: password_signin_error')

    # locator 64
    @property
    def signin_error(self):
        locator = Locator(By.CSS_SELECTOR, 'div[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 64: incorrect_signin_error')

    # locator 65
    @property
    def my_account_link(self):
        locator = Locator(By.CSS_SELECTOR, 'a[href="https://magento.softwaretestingboard.com/customer/account/"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 65: my_account_link')

    # locator 66
    @property
    def change_password_link(self):
        locator = Locator(By.CSS_SELECTOR, 'a[href="https://magento.softwaretestingboard.com/customer/account/edit/changepass/1/"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 66: change_password_link')

    # locator 67
    @property
    def current_password_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="current-password"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 67: current_password_input')

    # locator 68
    @property
    def new_password_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="password"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 68: new_password_input')

    # locator 69
    @property
    def confirm_new_password_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="password-confirmation"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 69: confirm_new_password_input')

    # locator 70
    @property
    def save_password_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[title="Save"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 70: save_password_button')

    # locator 71
    @property
    def account_information_msg(self):
        locator = Locator(By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
        return BaseElement(driver=self.driver, locator=locator, name='Locator 71: account_information_msg')

