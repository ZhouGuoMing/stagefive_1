# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : test_login.py
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Testlogin:
    def setup(self):
        '''
        复用浏览器:
        配置chrome启用路径到环境变量
        启动命令：chrome --remote-debugging-port=9222
        访问http://localhost:9222/
        '''
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        option.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome(options=option)
        # option1 = webdriver.ChromeOptions


    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # self.driver.get_cookies()
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # 打开 index页面，这时候需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 带有登录信息的cookie
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851061042340'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'FynnjF00byUvc4LsgyYTBG5RCRqdT35z5rT6suQV8Cahhs2aYh2l6Ie4a6r-pBKVAcRmoKDSf9wII211EA2yIyTESLfGwZ2aCbr4V7LkwhnTZJ_fLoSG79bHlXnwp9f8fAIWY_1vj2mMkNoeHe9qW6ybz3EXIIPI13sxNETIfqhQ2RGDy61MyihJzml9870gnCp7Bm96S0gTz3mnVceBPJSTYDbS852SRNMQxxSIpn7WbMGjh3xHJQ1RiXFze9GnwI87CUCzBetCjfVQTkbD9Q'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851061042340'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324973429766'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7160240'}, {'domain': 'work.weixin.qq.com', 'expiry': 1615474206, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4p8oc16'}, {'domain': '.qq.com', 'expiry': 1615529080, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1080057953.1615442672'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '0270832'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'P4oSJeD6DQ9KIptW8BTbsOWAOaNwFE_Uso8dfrhWi_Q5Yyu8NMa62_w5ccpJ7Bf4'}, {'domain': '.qq.com', 'expiry': 1615442732, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1678514680, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1491031827.1615442672'}, {'domain': '.work.weixin.qq.com', 'expiry': 1646978670, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1618034682, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 重新打开 已带有cookie 信息的index 页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def test_importcontact(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        action=TouchActions(self.driver)
        el=self.driver.find_element(By.CSS_SELECTOR, ".frame_logo")
        action.scroll_from_element(el,0,10000).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys("C:/Users/zhouguoming/Desktop/datas.xlsx")
        assert "datas.xlsx" == self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
