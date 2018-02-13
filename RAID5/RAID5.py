from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
        driver.find_element_by_css_selector("span.icon-44.icon-44-database").click()
        driver.find_element_by_css_selector("span.icon-32.icon-32-pool").click()
        driver.find_element_by_css_selector("span.icon-44.icon-44-add").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("autotest")
        time.sleep(2)
        driver.find_element_by_css_selector("select[name=\"raid\"]").click()
        Select(driver.find_element_by_xpath("//div[@id='raid']/select")).select_by_visible_text("RAID5")
        driver.find_element_by_name("raid").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div[3]/div/div[2]/div[2]/div/form/div[5]/div").click()
        driver.find_element_by_css_selector("label.checkbox-label").click()
        driver.find_element_by_css_selector("div.multi-item.multi-item-active > div.checkbox > label.checkbox-label").click()
        driver.find_element_by_xpath("//div[8]/div/button").click()
        time.sleep(2)

        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[5]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[11]/button/span/span").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/label").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_css_selector("div.loader-spinner").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div[2]/div").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[3]/button/span/span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[11]/div/button").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div[3]/div[2]/div[2]/div[2]/div/form/div[2]/div/input").clear()
        driver.find_element_by_xpath("//body[@id='main']/div/div[3]/div[2]/div[2]/div[2]/div/form/div[2]/div/input").send_keys("ok")
        driver.find_element_by_xpath("//div[4]/div/button").click()



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




