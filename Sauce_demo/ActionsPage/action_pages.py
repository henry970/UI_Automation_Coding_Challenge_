import time
import logging
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException


from Sauce_demo.LocatorsPage.Locators import LoginPageLocators, OrderPageLocatorsBackPark, LogOutPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        try:
            enter_username = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LoginPageLocators.USERNAME))
            enter_username.send_keys(username)
            logging.info("Entered username successfully.")
        except Exception as e:
            logging.error(f"Error entering username: {e}")
            self.driver.save_screenshot(f"screenshots/username_not_clickable_.png")

    def enter_password(self, password):
        try:
            enter_password = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LoginPageLocators.PASSWORD))
            enter_password.send_keys(password)
            logging.info("Entered password successfully.")
        except Exception as e:
            logging.error(f"Error entering password: {e}")
            self.driver.save_screenshot(f"screenshots/password_not_clickable.png")

    def click_login_button(self):
        try:
            click_login_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
            click_login_button.click()
            logging.info("Login button clicked successfully.")
        except Exception as e:
            logging.error(f"Error clicking login button: {e}")
            self.driver.save_screenshot(f"screenshots/login_button_not_clickable.png")

    def assert_login_success(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LoginPageLocators.ASSERTION))
            logging.info("Login was successful.")
        except Exception as e:
            logging.error(f"Login failed: {e}")
            self.driver.save_screenshot(f"screenshots/login_failed.png")
            raise AssertionError("Login assertion failed.")



class OrderPageLocators:
    def __init__(self, driver):
        self.driver = driver

    def capture_screenshot(self, action_name):
        screenshot_name = f"{action_name}.png"
        self.driver.save_screenshot(screenshot_name)
        logging.info(f"Screenshot taken: {screenshot_name}")

    def click_back_park_button(self):
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(OrderPageLocatorsBackPark.ClICK_BACK_PARK))
            button.click()
            time.sleep(3)
        except (TimeoutException, ElementNotInteractableException) as e:
            logging.error("Back park button is not clickable.")
            logging.error(e)
            self.capture_screenshot("click_back_park_button")

    def click_continue_button(self):
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(OrderPageLocatorsBackPark.ClICK_CONTINUE))
            button.click()
            time.sleep(3)
        except (TimeoutException, ElementNotInteractableException) as e:
            logging.error("Continue button is not clickable.")
            logging.error(e)
            self.capture_screenshot("click_continue_button")

    def click_checkout_button(self):
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(OrderPageLocatorsBackPark.ClICK_CHECKOUT))
            button.click()
            time.sleep(3)
        except TypeError as e:
            logging.error("Element 'ClICK_CHECKOUT' is not iterable. Exception: %s", e)
            self.driver.save_screenshot("screenshot_click_checkout_button_error.png")

    def enter_firstName(self, first):
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(OrderPageLocatorsBackPark.FIRSTNAME))
            field.send_keys(first)
            time.sleep(3)
        except TypeError as e:
            logging.error("Element 'FIRSTNAME' is not iterable. Exception: %s", e)
            self.driver.save_screenshot("screenshot_enter_firstName_error.png")

    def enter_LastName(self, last):
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(OrderPageLocatorsBackPark.LASTNAME))
            field.send_keys(last)
            time.sleep(3)
        except TypeError as e:
            logging.error("Element 'LASTNAME' is not iterable. Exception: %s", e)
            self.driver.save_screenshot("screenshot_enter_LastName_error.png")

    def enter_Postal_Code(self, code):
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(OrderPageLocatorsBackPark.POSTAL_CODE))
            field.send_keys(code)
            time.sleep(3)
        except TypeError as e:
            logging.error("Element 'POSTAL_CODE' is not iterable. Exception: %s", e)
            self.driver.save_screenshot("screenshot_enter_Postal_Code_error.png")

    def click_continue_button1(self):
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(OrderPageLocatorsBackPark.ClICK_CONTINUE1))
            button.click()
            time.sleep(3)
        except TypeError as e:
            logging.error("Element 'ClICK_CONTINUE1' is not iterable. Exception: %s", e)
            self.driver.save_screenshot("screenshot_click_continue_button1_error.png")

    def click_finish_button(self):
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(OrderPageLocatorsBackPark.ClICK_FINISH))
            button.click()
            time.sleep(3)
        except TypeError as e:
            logging.error("Element 'ClICK_FINISH' is not iterable. Exception: %s", e)
            self.driver.save_screenshot("screenshot_click_finish_button_error.png")

    def click_back_button(self):
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(OrderPageLocatorsBackPark.CLICK_BACK_BUTTON))
            button.click()
            time.sleep(3)
        except TypeError as e:
            logging.error("Element 'CLICK_BACK_BUTTON' is not iterable. Exception: %s", e)
            self.driver.save_screenshot("screenshot_click_back_button_error.png")
    def assert_login_success(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(OrderPageLocatorsBackPark.ASSERTION))
            logging.info("Login was successful.")
        except Exception as e:
            logging.error(f"Login failed: {e}")
            self.driver.save_screenshot(f"screenshots/login_failed.png")
            raise AssertionError("Login assertion failed.")


class LogOutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_profile_tab(self):
        try:
            click_profile_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LogOutPageLocators.CLICK_PROFILE_TAB))
            click_profile_tab.click()
            time.sleep(3)
        except TypeError as e:
            logging.error("Element 'CLICK_PROFILE_TAB' is not iterable. Exception: %s", e)
            self.driver.save_screenshot("screenshot_profile_tab_error.png")

    def click_log_out_button(self):
        try:
            click_log_out_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LogOutPageLocators.CLICK_lOG_OUT_BUTTON))
            click_log_out_button.click()
            time.sleep(3)
        except TypeError as e:
            logging.error("Element 'CLICK_LOG_OUT_BUTTON' is not iterable. Exception: %s", e)
            self.driver.save_screenshot("screenshot_log_out_button_error.png")
