from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_LINK), "wrong css"
        add_basket_link.click()


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_right_name_and_price(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_OF_A_BOOK).text
        assert name == "Coders at Work", "Thats it"

    def should_not_be_success_message(self):
        assert \
            self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert \
            self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared"

