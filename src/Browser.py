import time
import re
from log import log
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import json


class Browser:

    def __init__(self,street_name,street_number,neighborhood):
        self.street_name = street_name
        self.street_number = street_number
        self.neighborhood = neighborhood
        self.options = Options()
        # self.options.add_argument('--headless')
        self.options.page_load_strategy = 'eager'
        self.driver = webdriver.Firefox(options=self.options)
        self.session_id = self.driver.session_id
        self.command_executor_url = self.driver.command_executor._url
    
    def goto(self, url,need_config):
        try:
            if need_config == True:
                log().info(f"Starting config location for:{self.street_name},{self.street_number},{self.neighborhood}")
                self.config_location()
                if self.driver.current_url != url:
                    log().info(f"Going to {url}")
                    self.driver.get(url)
            else:
                if self.driver.current_url != url:
                    log().info(f"Going to {url}")
                    self.driver.get(url)
        except Exception as err:
            log().error(f"Error in method goto: {type(err)} > {err}")
            raise err
    
    def config_location(self):
        try:
            self.driver.get("https://www.ze.delivery/")
            time.sleep(3)
            try:
                self.driver.find_element_by_class_name('accept-cookie-container').click()
                time.sleep(1)
            except:
                pass
            self.driver.find_element_by_id('age-gate-button-yes').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="fake-address-search-input"]').click()
            adress_bar = self.driver.find_element_by_xpath('//*[@id="address-search-input-address"]')
            adress_bar.clear()
            time.sleep(2)
            adress_bar.send_keys(self.street_name  + self.street_number  + self.neighborhood)
            time.sleep(3)
            self.driver.find_elements_by_class_name('css-10klw3m')[0].click()
            time.sleep(2)
            self.driver.find_element_by_class_name('css-e0qn0l-checkboxText').click()
            time.sleep(5)
            self.driver.find_element_by_id("address-details-button-continue").click()
            time.sleep(5)
            
            return True
        
        except Exception as err:
            log().error(f"Error in method config_location: {type(err)} > {err}")
            raise err

    def __del__(self):
        if hasattr(self, 'driver') and self.driver is not None:
            self.driver.quit()

