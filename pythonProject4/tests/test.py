from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from pages.MainPage import MainPage


class VkTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.get('https://vk.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_search(self):
        search = MainPage(self.driver)
        search.enter_search('Привет')
        search.enter_search(Keys.ENTER)
        assert 'Результаты поиска' in self.driver.page_source
        pass

    def test_location(self):
        search = MainPage(self.driver)
        search.eng_lang()
        time.sleep(1)
        assert 'VK for mobile devices' in self.driver.page_source
        pass

    def test_wrong_password(self):
        search = MainPage(self.driver)
        search.enter_login('ilia.lukovoy@gmail.com')
        search.enter_password('mamama')
        search.enter_password(Keys.ENTER)
        time.sleep(1)
        assert 'Не удаётся войти.' in self.driver.page_source
        pass

    def test_reset_password(self):
        search = MainPage(self.driver)
        search.reset_password()
        search.enter_reset('ilia.lukovoy@gmail.com')
        search.enter_reset(Keys.ENTER)
        time.sleep(2)
        assert 'Введите текст с картинки' in self.driver.page_source
        pass

    def test_all_prod(self):
        search = MainPage(self.driver)
        search.all_prod()
        time.sleep(1)
        assert 'Мобильное приложение ВКонтакте' in self.driver.page_source
        pass

    def Off(self):
        self.driver.close()
        self.driver.quit()
        print("Gotovo! Klassno!!")
