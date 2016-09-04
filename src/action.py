import copy

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def modify_position(func):
    def inner(*args):
        locator = copy.copy(args[1])
        if args[2] != 0 and "?" in locator[1]:
            locator[1] = args[1][1].replace("?", str(args[2]))
        elif args[2] != 0 and "?" not in args[1]:
            raise ValueError("Locator doesn't have a modifier - {}".format(args[1][1]))
        elif args[2] == 0 and "?" in locator[1]:
            locator[1] = args[1][1].replace("?", ".")
        return func(args[0], locator, args[2], args[3])

    return inner


class Action:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._locator = None
        self._position = 0
        self._timeout = 30

    def element(self, locator):
        self._locator = locator
        return self

    def at(self, position):
        self._position = position
        return self

    def wait(self, timeout):
        self._timeout = timeout
        return self

    @modify_position
    def _get_element(self, locator, position, timeout):
        WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator[1])),
                                                   "[{}] > [{}] not visible after {} seconds".format(locator[2],
                                                                                                     locator[0],
                                                                                                     timeout))

        element = self._driver.find_element_by_xpath(locator[1])  # type: WebElement
        self._position = 0
        return element

    @modify_position
    def _get_elements(self, locator, position, timeout):
        WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator[1])),
                                                   "[{}] > [{}] not visible after {} seconds".format(locator[2],
                                                                                                     locator[0],
                                                                                                     timeout))

        elements = self._driver.find_elements_by_xpath(locator[1])
        self._position = 0
        return elements

    def type(self, text):
        with pytest.allure.step("Typed '{}' into [{}] > [{}]".format(text, self._locator[2], self._locator[0])):
            self._get_element(self._locator, self._position, self._timeout).send_keys(text)

    def submit(self):
        with pytest.allure.step("Pressed ENTER"):
            self._get_element(self._locator, self._position, self._timeout).send_keys(Keys.ENTER)

    def click(self):
        with pytest.allure.step(
                "Clicked [{}] > [{}] at position [{}]".format(self._locator[2], self._locator[0], self._position)):
            self._get_element(self._locator, self._position, self._timeout).click()

    def get_text(self):
        return self._get_element(self._locator, self._position, self._timeout).text

    def get_count(self):
        return len(self._get_elements(self._locator, self._position, self._timeout))
