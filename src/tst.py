import time

from selenium import webdriver

from src import log
from src.action import Action
from src.locators import HomePageLoc
from src.page_action import PageAction


class Test:

    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.action = Action(self.driver)
        self.page = PageAction(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    def test(self):
        self.page.open("https://google.com")
        self.action.element(HomePageLoc.SEARCH_FIELD).type("python")
        self.action.element(HomePageLoc.SEARCH_FIELD).submit()
        t1 = self.action.element(HomePageLoc.RESULT_LINK).at(3).get_text()
        self.page.take_screenshot()
        t2 = self.action.element(HomePageLoc.RESULT_LINK).get_text()
        log.message(t1)
        self.action.element(HomePageLoc.RESULT_LINK).at(10).click()
        time.sleep(5)
        self.page.navigate_back()
        self.action.element(HomePageLoc.RESULT_LINK).click()
        print(t1)
        print(t2)
