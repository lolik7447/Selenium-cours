from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_TEXT_ABOUT_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTRATION_FORM = (By.CSS_SELECTOR, "input[name='registration-email']")
    PASS_REGISTRATION_FORM1 = (By.CSS_SELECTOR, "input[name='registration-password1']")
    PASS_REGISTRATION_FORM2 = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTRATION_BTN = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_OF_A_BOOK = (By.CSS_SELECTOR, "div.alertinner strong")
    PRICE_OF_A_BOOK = (By.CSS_SELECTOR, "div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1)")

