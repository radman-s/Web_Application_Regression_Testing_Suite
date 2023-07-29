from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class BaseElement(object):
    def __init__(self, driver, locator, name):
        self.driver = driver
        self.locator = locator
        self.name = name
        self.web_element = None
        self.find()

    def find(self, multiple=False):
        try:
            if multiple:
                elements = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_all_elements_located(locator=self.locator))
                self.web_elements = elements
            else:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
                self.web_element = element
        except NoSuchElementException:
            print(f'Element(s) not found: {self.name}')
        except TimeoutException:
            print(f'Element(s) not visible: {self.name}')

    def is_displayed(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator=self.locator))
        self.web_element = element
        return self.web_element.is_displayed()

    def click(self):
        element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.locator))
        element.click()
        return None

    def click_simple(self):
        self.web_element.click()
        return None

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    def text(self):
        text = self.web_element.text
        return text

    def clear(self):
        self.web_element.clear()
        return None

    def select_dropdown(self, val):
        element = Select(self.web_element)
        element.select_by_value(val)
        return None

    def arrow_down(self):
        element = ActionChains(self.driver)
        element.send_keys(Keys.ARROW_DOWN)
        return None

    def enter(self):
        element = ActionChains(self.driver)
        element.send_keys(Keys.ENTER).perform()
        return None

    def move_to(self):
        element = ActionChains(self.driver)
        element.move_to_element(self.web_element).perform()
        return None
