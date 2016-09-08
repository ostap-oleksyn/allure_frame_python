import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from src.element import Element


class Action:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._position = 0
        self._timeout = 5

    def element(self, locator):
        self._locator = locator
        return self

    def at(self, position):
        self._position = position
        return self

    def wait(self, timeout):
        self._timeout = timeout
        return self

    def _wait_for_element(self):
        self._element = Element(self._driver, self._locator, self._position)
        WebDriverWait(self._driver, self._timeout).until(
            EC.visibility_of_element_located((By.XPATH, self._element.locator)),
            "{} is not visible after {} seconds".format(self._element.name, self._timeout))
        self._position = 0

    def _get_element(self):
        self._wait_for_element()
        element = self._driver.find_element_by_xpath(self._element.locator)  # type: WebElement
        return element

    def _get_elements(self):
        self._wait_for_element()
        elements = self._driver.find_elements_by_xpath(self._element.locator)
        return elements

    def type(self, text):
        element = self._get_element()
        with pytest.allure.step("Typed '{}' into {}".format(text, self._element.name)):
            element.send_keys(text)

    def submit(self):
        with pytest.allure.step("Pressed ENTER"):
            self._get_element().send_keys(Keys.ENTER)

    def click(self):
        element = self._get_element()
        with pytest.allure.step("Clicked {}".format(self._element.name)):
            element.click()

    def get_text(self):
        return self._get_element().text

    def get_count(self):
        return len(self._get_elements())
