import allure
from selenium.webdriver.firefox.webdriver import WebDriver


class PageAction:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @allure.step("Opened {1}")
    def open(self, url):
        self._driver.get(url)

    @allure.step("SCREENSHOT")
    def take_screenshot(self):
        allure.attach('screenshot.png', self._driver.get_screenshot_as_png(), allure.attach_type.PNG)
