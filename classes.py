from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from random import uniform

class InternetSpeedTwitterBot:
    def __init__(self, username, password, min_down_speed, min_up_speed):
        self.min_up_speed = min_up_speed
        self.min_down_speed = min_down_speed
        self.username = username
        self.password = password
        self.twitter_driver = None
        self.sign_in_button = None
        self.start_test_button = None
        self.cookie_accept_button = None
        self.down_speed = 0
        self.upload_speed = 0
        self.username_box = None
        self.password_box = None
        self.driver_options = webdriver.ChromeOptions()
        self.driver_options.add_experimental_option("detach", True)
        self.driver = None
        self.status_sharing_box = None
        self.status_textbox = None
        self.status_submitting_button = None

    def get_internet_speed(self):
        self.driver = webdriver.Chrome(options=self.driver_options)
        self.driver.get(url="https://www.speedtest.net/")
        self.driver.maximize_window()
        time.sleep(uniform(3.0, 4.0))
        self.cookie_accept_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[2]/div"
                                                                       "/div/button[2]")
        self.cookie_accept_button.click()
        time.sleep(uniform(0.5, 0.9))
        self.start_test_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]"
                                                                    "/div[3]/div[1]/a/span[4]")
        self.start_test_button.click()
        time.sleep(45)
        self.down_speed = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.upload_speed = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        print(f"Down speed - {self.down_speed}\nUp speed - {self.upload_speed}")
        self.driver.quit()

    def tweet_at_provider(self):
        self.twitter_driver = webdriver.Chrome(options=self.driver_options)
        self.twitter_driver.get(url="https://twitter.com/")
        time.sleep(uniform(3.0, 4.0))
        self.sign_in_button = self.twitter_driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a")
        self.sign_in_button.click()
        time.sleep(uniform(2.0, 3.0))
        self.username_box = self.twitter_driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/"
                                                                   "div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div"
                                                                   "/div/div[5]/label/div/div[2]/div/input")

        time.sleep(uniform(0.5, 1.0))
        self.username_box.send_keys(self.username, Keys.ENTER)
        time.sleep(uniform(1.0, 1.5))
        self.password_box = self.twitter_driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div"
                                                                       "/div/div/div/div[2]/div[2]/div/div/div[2]/div"
                                                                       "[2]/div[1]/div/div/div[3]/div/label/div/div[2]"
                                                                       "/div[1]/input")
        self.password_box.click()
        time.sleep(uniform(0.5, 1.0))
        self.password_box.send_keys(self.password, Keys.ENTER)
        time.sleep(uniform(4.0, 5.0))
        # So far everything works
        self.status_sharing_box = self.twitter_driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/"
                                                                             "div/div/div/div/div/a/div[2]/div/div/span")
        self.status_sharing_box.click()
        time.sleep(uniform(1.5, 2.0))
        self.status_textbox = self.twitter_driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div"
                                                                         "/div/div/div/div/div[2]/div[2]/div/div/div/"
                                                                         "div[3]/div[2]/div[1]/div/div/div/div[1]/div"
                                                                         "[2]/div/div/div/div/div/div/div/div/div/div"
                                                                         "/div/label/div[1]/div/div/div/div/div/div[2]"
                                                                         "/div")
        self.status_textbox.send_keys(f"Hey Internet Provider, why is my internet speed {self.down_speed}down"
                                      f"/{self.upload_speed}up when I pay for {self.min_down_speed}down/"
                                      f"{self.min_up_speed}up?")
        time.sleep(uniform(0.5, 1.0))
        self.status_submitting_button = self.twitter_driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]"
                                                                                   "/div[2]/div/div/div/div/div/div[2]"
                                                                                   "/div[2]/div/div/div/div[3]/div[2]"
                                                                                   "/div[1]/div/div/div/div[2]/div[2]"
                                                                                   "/div/div/div/div[4]")
        self.status_submitting_button.click()
        time.sleep(2)
        self.twitter_driver.quit()








