import random

import pytest
from selenium.webdriver.firefox.webdriver import WebDriver

from src.action import Action
from src.base_page import BasePage
from src.locators import HomePageLoc


class ResultPage(BasePage):
    def __init__(self, driver: WebDriver, action: Action):
        super().__init__(driver, action)

    @staticmethod
    def click_random_link():
        with pytest.allure.step("Clicked random link"):
            links = BasePage.action.element(HomePageLoc.RESULT_LINK).get_count()
            BasePage.action.element(HomePageLoc.RESULT_LINK).at(random.randint(1, links)).click()
