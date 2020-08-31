# -*- coding:utf-8 -*-
import os
import time
import logging
import warnings

from selenium.webdriver import Chrome, ChromeOptions

shimo_login_url = "https://shimo.im/login?from=home"


class Certify:

    def __init__(self, username=None, pwd=None,
                 executable_path="chromedriver",
                 log_level="INFO", headless=True):
        extra_options = ChromeOptions()
        extra_options.headless = headless
        self.driver = Chrome(executable_path, options=extra_options)
        self.username = username
        self.pwd = pwd
        self._load_username()
        self._load_pwd()
        self.log_level = log_level
        self._set_logger()

    def login(self):
        if not self.username or not self.pwd:
            warnings.warn(
                "Username or password is empty. You can login by "
                "setting 'SHIMO_USERNAME' and SHIMO_PASSWORD  environment variable.")
        self.logger.info("开始登录...")
        self.driver.get(shimo_login_url)
        time.sleep(3)
        self.driver.find_element_by_name("mobileOrEmail").send_keys(self.username)
        self.logger.info(f"输入用户名: {self.username}")
        self.driver.find_element_by_name("password").send_keys(self.pwd)
        self.logger.info(f"输入密码: {self.pwd}")
        self.driver.find_element_by_class_name("submit").click()
        time.sleep(3)
        if self.driver.current_url == "https://shimo.im/dashboard/used":
            self.show_doc_titles()
        else:
            tips = self.driver.find_element_by_class_name("tips")
            self.logger.error(f"登录失败，失败原因: {tips.text}")
        self.driver.quit()

    def show_doc_titles(self):
        titles = self.driver.find_elements_by_class_name("card-title")
        print(f"当前登录账户：{self.username}")
        print("当前文档列表：")
        for title in titles:
            print(f"    {title.text}")

    def _load_username(self):
        if self.username is None:
            self.username = os.environ.get("SHIMO_USERNAME", "")

    def _load_pwd(self):
        if self.pwd is None:
            self.pwd = os.environ.get("SHIMO_PASSWORD", "")

    def _set_logger(self):
        logging.basicConfig(
            format='[%(asctime)s]-[%(levelname)s] - %(message)s',
            datefmt='%m/%d/%Y %H:%M:%S')
        self.logger = logging.getLogger(self.__class__.__name__)
        try:
            self.logger.setLevel(self.log_level.upper())
        except ValueError:
            self.logger.setLevel("INFO")


if __name__ == '__main__':
    login = Certify()
    login.login()