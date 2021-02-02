import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep


class LanguageSelect(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://google.com/")

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys("platzi")
        search_field.submit()

        driver.back()
        sleep(10)
        driver.forward()
        sleep(10)
        driver.refresh()
        sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(output="reportes6", report_name="hello-world-report"),
    )
