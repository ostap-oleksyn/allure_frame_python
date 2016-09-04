import pytest
from selenium.webdriver.firefox.webdriver import WebDriver

from action import Action
from base_page import BasePage
from locators import HomePageLoc
from result_page import ResultPage


class HomePage(BasePage):
    def __init__(self, driver: WebDriver, action: Action):
        super().__init__(driver, action)

    @staticmethod
    def search_for(text):
        with pytest.allure.step("Search for '{}'".format(text)):
            BasePage.action.element(HomePageLoc.SEARCH_FIELD).type(text)
            BasePage.action.element(HomePageLoc.SEARCH_FIELD).submit()
        return ResultPage(BasePage.driver, BasePage.action)
