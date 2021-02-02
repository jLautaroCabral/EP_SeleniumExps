import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class LanguageSelect(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):

        driver = self.driver
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_language= Select(self.driver.find_element_by_id('select-language'))

        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)

        #Verifico que las lsiatas sean iguales
        self.assertListEqual(act_options, exp_options)
        #Verifico que idionma esta seleciionado
        self.assertEqual('English', select_language.first_selected_option.text)
        #Seleccionar el idioma German
        select_language.select_by_visible_text('German')
        #verifico que en la url diga store=german
        self.assertTrue('store=german' in self.driver.current_url)
        #selecciono por indice me devuelvo a Ingles
        select_language= Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reportes4', report_name='hello-world-report'))
