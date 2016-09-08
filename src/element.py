from selenium.webdriver.firefox.webdriver import WebDriver


class Element:
    def __init__(self, driver: WebDriver, locator: list, position):
        self._driver = driver
        self._locator = locator[1]
        self._name = "[{}] > [{}]".format(locator[2], locator[0])
        self._modify(locator, position)

    def _modify(self, locator, position):
        if position != 0 and "?" in locator[1]:
            self._locator = locator[1].replace("?", str(position))
            self._name = "[{}] > [{}] at position [{}]".format(locator[2], locator[0], position)
        elif position != 0 and "?" not in locator[1]:
            raise ValueError(
                "Locator [{}] > [{}] doesn't have a modifier - {}".format(locator[2], locator[0], locator[1]))
        elif position == 0 and "?" in locator[1]:
            self._locator = locator[1].replace("?", ".")
            self._name = "[{}] > [{}]".format(locator[2], locator[0])

    @property
    def locator(self):
        return self._locator

    @property
    def name(self):
        return self._name
