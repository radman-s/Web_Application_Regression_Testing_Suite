from pages.drivers import Drivers
from pages.magento_page import MagentoPage
import json
from faker import Faker

class RegistrationLoginErrorHandlingScenario:
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

    def test_registration_error_handling(self):
        try:
            self.setup()

            self.mp.go()

            # REGISTRATION ERROR HANDLING
            # assert all required fields error handling when left blank
            self.mp.create_account_button1.click()
            self.mp.create_account_button2.click()
            assert self.mp.first_name_register_error.text() == self.test_data['required_field_error'], "First name error is not as expected."
            assert self.mp.last_name_register_error.text() == self.test_data['required_field_error'], "Last name error is not as expected."
            assert self.mp.emai_register_error.text() == self.test_data['required_field_error'], "Email error is not as expected."
            assert self.mp.password_register_error.text() == self.test_data['required_field_error'], "Password error is not as expected."
            assert self.mp.confirm_password_error.text() == self.test_data['required_field_error'], "Confirm password error is not as expected."

            # enter correct name and last name
            self.mp.first_name_input.input_text(self.test_data['first_name'])
            self.mp.last_name_input.input_text(self.test_data['last_name'])
            # enter invalid email
            self.mp.create_account_email_input.input_text(self.test_data['invalid_email'])
            # enter invalid passwords
            self.mp.create_account_password_input.input_text(self.test_data['invalid_password'])
            self.mp.confirm_password_input.input_text(self.test_data['invalid_password'])
            self.mp.create_account_button2.click()
            # assert error handling for invalid email
            assert self.mp.emai_register_error.text() == self.test_data['invalid_email_error'], "Invalid email error is not as expected."
            # assert error handling for invalid password
            assert self.mp.password_register_error.text() == self.test_data['pass_min_error'], "Invalid password error is not as expected."

            # clear invalid credential and enter valid email and password
            self.mp.create_account_email_input.clear()
            self.mp.create_account_email_input.input_text(self.email)
            self.mp.create_account_password_input.input_text(self.test_data['password'])
            self.mp.confirm_password_input.input_text(self.test_data['invalid_password'])
            self.mp.create_account_button2.click()
            assert self.mp.confirm_password_error.text() == self.test_data['pass_same_error'], "Mismatching password error is not as expected."

            # create a valid account and logout
            self.browser.refresh()
            self.mp.first_name_input.input_text(self.test_data['first_name'])
            self.mp.last_name_input.input_text(self.test_data['last_name'])
            # store email for later login
            safe_email = self.email
            print(safe_email)

            self.mp.create_account_email_input.input_text(safe_email)
            self.mp.create_account_password_input.input_text(self.test_data['password'])
            self.mp.confirm_password_input.input_text(self.test_data['password'])
            self.mp.create_account_button2.click()
            # logout
            self.mp.logo.click()
            self.mp.welcome_button.click()
            self.mp.log_out_link.click()

            # LOGIN ERROR HANDLING
            # assert all required fields error handling when left blank (login)
            self.mp.sign_in_link.click()
            self.mp.sign_in_button.click()
            assert self.mp.email_signin_error.text() == self.test_data['required_field_error'], "Email error on login page is not as expected."
            assert self.mp.password_signin_error.text() == self.test_data['required_field_error'], "Password error on login page is not as expected."

            # assert error handling for invalid email format
            self.mp.sign_in_email_input.input_text(self.test_data['invalid_email'])
            self.mp.sign_in_password_input.input_text(self.test_data['password'])
            self.mp.sign_in_button.click()
            assert self.mp.email_signin_error.text() == self.test_data['invalid_email_error'], "Invalid email error on login page is not as expected."

            # assert error handling for invalid password (login)
            self.mp.sign_in_email_input.clear()
            self.mp.sign_in_email_input.input_text(self.email)
            self.mp.sign_in_password_input.input_text(self.test_data['invalid_password'])
            self.mp.sign_in_button.click()
            assert self.mp.signin_error.text() == self.test_data['invalid_signin_error'], "Invalid signin error is not as expected."

            print('registration and login error handling test passed')
        except Exception as e:
            print(f'Exception occurred: {str(e)}')
        finally:
            self.teardown()






