from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestCondiutLogin(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get('http://localhost:1667')
        time.sleep(1)

    def teardown(self):
        self.driver.quit()

    # # Test1
    def test__home_page_appearances(self):
        assert self.driver.title == 'Conduit'

    # Test3
    def test_cookie_accept(self):
        self.driver.maximize_window()
        cookie_accept = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'cookie__bar__buttons__button--accept'))
        )
        cookie_accept.click()
        try:
            WebDriverWait(
                self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, 'cookie-policy-panel'))
            )
            not_found = False
        except:
            not_found = True

        assert not_found

    # Test3
    def test_sign_up(self):
        self.driver.maximize_window()
        self.driver.find_element_by_partial_link_text('Sign up').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys('R1')
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('r1@gmail.com')
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys('Rr0123456')
        self.driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()
        time.sleep(2)
        element = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'swal-text'))
        )

        assert element.text == 'Your registration was successful!'

    # Test2
    def test_login(self):
        self.driver.maximize_window()
        self.driver.find_element_by_partial_link_text('Sign in').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('r1@gmail.com')
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys('Rr0123456')
        self.driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()
        element = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'R1'))
        )
        assert element.text == 'R1'
