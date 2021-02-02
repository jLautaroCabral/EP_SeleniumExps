import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath(
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[1]/div[4]/ul/li/div/h2/a')
        self.assertEquals(1, len(products))
    # def test_search_text_field(self):
    #     search_field = self.driver.find_element_by_id('search')

    # def test_search_text_field_by_name(self):
    #     search_field = self.driver.find_element_by_name('q')

    # def test_search_text_field_by_class_name(self):
    #     search_field = self.driver.find_element_by_class_name('input-text')

    # def test_search_button_enabled(self):
    #     button = self.driver.find_element_by_name('button')

    # def test_count_of_promo_banner_images(self):
    #     banner_list = self.driver.find_element_by_class_name('promos')
    #     banners = banner_list.find_elements_by_tag_name('img')
    #     self.assertEqual(3, len(banners))

    # def test_vip_promo(self):
    #     vip_promo = self.driver.find_element_by_xpath(
    #         '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/ul/li[1]/a/img')

    # def test_shopping_cart(self):
    #     shopping_cart_icon = self.driver.find_element_by_css_selector(
    #         '.header-minicart span.icon')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reportes2', report_name='hello-world-report'))
