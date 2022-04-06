import time

import pytest
import allure
from pages.demoblaze.home_page import HomePage
from pages.demoblaze.login_page import LoginPage
from pages.demoblaze.searchproduct import SearchProductPage


@pytest.mark.usefixtures("setup")
class TestHomePage:
    @allure.title("Home page - smoke test")
    @allure.description("Check if home page of Demoblaze has correct title")
    def test_homepage_title(self):
        homepage = HomePage(self.driver)
        homepage.open()
        # assert ("STORE" in homepage.get_page_title())
        LoginPage.open_login_page(self)
        LoginPage.login_with_credentials(self, "user@phptravels.com", "demouser")
        time.sleep(5)
        SearchProductPage.search_product(self)
