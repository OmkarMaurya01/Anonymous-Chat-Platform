import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup
options = uc.ChromeOptions()
options.add_argument('--headless')
prefs = {"credentials_enable_service": False,
            "profile.password_manager_enabled": False
            }

options.add_experimental_option("prefs", prefs)

driver = uc.Chrome(options=options)


def ShortLink(desiredLink ,longLink, gmail):
    
    # link = 'https://t.ly/links'
    # link = 'http://lnkiy.com/create-custom-url/'
    print('Link Compression proceed')
    link = 'http://lnkiy.com/lnkiy-signIn'
    # desiredLink = 'shreeHariVishnu'
    driver.get(link)
   
    sleep(1.5)
    name = driver.find_element(By.NAME, "email")
    name.send_keys(gmail)
    passward = driver.find_element(By.NAME, "password")
    passward.send_keys("passward@8732")
    xpath = '/html/body/div[1]/div/div/div[2]/form/button'
    submit = driver.find_element(By.XPATH,xpath)
    submit.click()
    driver.get('http://lnkiy.com/create-custom-url')

    # sleep(4)

    # try:
    #     xpath = '/html/body/div[1]/main/div/div/div[1]/div[2]/div[2]/table/tbody/tr/td[4]/div/button'
    #     dropDown = driver.find_element(By.XPATH , xpath)
    #     dropDown.click() 
    #     xpath = '//*[@id="spark-app"]/main/div/div/div[1]/div[2]/div[2]/table/tbody/tr/td[4]/div/div/a[5]'
    #     delete = driver.find_element(By.XPATH,xpath)
    #     delete.click()
    #     sleep(.7)
    #     xpath = '/html/body/div[4]/div/div[3]/button[1]'
    #     sure = driver.find_element(By.XPATH,xpath)
    #     sure.click()
    # except:pass

    # sleep(1)

   
    xpath = '//*[@id="longLink"]'
    inputLink = driver.find_element(By.XPATH,xpath)
    inputLink.send_keys(longLink)
    xpath = '//*[@id="customLink"]'
    DesiredLink = driver.find_element(By.XPATH,xpath)
    DesiredLink.send_keys(desiredLink)
    xpath = '//*[@id="home"]/div/div/div[2]/form[2]/button'
    ShortenBtn = driver.find_element(By.XPATH,xpath)
    ShortenBtn.click()
    

    # print(driver.page_source)
    sleep(1)
    status = "Name Avaialble To Be Used"
    airLink = f'http://darkroom.lnkiy.in/{desiredLink}'
    repeat = False
    
    try:
        id_ = 'ardyacsl'
        notice = driver.find_element(By.ID,id_)
        if 'This keyword is already in use' == notice.text:    
            status = "Name Already In Use"
            repeat = True
    except:pass

    return [repeat,status,airLink]




    # soup = BeautifulSoup(driver.page_source, 'html5lib')
    # file_ = open("test.txt",'+w')
    # file_.write(soup.text)
    # file_.close()
    
    # a = soup.find('a', attrs = {'id':'myInput'})
    # print(a)
    # style = '#most_recent_links > li > span.short-link'
    # freshLink = driver.find_element(By.CSS_SELECTOR,style)
    # freshLink.get_attribute('innerHTML')
    # print(freshLink.text)
    # print(freshLink)
    # print(freshLink.find_element(By.TAG_NAME,'a'))
    # ID= 'myInput'

    # xpath = '/html/body/div[1]/div/div/div[2]/div[1]/ul/li/span[2]/a'
    # freshLink = driver.find_element(By.XPATH , xpath)
    # freshLink = freshLink.get_attribute('innerHTML')
    # print(freshLink)

  


    # sleep(3)
    # xpath = '/html/body/div[1]/main/div/div/div[1]/div[2]/div[2]/table/tbody/tr/td[4]/div/button'
    # dropDown = driver.find_element(By.XPATH , xpath)
    # dropDown.click() 
    # xpath = '//*[@id="spark-app"]/main/div/div/div[1]/div[2]/div[2]/table/tbody/tr/td[4]/div/div/a[2]'
    # Edit = driver.find_element(By.XPATH,xpath)
    # Edit.click()

    # sleep(1)
    # # id_ = 'shortUrlEnding'
    # xpath= '/html/body/div[1]/main/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/form/div[1]/div/input'
    # shorturlInput = driver.find_element(By.XPATH,xpath)
    # shorturlInput.clear()
    # shorturlInput.send_keys(desiredLink)

    # # sleep(.3)
    # xpath = '//*[@id="updateLink"]/div/div/div[3]/button'
    # save = driver.find_element(By.XPATH,xpath)
    # save.click()

    # sleep(3)
    # try:
    #     xpath = '/html/body/div[1]/main/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/button/span'
    #     cross = driver.find_element(By.XPATH,xpath)
    #     cross.click()
    # except:pass

    # # sleep(1)
    # # xpath = '/html/body/div[1]/main/div/div/div[1]/div[2]/div[2]/table/tbody/tr/td[1]/a[1]'
    # style = '#spark-app > main > div > div > div.col-md-8 > div:nth-child(2) > div.table-responsive-md > table > tbody > tr:nth-child(1) > td:nth-child(1) > a.d-lg-none.d-xl-none'
    # FreshLink = driver.find_element(By.CSS_SELECTOR , style)
    # FreshLink = FreshLink.get_attribute("innerHTML")

    # freshLinkText = FreshLink.split("/")[-1]
    # FreshLink = "https://"+FreshLink 
    # status = 'Name Already Exists'
    # if freshLinkText == desiredLink: status = 'Link Created Succesfully'

    # return [status,FreshLink]


