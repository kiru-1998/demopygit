

#pytest -n 2 -m smoke --Browser-name firefox --html = reports/report.html

import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import presence_of_element_located, alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Pageobjects.Login import LoginPage

from Pageobjects.Login import LoginPage
from Pageobjects.shop import ShopPage

test_data_path="../Data/test_e2eframework.json"

with open(test_data_path)as f:
    test_data=json.load(f) # this method will convert json file to python

test_list=test_data['data']


@pytest.mark.parametrize('test_list_item',test_list)

def test_e2e(BrowserInstance,test_list_item):
    driver = BrowserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    loginpage=LoginPage(driver)
    shoppage=loginpage.login(test_list_item['userEmail'],test_list_item['userPasswd'])
    shoppage.add_product_cart(test_list_item['productName'])
    checkout_confirm=shoppage.go_to_cart()
    checkout_confirm.Checkout()
    checkout_confirm.delivery_address('India')
    checkout_confirm.validate()










# out of 50  test realy want to run test case parallel in pytest framework
#pytest -n 2  - pytest-xdist is plugin
