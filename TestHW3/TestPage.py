from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
    LOCATOR_PASS_FIELD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, '''button''')
    LOCATOR_ERROR_FIELD = (By.XPATH, '''//*[@id="app"]/main/div/div/div[2]/h2''')
    LOCATOR_POSITIVE_ENTER = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'Send {word} in {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send {word} in {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_name(self, word):
        logging.info(f'Send {word} in {TestSearchLocators.LOCATOR_NAME[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_NAME)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content(self, text):
        logging.info(f'Send {text} in {TestSearchLocators.LOCATOR_CONTENT[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        login_field.clear()
        login_field.send_keys(text)

    def click_button_send(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def click_contact_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT).click()

    def get_username_label(self):
        label_field = self.find_element(TestSearchLocators.LOCATOR_POSITIVE_ENTER, time=3)
        text = label_field.text
        logging.info(f'We found label {text} in label field {TestSearchLocators.LOCATOR_POSITIVE_ENTER[1]}')
        return text

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f'We found text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text
