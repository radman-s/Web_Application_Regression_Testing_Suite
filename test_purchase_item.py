from pages.drivers import Drivers
from pages.magento_page import MagentoPage
import json
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import re
from faker import Faker

class TestPurchaseScenario:
    def __init__(self):
        self.browser = None
        self.mp = None
        self.test_data = None
        self.email = None

    def load_test_data(self):
        # Load test data from JSON file
        with open('pages/test_data_magento.json') as file:
            self.test_data = json.load(file)

    def generate_fake_email(self):
        # Generate a fake email using Faker library
        faker = Faker()
        self.email = faker.email()

    def setup(self):
        # Load test data and set up the browser driver
        self.load_test_data()
        self.generate_fake_email()

        self.browser = Drivers('--ignore-certificate-errors').chrome()
        self.mp = MagentoPage(driver=self.browser)

    def teardown(self):
        # Quit the browser driver after the test completes
        self.browser.quit()

    def verify_homepage_title(self):
        # Verify the homepage title
        actual_title = self.browser.title
        expected_title = self.test_data['homepage_title']
        assert actual_title == expected_title, f"Homepage title '{actual_title}' does not match expected title '{expected_title}'"

    def verify_product_details(self):
        # Verify the product details
        self.mp.search_input.input_text(self.test_data['search_product'])
        self.mp.search_input.enter()
        self.first_item = self.mp.first_item_link.text()
        self.mp.first_item_link.click()
        assert self.browser.title == self.first_item, 'Item page title does not correspond to the selected product'
        self.mp.size_m_button.click()
        self.mp.color_1_button.click()
        self.mp.qty_input.clear()
        self.mp.qty_input.input_text(self.test_data['qty_item'])
        self.mp.add_to_card_button.click()
        assert self.mp.shopping_card_msg.text() == f'You added {self.first_item} to your shopping cart.', 'The shopping cart message is incorrect'

    def verify_shopping_cart(self):
        # Verify the shopping cart
        self.mp.shopping_card_button.click()
        # input(' ')
        print(self.mp.summary_item_name.text() )
        print(self.first_item)
        assert self.mp.summary_item_name.is_displayed(),'The item name in summary is not displayed'
        assert self.mp.summary_item_name.text() == self.first_item, 'Item name in summary does not match the selected product'
        self.mp.checkout_button.click()

    def verify_shipping_page(self):
        # Verify the shipping page
        self.mp.shipping_phone_input.input_text(self.test_data['phone'])
        self.mp.shipping_firstname_input.input_text(self.test_data['first_name'])
        self.mp.shipping_lastname_input.input_text(self.test_data['last_name'])
        self.mp.shipping_company_input.input_text(self.test_data['company'])

        self.mp.shipping_street_input.input_text(self.test_data['street'])
        self.mp.shipping_city_input.input_text(self.test_data['city'])
        self.mp.shipping_zip_input.input_text(self.test_data['zip'])

        self.mp.shipping_country_dropdown.input_text(self.test_data['country'])
        self.mp.flat_rate_radiobutton.click()
        self.mp.shipping_email_input.input_text(self.email)
        self.mp.shipping_next_button.click()
        assert self.browser.current_url == self.test_data['shipping_url'], 'Checkout URL does not match'

    def verify_payment_page(self):
        # Verify the payment page
        assert self.mp.place_order_button.is_displayed(), 'Place Order button is not displayed'
        assert self.browser.current_url == self.test_data['payment_url'], 'Payment URL does not match'
        assert self.test_data['first_name'] in self.mp.billing_details_text.text() and self.test_data['last_name'] in self.mp.billing_details_text.text(), 'Billing details do not match'

        self.mp.place_order_button.click()
        order_number_text = self.mp.order_number_text.text()
        assert re.search(self.test_data['order_number_pattern'], order_number_text), "Order number not found"

    def run_test(self):
        try:
            self.setup()

            self.mp.go()
            self.verify_homepage_title()

            self.verify_product_details()
            self.verify_shopping_cart()

            self.verify_shipping_page()
            self.verify_payment_page()

            print('Purchase Test passed')
        except (NoSuchElementException, TimeoutException) as e:
            print(f'Exception occurred: {str(e)}')
        finally:
            self.teardown()


