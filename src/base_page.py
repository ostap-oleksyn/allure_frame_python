from selenium.webdriver.firefox.webdriver import WebDriver

from action import Action


class BasePage:
    driver = None  # type: WebDriver
    action = None  # type: Action

    def __init__(self, driver: WebDriver, action: Action):
        BasePage._driver = driver
        BasePage.action = action
