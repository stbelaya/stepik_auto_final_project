from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def fill_text_field(self, how, what, value):
        field = self.browser.find_element(how, what)
        field.send_keys(value)

    def go_to_basket_page(self):
        self.should_be_view_basket_button()
        view_basket_button = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        view_basket_button.click()

    def go_to_login_page(self):
        self.should_be_login_link()
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)

    def search_product(self, text):
        search_field = self.browser.find_element(*BasePageLocators.SEARCH_INPUT)
        search_button = self.browser.find_element(*BasePageLocators.SEARCH_BUTTON)
        search_field.send_keys(text)
        search_button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_search_button(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_BUTTON), "Search button is not presented"

    def should_be_search_field(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_INPUT), "Search field is not presented"

    def should_be_view_basket_button(self):
        assert self.is_element_present(*BasePageLocators.VIEW_BASKET_BUTTON), "View Basket button is not presented"

    # def solve_quiz_and_get_code(self):
    #     alert = self.browser.switch_to.alert
    #     x = alert.text.split(" ")[2]
    #     answer = str(math.log(abs((12 * math.sin(float(x))))))
    #     alert.send_keys(answer)
    #     alert.accept()
    #     try:
    #         alert = self.browser.switch_to.alert
    #         alert_text = alert.text
    #         print(f"Your code: {alert_text}")
    #         alert.accept()
    #     except NoAlertPresentException:
    #         print("No second alert presented")
