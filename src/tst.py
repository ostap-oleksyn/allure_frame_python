import time
from selenium import webdriver

from action import Action
from home_page import HomePage
from locators import HomePageLoc
from page_action import PageAction


class Test:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.action = Action(self.driver)
        self.page = PageAction(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    def test(self):
        page = PageAction(self.driver)
        action = Action(self.driver)

        page.open("https://google.com")
        action.element(HomePageLoc.SEARCH_FIELD).type("python")
        action.element(HomePageLoc.SEARCH_FIELD).submit()

        t1 = action.element(HomePageLoc.RESULT_LINK).at(3).get_text()
        t2 = action.element(HomePageLoc.RESULT_LINK).get_text()
        print(t1)
        print(t2)

    def test1(self):
        self.page.open("https://google.com")
        home_page = HomePage(self.driver, self.action)
        result_page = home_page.search_for("python")
        result_page.click_random_link()
        time.sleep(5)
        self.page.take_screenshot()
