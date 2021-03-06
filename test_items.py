import pytest
from selenium import webdriver
import time

def presence_button(browser):
   try:
      button = browser.find_element_by_css_selector("#add_to_basket_form > button")
      return True
   except:
      return False

def test_for_the_presence_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert presence_button(browser), "Button not found!"
    time.sleep(3)
