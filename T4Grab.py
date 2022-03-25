import string
from time import sleep
from tokenize import String
import xlrd

import undetected_chromedriver as uc
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def delay(waiting_time=5):
    driver.implicitly_wait(waiting_time)


def is_t4():
    sleep(10)
    newtxt = driver.find_element(By.XPATH,
                                 '//*[@id="cell-OMAze2Hp239U"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div['
                                 '1]/div/colab-static-output-renderer/div[1]/div/pre').get_attribute(
        "outerHTML")
    ftxt = "Tesla T4 "
    if ftxt in newtxt:
        return True


def chk_gpu1():
    ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.RETURN).key_up(Keys.CONTROL).perform()

    sleep(3)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    sleep(1)
    ActionChains(driver).send_keys(Keys.RETURN).perform()
    # CHECK IF GPU IS T4
    # READ STREAM OUTPUT
    sleep(30)


def chk_gpu():
    ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.RETURN).key_up(Keys.CONTROL).perform()

    # sleep(3)
    # ActionChains(driver).send_keys(Keys.TAB).perform()
    # sleep(1)
    # ActionChains(driver).send_keys(Keys.RETURN).perform()
    # CHECK IF GPU IS T4
    # READ STREAM OUTPUT
    sleep(30)


if __name__ == '__main__':
    wb = xlrd.open_workbook('demo.xls')
    sh = wb.sheet_by_name('log')
    rowCount = sh.nrows
    colCount = sh.ncols
    for curr_row in range(0, rowCount, 1):
        uname = sh.cell_value(curr_row, 0)
        upass = sh.cell_value(curr_row, 1)

        driver = uc.Chrome()
        driver.get('https://accounts.google.com/')

        # add email
        driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(uname)
        driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
        sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(upass)
        driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
        sleep(2)
        driver.get('https://colab.research.google.com/drive/1CibQ4uHkXI0o9qC-778qFbQgrUWq1GAv?usp=sharing')
        sleep(5)
        chk_gpu1()
        # keysPressed = Keys.chord(Keys.CONTROL, Keys.RETURN)
        # ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.RETURN).key_up(Keys.CONTROL).perform()
        #
        # sleep(3)
        # ActionChains(driver).send_keys(Keys.TAB).perform()
        # sleep(1)
        # ActionChains(driver).send_keys(Keys.RETURN).perform()
        # # CHECK IF GPU IS T4
        # # READ STREAM OUTPUT
        # sleep(30)
        i = 1
        while i <= 4:

            is_t4()
            if is_t4 is True:
                print("Found Tesla T4")

                break
            else:
                print("[INFO] Not found ... Retrying..." + i + " Try")
                print("[INFO] Do factory reset manually")
                # driver.find_element(By.XPATH, '//*[@id="runtime-menu-button"]/div/div/div[1]').click()
                sleep(10)

                chk_gpu()
                i = i + 1

        ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.F9).key_up(Keys.CONTROL).perform()
        sleep(20)
        # switch to captcha frame

        # TO DO
        # Check if captcha appear
        # Solve Recaptcha
        ###############
        driver.find_element_by_partial_link_text("https://tmate.io").click()
        driver.switch_to.window(driver.window_handles[1])
        sleep(5)
        ActionChains(driver).send_keys('q').perform()
        sleep(2)
        ActionChains(driver).send_keys('nvidia-smi').perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        sleep(20)

    sleep(999999)
