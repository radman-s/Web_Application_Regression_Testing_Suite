from pages.drivers import Drivers
from pages.magento_page import MagentoPage
import json
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class FilterSearchScenario:
    def __init__(self):
        self.browser = None
        self.mp = None
        self.test_data = None

    def load_test_data(self):
        # Load test data from JSON file
        with open('pages/test_data_magento.json') as file:
            self.test_data = json.load(file)

    def setup(self):
        # Load test data and set up the browser driver
        self.load_test_data()

        self.browser = Drivers('--ignore-certificate-errors').chrome()
        self.mp = MagentoPage(driver=self.browser)

    def teardown(self):
        # Quit the browser driver after the test completes
        self.browser.quit()

    def check_order(self, locator, max_elements=None, perform_check=True):
        # Check the order of elements in the locator
        elements = locator.driver.find_elements(*locator.locator)[:max_elements]
        values = [element.get_attribute('innerText') for element in elements]
        sorted_values = sorted(values)

        if perform_check:
            if values == sorted_values:
                print('The items are in order')
            else:
                print('The items are not in order')

        return values

    def price_range_filter(self, prices, price_range):
        # Filter prices based on the given price range
        for price in prices:
            numeric_price = float(price.replace('$', ''))
            min_price = float(price_range[0].replace('$', ''))
            max_price = float(price_range[1].replace('$', ''))

            assert min_price <= numeric_price <= max_price, f"Price {price} is not within the expected price range {price_range}"
            print(f'Price {price} is in expected range {price_range}')

        print('Filter test passed')

    def run_test(self):
        try:
            self.setup()

            self.mp.go()

            # Verify the homepage title
            assert self.browser.title == self.test_data['homepage_title'], 'Title does not match'

            # Navigate to the jackets section for women
            self.mp.expand_menu_woman.move_to()
            self.mp.expand_tops_woman.move_to()
            self.mp.expand_jackets_woman.click()
            assert self.browser.current_url == self.test_data['woman_jackets_url'], 'URL does not match'

            # Check product by alphabetical order
            self.mp.sort_by_expand.click()
            self.mp.sort_by_name.click()
            self.mp.names_jackets_woman.find(multiple=True)
            self.check_order(self.mp.names_jackets_woman, max_elements=12, perform_check=True)

            # Check products by numeric order from lowest to highest
            self.mp.sort_by_expand.click()
            self.mp.sort_by_price.click()
            self.mp.price_jackets_woman.find(multiple=True)
            self.check_order(self.mp.price_jackets_woman, max_elements=12, perform_check=True)

            # Check filter pricerange 1
            self.mp.shopping_price_expand.click()
            price_range = self.check_order(self.mp.shopping_price_1, max_elements=2, perform_check=False)
            self.mp.shopping_price_1.click()
            prices = self.check_order(self.mp.price_jackets_woman, max_elements=12, perform_check=False)
            self.price_range_filter(prices, price_range)

            self.browser.back()

            # Check filter pricerange 2
            self.mp.shopping_price_expand.click()
            price_range = self.check_order(self.mp.shopping_price_2, max_elements=2, perform_check=False)
            self.mp.shopping_price_2.click()
            prices = self.check_order(self.mp.price_jackets_woman, max_elements=12, perform_check=False)
            self.price_range_filter(prices, price_range)

        except (NoSuchElementException, TimeoutException) as e:
            print(f'Exception occurred: {str(e)}')
        finally:
            self.teardown()

if __name__ == "__main__":
    test_filter_search = TestFilterSearch()
    test_filter_search.run_test()
