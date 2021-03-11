# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : add_member_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from live_homework.page.base_page import BasePage

class AddMemberPage(BasePage):

    def add_member(self,username,account,phonenum):
        # 输入  用户名
        self.find(By.ID,"username").send_keys(username)
        # 输入  帐号
        self.find(By.ID,"memberAdd_acctid").send_keys(account)
        # 输入  手机号
        self.find(By.ID,"memberAdd_phone").send_keys(phonenum)
        # 点击  保存
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        return self.driver

    def get_member(self):
        # 显式等待
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")))
        locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")
        self.wait_for_click(10,locator)
        # find_elements 查找页面 上的相同属性的所有元素，[element1,element2......]
        eles_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print(eles_list)
        names = []
        for ele in eles_list:
            names.append(ele.get_attribute("title"))


        return names