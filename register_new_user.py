import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver
        bug = '#######################'

        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        print(bug)

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())

        first_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('Test@email.com')
        news_letter_subscription.send_keys('Test')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reportes3', report_name='hello-world-report'))
