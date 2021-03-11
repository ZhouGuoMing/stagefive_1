# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : base_page.py
# 基类，存放init ，find
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            option = Options()
            # option.debugger_address = "127.0.0.1:9222"
            # self.driver = webdriver.Chrome(options=option)
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        if self.base_url != "":
            self.driver.get(self.base_url)

        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851061042340'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'FynnjF00byUvc4LsgyYTBG5RCRqdT35z5rT6suQV8Cahhs2aYh2l6Ie4a6r-pBKVAcRmoKDSf9wII211EA2yIyTESLfGwZ2aCbr4V7LkwhnTZJ_fLoSG79bHlXnwp9f8fAIWY_1vj2mMkNoeHe9qW6ybz3EXIIPI13sxNETIfqhQ2RGDy61MyihJzml9870gnCp7Bm96S0gTz3mnVceBPJSTYDbS852SRNMQxxSIpn7WbMGjh3xHJQ1RiXFze9GnwI87CUCzBetCjfVQTkbD9Q'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851061042340'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324973429766'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7160240'}, {'domain': 'work.weixin.qq.com', 'expiry': 1615474206, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4p8oc16'}, {'domain': '.qq.com', 'expiry': 1615529080, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1080057953.1615442672'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '0270832'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'P4oSJeD6DQ9KIptW8BTbsOWAOaNwFE_Uso8dfrhWi_Q5Yyu8NMa62_w5ccpJ7Bf4'}, {'domain': '.qq.com', 'expiry': 1615442732, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1678514680, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1491031827.1615442672'}, {'domain': '.work.weixin.qq.com', 'expiry': 1646978670, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1618034682, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        # self.driver.get(self.base_url)

    def get_cookie(self):
        self.driver.get_cookie()

    def get_url(self,base_url):
        self.driver.get(base_url)

    def quit_driver(self):
        return self.driver.quit()

    def find(self,locator, value):
        return self.driver.find_element(locator, value)

    def finds(self,locator, value):
        return self.driver.find_elements(locator, value)

    def wait_for_click(self,timeout,locator):
        WebDriverWait(self.driver,timeout).until(expected_conditions.element_to_be_clickable(locator))