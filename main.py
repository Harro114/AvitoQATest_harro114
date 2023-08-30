import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service


class AvitoFavoritesTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path='./chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.base_url = "https://www.avito.ru"

    def test_add_favorite(self):
        # Переход на страницу избранных
        driver = self.driver

        # Добавление объявления в избранное с страницы товара
        driver.get(self.base_url + "/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")
        add_to_fav_button = driver.find_element(By.CLASS_NAME, "desktop-usq1f1")
        add_to_fav_button.click()

        driver.get(self.base_url + "/favorites")
        try:
            check_fav = driver.find_element(By.XPATH,
                                            '//a[@href="/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"]')
        except AssertionError:
            self.assertTrue(False, "Ad not at favorite")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
