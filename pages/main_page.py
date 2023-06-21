from .base_page import BasePage
from .locators import BasketPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_not_be_items_in_basket(self):
        assert \
            self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "There are items in your basket "

    def should_be_empty_basket_message(self):
        assert \
            self.is_element_present(*BasketPageLocators.BASKET_TEXT_ABOUT_EMPTY), \
            "Your basket is not empty"


