from ssqatest.src.helpers.config_helpers import get_base_url
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.HomePageLocators import HomePageLocators
import logging as logger


class HomePage(HomePageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
        
    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BTN)

