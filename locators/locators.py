from selenium.webdriver.common.by import By


class LogInLocators:
    user_account_menu = (By.XPATH, "//div[@class='dropdown dropdown-login dropdown-tab']")
    login_link = (By.XPATH, "//*[@id='login2']")
    username_textbox = (By.XPATH, "//*[@id='loginusername']")
    password_textbox = (By.XPATH, "//*[@id='loginpassword']")
    phone_category_link = (By.XPATH, "//a[contains(text(),'Phones')]")
    samsung_phone_link = (By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]")
    add_to_cart_link = (By.XPATH, "//a[contains(text(),'Add to cart')]")