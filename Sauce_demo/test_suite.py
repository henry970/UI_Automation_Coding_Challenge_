import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Config.config import Config, ConfigOrderPage
from Sauce_demo.ActionsPage.action_pages import LoginPage, OrderPageLocators, LogOutPage


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url(Config.BaseUrl)
    return login_page


def test_login_page_on_sauce_demo_website(login):
    login.enter_username(Config.UserName)
    login.enter_password(Config.Password)
    login.click_login_button()


def test_order_product_on_sauce_demo_website(login):
    test_login_page_on_sauce_demo = OrderPageLocators(login.driver)
    test_login_page_on_sauce_demo.click_back_park_button()
    test_login_page_on_sauce_demo.click_continue_button()
    test_login_page_on_sauce_demo.click_checkout_button()
    test_login_page_on_sauce_demo.enter_firstName(ConfigOrderPage.FirstName)
    test_login_page_on_sauce_demo.enter_LastName(ConfigOrderPage.LastName)
    test_login_page_on_sauce_demo.enter_Postal_Code(ConfigOrderPage.PostalCode)
    test_login_page_on_sauce_demo.click_continue_button1()
    test_login_page_on_sauce_demo.click_finish_button()
    test_login_page_on_sauce_demo.click_back_button()



def test_log_out_page_on_sauce_demo_website(login):
    test_log_out_page_on_sauce_demo = LogOutPage(login.driver)
    test_log_out_page_on_sauce_demo.click_profile_tab()
    test_log_out_page_on_sauce_demo.click_log_out_button()
