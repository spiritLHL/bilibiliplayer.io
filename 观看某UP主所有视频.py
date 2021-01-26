from selenium import webdriver
import time,re,jieba

name = input('输入UP主名字：')
page_times = eval(input('获取第几页前的视频：'))
driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
driver.maximize_window()
'''
driver.get('https://www.bilibili.com/')
time.sleep(3)
cookies = {"_uuid": "1E53F7A4-C37D-3613-A4F2-E347430C120A67962infoc", "bili_jct": "cede360f1a3aee502de6606d41989408", "bp_t_offset_11573578": "392183990769047402", "bsource": "seo_bing", "buvid3": "5C737AB1-F195-4802-9224-8A61D49C983F155809infoc", "CURRENT_FNVAL": "16", "DedeUserID": "11573578",
            "DedeUserID__ckMd5": "ba7282aacf9f8b10","LIVE_BUVID": "AUTO2315901530176561","PVID": "3","rpdid": "|(J~RYumk|~Y0J'ul)mYk~ll~","SESSDATA": "46494355,1605179521,5113e*51","sid": "b7fjrcma"}
driver.add_cookie(cookies)
time.sleep(3)
driver.refresh()
'''
driver.get('https://search.bilibili.com/?spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.11')
time.sleep(2)
driver.find_element_by_css_selector('html body#bili-search div#server-search-app.bili-search div.home-wrap div.home-form div.home-input.clearfix div.input-suggest input#search-keyword.content').send_keys(f'{name}\n')
time.sleep(2)
element = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/div/div[1]/div[3]/ul/li[8]/a')
time.sleep(2)
element.click()
time.sleep(3)
UP = element.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/ul/li/div[2]/div[1]/a[1]')
time.sleep(2)
UP_index = UP.get_attribute('href')
print(UP_index)
time.sleep(2)
#href="//space.bilibili.com/11573578?from=search&seid=9471147394431946391"
UP_ID = re.findall('//space.bilibili.com/(.*?)?from=search&.*?',UP_index,re.S)
print(UP_ID[0][0:-1])
driver.get('https://space.bilibili.com/'+f'{UP_ID[0][0:-1]}'+'/video')
time.sleep(2)
BV = []
try:
    for i in range(page_times):
        list = driver.find_element_by_css_selector('html body div#app.visitor div.s-space div div#page-video.wrapper div.col-full.clearfix div.main-content div#submit-video.section.video div#video-list-style.cube div#submit-video-list.content ul.clearfix.cube-list').find_elements_by_tag_name('li')
        for element in list:
            BV.append(element.get_attribute('data-aid'))
            time.sleep(0.6)
        driver.find_element_by_css_selector('html body div#app.visitor div.s-space div div#page-video.wrapper div.col-full.clearfix div.main-content div#submit-video.section.video div#video-list-style.cube div#submit-video-list.content ul.be-pager li.be-pager-next').click()
        time.sleep(5)
except:
    print('BV号已全部获取完毕')
    print(BV)
urls = []
for bv in BV:
    urls.append('https://www.bilibili.com/video/'+f'{bv}')
print('链接拼接完毕')
print(urls)
for i in urls:
    driver.get(i)
    time.sleep(10)
    page_text = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div[9]/div[2]/div[2]/div[1]/div[2]/div').text
    list_time = jieba.lcut(page_text)
    wait = int(list_time[-3]) * 60 + int(list_time[-1])#播放时长获取
    driver.find_element_by_xpath(
        '/html/body/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div[10]/div[2]/div[2]/div[1]/div[1]/button')
    time.sleep(4)
    print('控件抓取成功')
    driver.find_element_by_xpath(
        '/html/body/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div[10]/div[2]/div[2]/div[1]/div[1]/button').click()
    time.sleep(3)
    print('播放成功')
    print(f'播放时长{wait}秒')
    time.sleep(wait)



