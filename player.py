from selenium import webdriver
import time
import random


driver_A = webdriver.Chrome(r'C:\chromedriver.exe')
#driver_B = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
#driver_C = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
urllists1 = [
'',
''
]

urllists2 = [
'',
''
]

urllists3 = [
'',
''
]




i = 0


def getdetail_A(driver_C=driver_A):
    driver_A.find_element_by_xpath(
        '//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[10]/div[2]/div[2]/div[1]/div[1]/button[1]')
    time.sleep(6)
    print('A控件抓取成功')
    driver_A.find_element_by_xpath(
        '//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[10]/div[2]/div[2]/div[1]/div[1]/button[1]').click()
    time.sleep(5)
    print('A播放成功')



def getdetail_B(driver_B=driver_B):
    driver_B.find_element_by_xpath(
        '/html/body/div[3]/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div[9]/div[2]/div[2]/div[1]/div[1]/button[1]')
    time.sleep(4)
    print('B控件抓取成功')
    driver_B.find_element_by_xpath(
        '/html/body/div[3]/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div[9]/div[2]/div[2]/div[1]/div[1]/button[1]').click()
    time.sleep(3)
    print('B播放成功')
    

def getdetail_C(driver_C=driver_C):
    driver_C.find_element_by_xpath(
        '/html/body/div[3]/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div[9]/div[2]/div[2]/div[1]/div[1]/button[1]')
    time.sleep(4)
    print('C控件抓取成功')
    driver_C.find_element_by_xpath(
        '/html/body/div[3]/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div[9]/div[2]/div[2]/div[1]/div[1]/button[1]').click()
    time.sleep(3)
    print('C播放成功')
    
def get(driver_A=driver_A,driver_B=driver_B,driver_C=driver_C):
        url1 = urllists1[]
        url2 = urllists2[]
        url3 = urllists3[random.randrange( , , )]#这里可以用索引顺序播放或是随机播放
 '''
        try:
            try:
                driver_C.set_page_load_timeout(5)
                driver_C.get(url1)
            except:
                driver_C.refresh()
                print("C_refresh")
        except:
            print('C_error')

        time.sleep(1)

        try:
            try:
                driver_B.set_page_load_timeout(5)
                driver_B.get(url2)
            except:
                driver_B.refresh()
                print("B_refresh")
        except:
            print('B_error')
'''
        try:
            try:
                driver_A.set_page_load_timeout(5)
                driver_A.get(url3)
            except:
                driver_A.refresh()
                print("A_refresh")
        except:
            print('A_error')

t = 0

while True:
    try:
        get()
        time.sleep(3)
        driver_A.maximize_window()
        #driver_B.maximize_window()
        #driver_C.maximize_window()
        time.sleep(3)
        getdetail_A()
        '''
        time.sleep(2)
        getdetail_B()
        time.sleep(3)
        getdetail_C()
        time.sleep()
        '''
        driver_A.delete_all_cookies()
        time.sleep(1)
        '''
        driver_B.delete_all_cookies()
        time.sleep(1)
        driver_C.delete_all_cookies()
        time.sleep(1)
        '''
        time.sleep()#这里填入播放时间，可以用列表注入不同的视频播放时间
    except:
        t = t +1
        print('error has happened {} times'.format(t))
        continue
        
