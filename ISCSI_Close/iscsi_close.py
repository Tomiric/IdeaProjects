from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver

        driver.get("https://172.16.11.35/auth")
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("admin")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_css_selector("button.button-text.button-text-large").click()
        driver.find_element_by_css_selector("span.icon-44.icon-44-security").click()
        driver.find_element_by_css_selector("span.icon-32.icon-32-access").click()
        driver.find_element_by_css_selector("div.table-row > div.table-cell-100").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[3]/button/span/span").click()
        driver.find_element_by_css_selector("input.input").clear()
        driver.find_element_by_css_selector("input.input").send_keys("ok")
        driver.find_element_by_css_selector("button.button-text").click()
        time.sleep(2)
        driver.find_element_by_css_selector("span.icon-44.icon-44-protocol").click()
        driver.find_element_by_css_selector("span.icon-32.icon-32-iscsi").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div[3]/div/div[2]/div[2]").click()
        driver.find_element_by_css_selector("span.button-icon-image > span.icon-44.icon-44-settings").click()
        driver.find_element_by_css_selector("button.button-text").click()
        driver.find_element_by_css_selector("input.input").clear()
        driver.find_element_by_css_selector("input.input").send_keys("ok")
        driver.find_element_by_css_selector("div.form-cell.form-cell-center.form-cell-100 > button.button-text").click()

        driver.find_element_by_css_selector("span.icon-44.icon-44-database").click()
        driver.find_element_by_css_selector("span.icon-32.icon-32-volume").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[4]/div").click()
        driver.find_element_by_css_selector("span.button-icon-image > span.icon-44.icon-44-settings").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_css_selector("input.input").clear()
        driver.find_element_by_css_selector("input.input").send_keys("ok")
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        time.sleep(3)


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
