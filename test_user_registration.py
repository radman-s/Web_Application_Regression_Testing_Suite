from pages.drivers import Drivers
from pages.magento_page import MagentoPage
import json
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from faker import Faker

class TestRegistrationScenario:
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

    def register_new_account(self):
        # Perform registration by filling in the required details
        self.mp.create_account_button1.click()
        self.mp.first_name_input.input_text(self.test_data['first_name'])
        self.mp.last_name_input.input_text(self.test_data['last_name'])
        self.mp.create_account_email_input.input_text(self.email)
        self.mp.create_account_password_input.input_text(self.test_data['password'])
        self.mp.confirm_password_input.input_text(self.test_data['password'])
        self.mp.create_account_button2.click()

    def verify_confirmation_message(self):
        # Verify the presence of the confirmation message
        assert self.mp.contact_info_text.text(), 'Confirmation message not displayed'

    def verify_customer_account_url(self):
        # Verify the customer account URL
        actual_url = self.browser.current_url
        expected_url = self.test_data['customer_url']
        assert actual_url == expected_url, f"Expected customer account URL '{expected_url}', but actual URL is '{actual_url}'"

    def log_out(self):
        # Log out from the customer account
        self.mp.account_link.click()
        self.mp.log_out_link.click()

    def verify_sign_out_message(self):
        # Verify the sign-out message
        actual_message = self.mp.sign_out_title.text()
        expected_message = self.test_data['sign_out_msg']
        assert actual_message == expected_message, f"Expected sign-out message '{expected_message}', but actual message is '{actual_message}'"

    def sign_in(self):
        # Perform sign-in using the registered credentials
        self.mp.sign_in_link.click()
        self.mp.sign_in_email_input.input_text(self.email)
        self.mp.sign_in_password_input.input_text(self.test_data['password'])
        self.mp.sign_in_button.click()

    def verify_email_in_contact_info(self):
        # Verify the email in the contact information
        expected_email = self.email
        assert expected_email in self.mp.contact_info.text(), f"Email '{expected_email}' does not match the expected email in contact info"

    def run_test(self):
        try:
            self.setup()

            self.mp.go()
            self.verify_homepage_title()

            self.register_new_account()
            self.verify_confirmation_message()
            self.verify_customer_account_url()

            self.log_out()
            self.verify_sign_out_message()

            self.sign_in()
            self.verify_email_in_contact_info()

            print('Registration Test passed')
        except (NoSuchElementException, TimeoutException) as e:
            print(f'Exception occurred: {str(e)}')
        finally:
            self.teardown()

