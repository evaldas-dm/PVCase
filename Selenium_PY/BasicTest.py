import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep
import warnings
import urllib3
import xlrd
 
class PVCaseTest(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
    def test_login_crud(self):
        driver_chrome = webdriver.Chrome()
        self.driver = driver_chrome
        self.driver.implicitly_wait(10)
        driver_chrome.maximize_window()
        driver_chrome.get('http:qa.yield.pvcase.com')
 
        # Perform login operation

        wb = xlrd.open_workbook("TestData.xls")
        sheet = wb.sheet_by_name("data")

        rowCount = sheet.nrows
        colCount = sheet.ncols
        curr_row = 1
        print(rowCount)
        print(colCount)
# for loop to iterate through TestData.xls, to validate login and CRUD functions
        for curr_row in range(1, rowCount):
            #login validation part
            user_name = sheet.cell_value(curr_row, 0)
            password = sheet.cell_value(curr_row, 1)
            loginText = driver_chrome.find_element(By.LINK_TEXT, "Login here")
            loginText.click()
            #time.sleep(1)
            usernameInput = driver_chrome.find_element(By.NAME, "login")
            passwordInput = driver_chrome.find_element(By.NAME, "password")
            usernameInput.send_keys(user_name)
            passwordInput.send_keys(password)
            submitButton = driver_chrome.find_element(By.CSS_SELECTOR, "input[type='submit']")
            submitButton.click()
            helloText = driver_chrome.find_element_by_tag_name('h1')
            assert helloText.text == "Hello "+user_name
            print(user_name+" logged in successfully")
            ##CRUD validation
            #Verify CREATE
            memosLink = driver_chrome.find_element(By.LINK_TEXT, "Memos")
            memosLink.click()
            memoInput = driver_chrome.find_element(By.NAME, "memo")
            memoInput.clear()
            memoInput.send_keys("comment")
            memoSubmit = driver_chrome.find_element(By.XPATH, "//*[@id='usrform']/input")
            memoSubmit.click()
            #Verify READ
            memoTable = driver_chrome.find_element(By.XPATH, "//tbody/tr/td[3]")
            assert memoTable.text == "comment"
            #Verify UPDATE
            editLink = driver_chrome.find_element(By.LINK_TEXT, "Edit")
            editLink.click()
            editField = driver_chrome.find_element(By.XPATH, "//*[@id='usrform']/textarea")
            editField.clear()
            editField.send_keys("new comment")
            editSubmit = driver_chrome.find_element(By.XPATH, "//*[@id='usrform']/input")
            editSubmit.click()
            memoEdited = driver_chrome.find_element(By.XPATH, "//tbody/tr/td[3]")
            assert memoEdited.text == "new comment"
            #Verify DELETE
            deleteLink = driver_chrome.find_element(By.LINK_TEXT, "Delete")
            deleteLink.click()
            print("CRUD verification passed for user "+user_name)
            logoutButton = driver_chrome.find_element(By.TAG_NAME, "button")
            logoutButton.click()
            driver_chrome.get('http:qa.yield.pvcase.com')

 
    def tearDown(self):
        # Close the browser.
        self.driver.close()
        self.driver.quit()
 
if __name__ == '__main__':
    unittest.main()