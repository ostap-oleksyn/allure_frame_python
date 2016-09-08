import pytest


def message(text):
    with pytest.allure.step("LOG: {}".format(text)):
        pass
