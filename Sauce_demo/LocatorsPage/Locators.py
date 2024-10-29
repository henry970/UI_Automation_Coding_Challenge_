from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.NAME, "user-name")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ASSERTION = (By.XPATH, '/html/body/div/div/div/div[1]/div[2]/span')


class OrderPageLocatorsBackPark:
    ClICK_BACK_PARK = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div')
    ClICK_CONTINUE = (By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a')
    ClICK_CHECKOUT = (By.ID, 'checkout')
    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    ClICK_CONTINUE1 = (By.ID, 'continue')
    ClICK_FINISH = (By.ID, "finish")
    CLICK_BACK_BUTTON = (By.ID, "back-to-products")
    ASSERTION = (By.XPATH, '/html/body/div/div/div/div[1]/div[2]/span')



class LogOutPageLocators:
    CLICK_PROFILE_TAB = (By.ID, "react-burger-menu-btn")
    CLICK_lOG_OUT_BUTTON = (By.ID, "logout_sidebar_link")


